import sys
import ctypes
import copy
import re
import xml.etree.ElementTree as ET
from lxml import etree
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QSplashScreen, QMainWindow, QTextEdit
#from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt, QObject, QRect, QTimer, QThread, pyqtSignal
#from PyQt6.QtCore import QObject, QThread, pyqtSignal

myappid = u'UK.CORPSE.Explorer.1.01' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class SearchWorker(QObject):
    progress = pyqtSignal(int)
    finished = pyqtSignal(int, str)
    chain = pyqtSignal(list)

    def __init__(self, root, query_params):
        super().__init__()
        self.root = query_params["root"]
        self.params = query_params
        self.interrupted = False

    # Converts time strings in the format NN:NN to seconds (int type)
    def to_seconds(self, input_string: str) -> str:
        TIME_REGEX = '^([0-9]*?):([0-9]*?)$'
        HOUR_REGEX = '^([0-9]*?):([0-9]*?):([0-9]*?)$'
        SECONDS_IN_MINUTE = 60
        SECONDS_IN_HOUR = 3600

        input_string = str(input_string)

        print("input: " + input_string)

        #input_string = input_string.replace(" ", "").replace("(", "").replace(")", "")

        if not re.match(TIME_REGEX, input_string):
            if re.match(HOUR_REGEX, input_string):  # Handle strings with hours
                r = re.compile(HOUR_REGEX)
                hours = int(re.sub(r, r'\1', input_string))
                minutes = int(re.sub(r, r'\2', input_string))
                seconds = int(re.sub(r, r'\3', input_string))
                output = ((hours * SECONDS_IN_HOUR) + (minutes * SECONDS_IN_MINUTE) + seconds)
                return output
                
            print ("INVALID TIME FORMAT, REQUIRES NN:NN")
            print ("Given: \'" + input_string + "\'")
            return "1"

        r = re.compile(TIME_REGEX)
        minutes = re.sub(r, r'\1', input_string)
        seconds = re.sub(r, r'\2', input_string)
        
        output = str((int(minutes) * SECONDS_IN_MINUTE) + int(seconds))

        print("output: " + output)

        return output

    def run(self):
        
        # Emit 0% progress at start
        self.progress.emit(0)
        _total_items = self.params["total_words"]
        
        query_results = []
        title_list = [""]
        non_lemmas = []

        lemma_count = sum(1 for w in self.params["tree"].iter("w") if w.get("lemma") == self.params["query_value"])

        TIME_REGEX = '^([0-9]*?):([0-9]*?)$'
        HOUR_REGEX = '^([0-9]*?):([0-9]*?):([0-9]*?)$'

        # Handle ill-formed input

        # Pre-process the track/album lengths
        if self.params["album_length_search"]:
            if re.match(TIME_REGEX, self.params["album_length_value"]) or re.match(HOUR_REGEX, self.params["album_length_value"]):
                self.params["album_length_value"] = self.to_seconds(self.params["album_length_value"])
                print(self.to_seconds(self.params["album_length_value"]))
                #print(self.params["album_length_value"])
            elif not self.params["album_length_value"].isnumeric(): # Handle invalid format
                self.finished.emit(20, "Invalid Search, Album Length Non-Numeric")
                return

        if self.params["track_length_search"]:
            if re.match(TIME_REGEX, self.params["track_length_value"]) or re.match(HOUR_REGEX, self.params["track_length_value"]):
                self.params["track_length_value"] = self.to_seconds(self.params["track_length_value"])
                print(self.params["track_length_value"])
            elif not self.params["track_length_value"].isnumeric(): # Handle invalid format
                self.finished.emit(20, "Invalid Search, Track Length Non-Numeric")
                return

        if self.params["album_rating_search"]:
            if not self.params["album_rating_value"].isnumeric(): # Handle invalid format
                self.finished.emit(20, "Invalid Search, Album Rating Non-Numeric")
                return
            
        if self.params["track_index_search"]:
            if not self.params["track_index_value"].isnumeric(): # Handle invalid format
                self.finished.emit(20, "Invalid Search, Track Index Non-Numeric")
                return
            
        if self.params["track_wordcount_search"]:
            if not self.params["track_wordcount_value"].isnumeric(): # Handle invalid format
                self.finished.emit(20, "Invalid Search, Track Word Count Non-Numeric")
                return
        
        if self.params["word_index_search"]:
            if not self.params["word_index_value"].isnumeric(): # Handle invalid format
                self.finished.emit(20, "Invalid Search, Word Index Non-Numeric")
                return


        _progress_count = 0
        for artist in self.params["root"].findall("artist"):
            if self.interrupted:
                break

            if self.params["artist_name_search"] and artist.get("name").lower() != self.params["artist_name_value"].lower():
                _progress_count += 1
                continue # Artist name required, but not matched. Skip

            # Filter by artist genre
            if self.params["artist_genre_search"] and artist.get("genre").lower() != self.params["artist_genre_value"].lower():
                _progress_count += 1
                continue # Artist genre required, but not matched. Skip

            ### Match by album tags
            for album in artist.findall("al"):

                # Filter by album year
                #_album_year = int(album.get("date"))
                _album_year = album.get("date")

                if not self.params[str(_album_year)]:
                    _progress_count += 1
                    continue  # Skip if the year is unchecked

                if self.params["album_name_search"] and album.get("name").lower() != self.params["album_name_value"].lower():
                    _progress_count += 1
                    continue # Album name required, but not matched. Skip

                # Filter by album rating
                _album_rating = float(album.findtext("rating"))

                match str(self.params["album_rating_op"]):
                    case ">":
                        if self.params["album_rating_search"] and not (_album_rating > float(self.params["album_rating_value"])):
                            _progress_count += 1
                            continue # Album rating ">" required, but not matched. Skip
                    case "=":
                        if self.params["album_rating_search"] and not (_album_rating == float(self.params["album_rating_value"])):
                            _progress_count += 1
                            continue # Album rating "=" required, but not matched. Skip
                    case "<":
                        if self.params["album_rating_search"] and not (_album_rating < float(self.params["album_rating_value"])):
                            _progress_count += 1
                            continue # Album rating "<" required, but not matched. Skip

                # Filter by album length
                _album_length = int(album.findtext("length"))

                match str(self.params["album_length_op"]):
                    case ">":
                        if self.params["album_length_search"] and not (_album_length > int(self.params["album_length_value"])):
                            _progress_count += 1
                            continue # Album length ">" required, but not matched. Skip
                    case "=":
                        if self.params["album_length_search"] and not (_album_length == int(self.params["album_length_value"])):
                            _progress_count += 1
                            continue # Album length "=" required, but not matched. Skip
                    case "<":
                        if self.params["album_length_search"] and not (_album_length < int(self.params["album_length_value"])):
                            _progress_count += 1
                            continue # Album length "<" required, but not matched. Skip

                _previous_h = False

                ### Match by track tags
                for track in album.findall("tr"):

                    #for word in track.findall("w"):
                    #    print(word.text)

                    _track_index_str = track.get("index").replace(" ", "").lower()
                    _track_index = 0

                    if _track_index_str.isnumeric():
                        _track_index = int(_track_index_str)
                    elif _track_index_str == "":
                        _track_index = -1
                    else:
                        match _track_index_str:
                            case 'a':
                                _track_index = 1
                            case 'b':
                                _track_index = 2
                            case 'c':
                                _track_index = 3
                            case 'd':
                                _track_index = 4
                            case 'e':
                                _track_index = 5
                            case 'f':
                                _track_index = 6
                            case 'g':
                                _track_index = 7
                            case 'h':
                                _previous_h = True
                                _track_index = 8
                            case 'i':
                                if _previous_h:
                                    _track_index = 1
                                else:
                                    _track_index = 9
                            case 'j':
                                _track_index = 10
                            case 'k':
                                _track_index = 11
                            case 'l':
                                _track_index = 12
                            case "ii":
                                _track_index = 2
                            case "iii":
                                _track_index = 3
                            case "iv":
                                _track_index = 4
                            case 'v':
                                _track_index = 5
                            case "vi":
                                _track_index = 6
                            case "vii":
                                _track_index = 7
                            case "viii":
                                _track_index = 8
                            case "iv":
                                _track_index = 9
                            case "x":
                                _track_index = 10
                            case "xi":
                                _track_index = 11
                            case "xii":
                                _track_index = 12
                            case _:
                                _track_index = -1

                    _previous_h = False

                    match str(self.params["track_index_op"]):
                        case ">":
                            if self.params["track_index_search"] and not (_track_index > int(self.params["track_index_value"])):
                                _progress_count += 1
                                continue # Track index ">" required, but not matched. Skip
                        case "=":
                            if self.params["track_index_search"] and not (_track_index == int(self.params["track_index_value"])):
                                _progress_count += 1
                                continue # Track index "=" required, but not matched. Skip
                        case "<":
                            if self.params["track_index_search"] and not (_track_index < int(self.params["track_index_value"])):
                                _progress_count += 1
                                continue # Track index "<" required, but not matched. Skip

                    # Filter by track length
                    _track_length = int(track.findtext("length"))

                    match str(self.params["track_length_op"]):
                        case ">":
                            if self.params["track_length_search"] and not (_track_length > int(self.params["track_length_value"])):
                                _progress_count += 1
                                continue # Track length ">" required, but not matched. Skip
                        case "=":
                            if self.params["track_length_search"] and not (_track_length == int(self.params["track_length_value"])):
                                _progress_count += 1
                                continue # Track length "=" required, but not matched. Skip
                        case "<":
                            if self.params["track_length_search"] and not (_track_length < int(self.params["track_length_value"])):
                                _progress_count += 1
                                continue # Track length "<" required, but not matched. Skip

                    # Filter by track word count
                    _track_word_count = len(track.findall('w'))

                    match str(self.params["track_wordcount_op"]):
                        case ">":
                            if self.params["track_wordcount_search"] and not (_track_word_count > int(self.params["track_wordcount_value"])):
                                _progress_count += 1
                                continue # Track word count ">" required, but not matched. Skip
                        case "=":
                            if self.params["track_wordcount_search"] and not (_track_word_count == int(self.params["track_wordcount_value"])):
                                _progress_count += 1
                                continue # Track word count "=" required, but not matched. Skip
                        case "<":
                            if self.params["track_wordcount_search"] and not (_track_word_count < int(self.params["track_wordcount_value"])):
                                _progress_count += 1
                                continue # Track word count "<" required, but not matched. Skip

                    _null_query_index = 1

                    ### Match by word tags
                    for word in track.findall("w"):

                        path = ".//artist[@name=\"" + artist.get("name") + "\"]/al[@name=\"" + album.get("name") + "\"]/tr[@index=\"" + track.get("index") + "\"]"

                        if str(self.params["query_value"]) != "": # There is an entry
                            # Filter by part of speech
                            
                            if str(self.params["pos_value"]) != "---" and word.get("pos") != str(self.params["pos_value"]):
                                continue
                            #print("Entry POS: " + word.get("pos") + " POS Query: " + str(self.params["pos_value"]))

                            word_index = 1

                            # Filter by lemma
                            if self.params["lemma_checked"]:

                                if word.get("lemma") != str(self.params["query_value"]):
                                    _progress_count += 1
                                    continue
                                else:
                                    # Iterate over each <w> element in the current track
                                    for w in track.findall("w"):
                                        # print(w.text)
                                        if w.get("lemma") == self.params["query_value"]:
                                            break
                                        word_index += 1

                                if self.params["word_index_search"]:
                                    if word_index != int(self.params["word_index_value"]):
                                        # print("Word Index: " + str(word_index) + " Search Index: " + self.params["word_index_value"])
                                        _progress_count += 1
                                        continue
                            else:   # Filter by match
                                if self.params["case_checked"]:     # Case sensitive
                                    if str(word.text) != str(self.params["query_value"]):
                                        _progress_count += 1
                                        continue
                                    else:
                                        # Iterate over each <w> element in the current track
                                        for w in track.findall("w"):
                                            # print(w.text)
                                            if w.text == self.params["query_value"]:
                                                break
                                            word_index += 1
                                else:   # Case insensitive
                                    if str(word.text).lower() != str(self.params["query_value"]).lower():
                                        _progress_count += 1
                                        continue
                                    else:
                                        # Iterate over each <w> element in the current track
                                        for w in track.findall("w"):
                                            # print(w.text)
                                            if w.text.lower() == self.params["query_value"].lower():
                                                break
                                            word_index += 1

                                if self.params["word_index_search"]:
                                    if word_index != int(self.params["word_index_value"]):
                                        # print("Word Index: " + str(word_index) + " Search Index: " + self.params["word_index_value"])
                                        _progress_count += 1
                                        continue
                        else:   # Null-entry search
                            if str(self.params["pos_value"]) != "---" and word.get("pos") != str(self.params["pos_value"]):
                                _null_query_index += 1
                                continue

                            if self.params["word_index_search"]:
                                    if _null_query_index != int(self.params["word_index_value"]):
                                        # print("Word Index: " + str(word_index) + " Search Index: " + self.params["word_index_value"])
                                        _progress_count += 1
                                        _null_query_index += 1
                                        continue
                                    else:
                                        print(str(_null_query_index) + " " + word.text)

                            title_list.append("")

                        if str(word.text) not in non_lemmas:
                            non_lemmas.append(str(word.text))

                        # Add the track to results if all conditions met
                        #query_results.append((artist.get("name"), album.get("name"), track.get("index"), word.text))
                        
                        query_results.append((path, artist.get("name"), album.get("name")))
                        _progress_count += 1
                        _null_query_index += 1

            # Update progress
            if _progress_count % 10 == 0:
                self.progress.emit(int((_progress_count / _total_items) * 100))
                #print("Progress: " + str(int((_progress_count / _total_items) * 100)))
                if _progress_count % 100 == 0:  # Throttle QApplication events to every 100 items
                    QApplication.processEvents()

        artist_change = False
        concordance = previous_title = previous_artist =""

        # Output the results
        for r in query_results:
            tr = self.params["tree"].find(r[0])

            title = ""
            ar_title = ""
            plain_title = ""
            artist_change = False
                
            for w in tr.findall(".//*"):
                if w.tag in {"w", "punc"}:
                    if w.text[0] == '\'' or w.text == "n't":
                        title = title[0:-1]
                        
                    if previous_artist != r[1]:
                        artist_change = True
                        previous_artist = r[1]
                        artist_string = "- = - " + r[1] + " - = -"
                        ar_title += "<br><b>" + artist_string + "</b><br>"
                        title_list.append(artist_string)
                    
                    is_word = False
                    for i in non_lemmas:
                        if w.text == i:
                            is_word = True

                    if is_word:
                        title += "<b>" + w.text + "</b> "
                    else:
                        title += w.text + " "
                    
                    plain_title += w.text + " "

                    title_list.append(plain_title + " [" + r[2] + "]")

            current_title = title + " (" + r[2] + ")<br>"

            trans = tr.find("trans")  # Find the translation tag
            if trans is not None:  # Check if it exists
                current_title = current_title + "<em>    ==> " + trans.text + "</em><br>"

            if artist_change:
                full_title = ar_title + current_title
            else:
                full_title = current_title
            
            #print("Previous: " + previous_title + " Current: " + full_title)

            if previous_title != current_title:
                concordance += full_title
                previous_title = current_title

            #print(title)

        max_char_len = len(max(title_list , key = len))
        print("Max character length: " + str(max_char_len))

        centered_format = "<p style='text-align: center;'>"

        concordance_array = concordance.replace("<br>", "\n").splitlines()

        line_count = 0
        for line in concordance_array:
            if "- = -" not in line and "==>" not in line and line != "":
                line_count += 1
        
        lemma_percentage = (lemma_count / self.params["total_words"]) * 100
        lemma_percentage = round(lemma_percentage, 2)

        titles_percentage = (line_count / self.params["total_titles"]) * 100
        titles_percentage = round(titles_percentage, 2)
        

        html_concordance = ("<b>" + str(line_count) + " hits</b><br>" + "<b> Lemma Frequency: "
                            + str(lemma_count) + " / " + str(self.params["total_words"])
                            + " | " + str(lemma_percentage) + "%</b>><br>" + "<b> Title Frequency: "
                            + str(line_count) + " / " + str(self.params["total_titles"])
                            + " | " + str(titles_percentage) + "%</b>" + concordance) #+ "</p>"

        if max_char_len == 0:
            result_text = centered_format + "<br><b>No matches found</b><br>"
        else:
            result_text = html_concordance

        print("Query: " + self.params["query_value"])

        # Emit signal with concordance results

        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-= CHAIN ON/OFF -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

        #self.chain.emit(query_results)
        self.finished.emit(max_char_len, result_text)
        

    def stop(self):
        self.interrupted = True

class MainUI(QMainWindow):
    # Build the query dynamically
    query_results = []

    def __init__(self):
        super(MainUI, self).__init__()

        loadUi("corpus_gui.ui", self)

        #self.setWindowIcon(QIcon("uk_icon.ico"))
        self.setWindowIcon(QIcon("Images/uk_image.png"))

        self.tree = ET.parse("full_corpus.xml")
        self.root = self.tree.getroot()
        self.prev_chain = False
        self.amberIndicator.hide()

        # Hide unimplemented features
        self.HIDE_TYPE_SEARCH = True
        self.HIDE_CHAIN_SEARCH = True

        if self.HIDE_CHAIN_SEARCH:
            self.redIndicator.hide()
            self.chainIcon.hide()
            self.chainButton.hide()

        if self.HIDE_TYPE_SEARCH:
            self.searchTrackType.hide()
            self.valueTrackType.hide()

        ADJUSTMENT_CONSTANT = 5

        self.total_words = sum(1 for _ in self.tree.iter("w"))
        self.total_titles = sum(1 for _ in self.tree.iter("tr")) - ADJUSTMENT_CONSTANT

        self.lemma_dict = {}

        # Iterate over all <w> elements and count each lemma
        for w in self.tree.iter("w"):
            _lemma = w.get("lemma")
            if _lemma:
                # Increment the count of this lemma in the dictionary
                if _lemma in self.lemma_dict:
                    self.lemma_dict[_lemma] += 1
                else:
                    self.lemma_dict[_lemma] = 1

        # Calculate percentages and create a list of 3-tuples (lemma, count, percentage)
        lemma_percentages = [(lemma, count, (count / self.total_words) * 100) for lemma, count in self.lemma_dict.items()]

        # Sort by percentage in descending order (optional)
        lemma_percentages.sort(key=lambda x: x[2], reverse=True)

        self.corpus_stats = "\n".join([f"{count},  {percentage:.2f}%  {lemma}" 
                           for lemma, count, percentage in lemma_percentages])

        self.corpus_stats = "Corpus Statistics:\n" + self.corpus_stats

        self.concordance.setText(self.corpus_stats)

        self.searchProgressBar.setValue(0)
        self.searchProgressBar.hide()

        # Update Functions:
        #self.searchButton.clicked.connect(self.on_search)
        self.searchButton.clicked.connect(lambda: self.start_search(False))
        self.chainButton.clicked.connect(lambda: self.start_search(True))
        self.clearButton.clicked.connect(self.on_clear)
        self.statsButton.clicked.connect(self.on_stats)
        self.dateAll.clicked.connect(self.on_date_all)
        self.dateNone.clicked.connect(self.on_date_none)

        #self.clearButton.clicked.connect(self.on_clear)

    def start_search(self, is_chain):

        _tree = self.tree
        _root = self.root

        if not self.HIDE_CHAIN_SEARCH:
            if is_chain: # <-- Should always be False if left unimplemented
                if self.prev_chain:
                    pass
                    #_tree = ET.parse("subset_corpus.xml")
                    #_root = _tree.getroot()
                
                self.prev_chain = True
                self.amberIndicator.show()
                self.redIndicator.hide()
            else:
                self.prev_chain = False
                self.amberIndicator.hide()
                self.redIndicator.show()

        query_params = {
        "tree": _tree,
        "root": _root,
        "total_words": self.total_words,
        "total_titles": self.total_titles,

        "query_value": self.queryLine.text(),
        "case_checked": self.caseCheckBox.isChecked(),
        "lemma_checked": self.lemmaCheckBox.isChecked(),
        "word_index_search": self.searchWordIndex.isChecked(),
        "word_index_value": self.valueWordIndex.text(),
        "pos_value": self.posBox.currentText(),

        # Artist parameters
        "artist_name_search": self.searchArtistName.isChecked(),
        "artist_name_value": self.valueArtistName.text(),

        "artist_genre_search": self.searchArtistGenre.isChecked(),
        "artist_genre_value": self.valueArtistGenre.currentText(),
        
        # Album parameters
        "1966": self.date1968.isChecked(),
        "1967": self.date1968.isChecked(),
        "1968": self.date1968.isChecked(),
        "1969": self.date1969.isChecked(),
        "1970": self.date1970.isChecked(),
        "1971": self.date1971.isChecked(),
        "1972": self.date1972.isChecked(),
        "1973": self.date1973.isChecked(),
        "1974": self.date1974.isChecked(),
        "1975": self.date1975.isChecked(),
        "1976": self.date1976.isChecked(),
        "1977": self.date1977.isChecked(),
        "1978": self.date1978.isChecked(),
        "1979": self.date1979.isChecked(),
        "1980": self.date1980.isChecked(),
        "1981": self.date1981.isChecked(),
        "1982": self.date1982.isChecked(),
        "1983": self.date1983.isChecked(),
        "1984": self.date1984.isChecked(),

        "album_name_search": self.searchAlbumName.isChecked(),
        "album_name_value": self.valueAlbumName.text(),

        "album_rating_search": self.searchAlbumRating.isChecked(),
        "album_rating_op": self.searchAlbumRatingOp.currentText(),
        "album_rating_value": self.valueAlbumRating.text(),

        "album_length_search": self.searchAlbumLength.isChecked(),
        "album_length_op": self.searchAlbumLengthOp.currentText(),
        "album_length_value": self.valueAlbumLength.text(),

        # Track parameters
        "track_index_search": self.searchTrackIndex.isChecked(),
        "track_index_op": self.searchTrackIndexOp.currentText(),
        "track_index_value": self.valueTrackIndex.text(),

        "track_length_search": self.searchTrackLength.isChecked(),
        "track_length_op": self.searchTrackLengthOp.currentText(),
        "track_length_value": self.valueTrackLength.text(),

        "track_wordcount_search": self.searchTrackWordcount.isChecked(),
        "track_wordcount_op": self.searchTrackWordcountOp.currentText(),
        "track_wordcount_value": self.valueTrackWordcount.text()}

        # Spin up thread and worker with the parameters
        self.thread = QThread()
        self.thread.setParent(None)  # Detach the thread from the parent to prevent premature destruction
        self.worker = SearchWorker(self.root, query_params)
        self.worker.moveToThread(self.thread)

        # Connect signals
        self.thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.search_finished)
        self.worker.finished.connect(self.thread.quit)
        self.worker.chain.connect(self.save_subset)
        self.thread.finished.connect(self.thread.deleteLater)

        # Start the thread
        self.searchButton.setEnabled(False)
        self.clearButton.setEnabled(False)
        self.statsButton.setEnabled(False)
        self.searchProgressBar.show()
        self.thread.start()

    def update_progress(self, value):
        self.searchProgressBar.setValue(value)

    def search_finished(self, max_char_len, result_text):
        self.searchButton.setEnabled(True)
        self.clearButton.setEnabled(True)
        self.statsButton.setEnabled(True)

        # Horizontal width
        self.concordance.setLineWrapColumnOrWidth(max_char_len * 8) # Set the width
        self.concordance.setLineWrapMode(QTextEdit.LineWrapMode.FixedPixelWidth)

        new_font = QFont("Consolas", 10)
        self.concordance.setFont(new_font)

        self.searchProgressBar.hide()
        self.concordance.setText(result_text)
        #self.save_subset(query_results)

    def closeEvent(self, event):
        if hasattr(self, 'worker'):
            self.worker.stop()
            if hasattr(self, 'thread') and self.thread.isRunning():
                self.thread.quit()
                self.thread.wait()  # Ensure the thread exits cleanly before destroying it
        event.accept()

    # DEBUG
    def save_subset(self, query_results):   # Only called via chain-search

        # THIS FUNCTION IS AI-GENERATED AND DOES NOT WORK AS INTENDED

        # Create a new XML tree with root <corpus>
        subset_root = etree.Element("corpus")
        output_file = "subset_corpus.xml"

        # Parse the full corpus using lxml
        full_corpus_tree = etree.parse("full_corpus.xml")
        root = full_corpus_tree.getroot()

        # A dictionary to store already-added artists and albums
        artist_map = {}

        for result in query_results:
            path = result[0]
            matching_elements = root.xpath(path)

            for element in matching_elements:
                # Find the ancestor artist and album elements
                artist = element.xpath("ancestor::artist")[0]
                album = element.xpath("ancestor::al")[0]

                # Ensure artist exists in the subset
                artist_name = artist.get("name")
                if artist_name not in artist_map:
                    # Deep copy the artist and add it to the root
                    copied_artist = copy.deepcopy(artist)
                    subset_root.append(copied_artist)
                    artist_map[artist_name] = copied_artist
                else:
                    # Use the existing artist node in the subset
                    copied_artist = artist_map[artist_name]

                # Ensure album exists under this artist
                album_name = album.get("name")
                # Use XPath with parameters for safety
                existing_album = copied_artist.xpath(f"./al[@name=$name]", name=album_name)
                if not existing_album:
                    # Deep copy the album and add it under the artist
                    copied_album = copy.deepcopy(album)
                    copied_artist.append(copied_album)
                else:
                    # Use the existing album node
                    copied_album = existing_album[0]

                # Append the matching element under the album
                copied_album.append(copy.deepcopy(element))

        # Write the new XML tree to a file
        with open(output_file, "wb") as file:
            file.write(etree.tostring(subset_root, pretty_print=True, encoding="UTF-8", xml_declaration=True))
        print(f"Subset saved to {output_file}")

    def on_clear(self):
        self.queryLine.setText("")
        self.concordance.setText("")

    def on_stats(self):
        self.concordance.setText(self.corpus_stats)

    def on_date_all(self):
        self.date1968.setChecked(True)
        self.date1969.setChecked(True)
        self.date1970.setChecked(True)
        self.date1971.setChecked(True)
        self.date1972.setChecked(True)
        self.date1973.setChecked(True)
        self.date1974.setChecked(True)
        self.date1975.setChecked(True)
        self.date1976.setChecked(True)
        self.date1977.setChecked(True)
        self.date1978.setChecked(True)
        self.date1979.setChecked(True)
        self.date1980.setChecked(True)
        self.date1981.setChecked(True)
        self.date1982.setChecked(True)
        self.date1983.setChecked(True)
        self.date1984.setChecked(True)

    def on_date_none(self):
        self.date1968.setChecked(False)
        self.date1969.setChecked(False)
        self.date1970.setChecked(False)
        self.date1971.setChecked(False)
        self.date1972.setChecked(False)
        self.date1973.setChecked(False)
        self.date1974.setChecked(False)
        self.date1975.setChecked(False)
        self.date1976.setChecked(False)
        self.date1977.setChecked(False)
        self.date1978.setChecked(False)
        self.date1979.setChecked(False)
        self.date1980.setChecked(False)
        self.date1981.setChecked(False)
        self.date1982.setChecked(False)
        self.date1983.setChecked(False)
        self.date1984.setChecked(False)

# Main Function / Driver
if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui = MainUI()

    # Create splash screen
    pixmap = QPixmap("Images/splash_image.png")
    splash = QSplashScreen(pixmap)
    splash.show()

    QApplication.processEvents()

    # Close the splash screen and show GUI after 3 seconds
    QTimer.singleShot(3000, lambda: (splash.close(), ui.show()))

    app.exec()
