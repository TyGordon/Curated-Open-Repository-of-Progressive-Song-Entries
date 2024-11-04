import sys
import xml.etree.ElementTree as ET
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QTextEdit
from PyQt6.QtGui import QFont
from PyQt6.uic import loadUi

class MainUI(QMainWindow):

    tree = ET.parse("full_corpus.xml")
    root = tree.getroot()

    # Build the query dynamically
    query_results = []


    def __init__(self):
        super(MainUI, self).__init__()

        loadUi("corpus_gui.ui", self)

        self.tree = ET.parse("full_corpus.xml")
        self.root = self.tree.getroot()

        self.tag_search_pos = str(self.posBox.currentText())

        # Update Functions:
        self.searchButton.clicked.connect(self.on_search)
        self.clearButton.clicked.connect(self.on_clear)
        self.dateAll.clicked.connect(self.on_date_all)
        self.dateNone.clicked.connect(self.on_date_none)
 
        #self.clearButton.clicked.connect(self.on_clear)

    def on_search(self):

        query_results = []
        title_list = [""]
        non_lemmas = []

        ### Match by artist tags
        for artist in self.root.findall("artist"):

            if self.searchArtistName.isChecked() and artist.get("name").lower() != self.valueArtistName.text().lower():
                continue # Artist name required, but not matched. Skip
            

            # Filter by artist genre
            if self.searchArtistGenre.isChecked() and artist.get("genre").lower() != self.valueArtistGenre.currentText().lower():
                continue # Artist genre required, but not matched. Skip

            ### Match by album tags
            for album in artist.findall("al"):

                # Filter by album year
                _album_year = int(album.get("date"))

                # Skip if the year found is not required
                match _album_year:
                    case 1968:
                        if not self.date1968.isChecked():
                            continue
                    case 1969:
                        if not self.date1969.isChecked():
                            continue
                    case 1970:
                        if not self.date1970.isChecked():
                            continue
                    case 1971:
                        if not self.date1971.isChecked():
                            continue
                    case 1972:
                        if not self.date1972.isChecked():
                            continue
                    case 1973:
                        if not self.date1973.isChecked():
                            continue
                    case 1974:
                        if not self.date1974.isChecked():
                            continue
                    case 1975:
                        if not self.date1975.isChecked():
                            continue
                    case 1976:
                        if not self.date1976.isChecked():
                            continue
                    case 1977:
                        if not self.date1977.isChecked():
                            continue
                    case 1978:
                        if not self.date1978.isChecked():
                            continue
                    case 1979:
                        if not self.date1979.isChecked():
                            continue
                    case 1980:
                        if not self.date1980.isChecked():
                            continue
                    case 1981:
                        if not self.date1981.isChecked():
                            continue
                    case 1982:
                        if not self.date1982.isChecked():
                            continue
                    case 1983:
                        if not self.date1983.isChecked():
                            continue
                    case 1984:
                        if not self.date1984.isChecked():
                            continue

                if self.searchAlbumName.isChecked() and album.get("name").lower() != self.valueAlbumName.text().lower():
                    continue # Album name required, but not matched. Skip

                # Filter by album rating
                _album_rating = float(album.findtext("rating"))

                match str(self.searchAlbumRatingOp.currentText()):
                    case ">":
                        if self.searchAlbumRating.isChecked() and not (_album_rating > float(self.valueAlbumRating.text())):
                            continue # Album rating ">" required, but not matched. Skip
                    case "=":
                        if self.searchAlbumRating.isChecked() and not (_album_rating == float(self.valueAlbumRating.text())):
                            continue # Album rating "=" required, but not matched. Skip
                    case "<":
                        if self.searchAlbumRating.isChecked() and not (_album_rating < float(self.valueAlbumRating.text())):
                            continue # Album rating "<" required, but not matched. Skip

                # Filter by album length
                _album_length = int(album.findtext("length"))

                match str(self.searchAlbumLengthOp.currentText()):
                    case ">":
                        if self.searchAlbumLength.isChecked() and not (_album_length > int(self.valueAlbumLength.text())):
                            continue # Album length ">" required, but not matched. Skip
                    case "=":
                        if self.searchAlbumLength.isChecked() and not (_album_length == int(self.valueAlbumLength.text())):
                            continue # Album length "=" required, but not matched. Skip
                    case "<":
                        if self.searchAlbumLength.isChecked() and not (_album_length < int(self.valueAlbumLength.text())):
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
                            case _:
                                _track_index = -1

                    _previous_h = False

                    match str(self.searchTrackIndexOp.currentText()):
                        case ">":
                            if self.searchTrackIndex.isChecked() and not (_track_index > int(self.valueTrackIndex.text())):
                                continue # Track index ">" required, but not matched. Skip
                        case "=":
                            if self.searchTrackIndex.isChecked() and not (_track_index == int(self.valueTrackIndex.text())):
                                continue # Track index "=" required, but not matched. Skip
                        case "<":
                            if self.searchTrackIndex.isChecked() and not (_track_index < int(self.valueTrackIndex.text())):
                                continue # Track index "<" required, but not matched. Skip

                    # Filter by track length
                    _track_length = int(track.findtext("length"))

                    match str(self.searchTrackLengthOp.currentText()):
                        case ">":
                            if self.searchTrackLength.isChecked() and not (_track_length > int(self.valueTrackLength.text())):
                                continue # Track length ">" required, but not matched. Skip
                        case "=":
                            if self.searchTrackLength.isChecked() and not (_track_length == int(self.valueTrackLength.text())):
                                continue # Track length "=" required, but not matched. Skip
                        case "<":
                            if self.searchTrackLength.isChecked() and not (_track_length < int(self.valueTrackLength.text())):
                                continue # Track length "<" required, but not matched. Skip

                    # Filter by track word count
                    _track_word_count = len(track.findall('w'))

                    match str(self.searchTrackWordcountOp.currentText()):
                        case ">":
                            if self.searchTrackWordcount.isChecked() and not (_track_word_count > int(self.valueTrackWordcount.text())):
                                continue # Track word count ">" required, but not matched. Skip
                        case "=":
                            if self.searchTrackWordcount.isChecked() and not (_track_word_count == int(self.valueTrackWordcount.text())):
                                continue # Track word count "=" required, but not matched. Skip
                        case "<":
                            if self.searchTrackWordcount.isChecked() and not (_track_word_count < int(self.valueTrackWordcount.text())):
                                continue # Track word count "<" required, but not matched. Skip

                    ### Match by word tags
                    for word in track.findall("w"):

                        if str(self.queryLine.text()) != "":
                            # Filter by word part of speech
                            #if self.tag_search_pos != "---" and word.get("pos") != str(self.posBox.currentText()):
                            #    continue

                            # Filter by lemma
                            if self.lemmaCheckBox.isChecked():
                                if word.get("lemma") != str(self.queryLine.text()):
                                    continue
                                #else:
                                    #print("Query: " + str(self.queryLine.text()) + " Match: " + word.get("lemma"))
                            else:
                                if str(word.text) != str(self.queryLine.text()):
                                    continue
                        else:
                            title_list.append("")

                        if str(word.text) not in non_lemmas:
                            non_lemmas.append(str(word.text))

                        # Add the track to results if all conditions met
                        #query_results.append((artist.get("name"), album.get("name"), track.get("index"), word.text))

                        path = ".//artist[@name=\"" + artist.get("name") + "\"]/al[@name=\"" + album.get("name") + "\"]/tr[@index=\"" + track.get("index") + "\"]"
                        
                        
                        query_results.append((path, artist.get("name"), album.get("name")))
                        # print (path)

                        #.//artist[@name="Alan Parsons Project"]/al[@name="Tales of Mystery and Imagination"]/tr[@index="1"]

        concordance = ""
        artist_change = False
        previous_title = ""
        previous_artist = ""
        title_count = 0
        artist_count = 0

        # Output the results
        for r in query_results:
            tr = self.tree.find(r[0])

            title = ""
            ar_title = ""
            plain_title = ""
            artist_change = False
            for w in tr.findall("w"):
                if w.text[0] == '\'' or w.text == "n't":
                    title = title[0:-1]
                    
                if previous_artist != r[1]:
                    artist_change = True
                    previous_artist = r[1]
                    artist_string = "- = - " + r[1] + " - = -"
                    ar_title += "<br><b>" + artist_string + "</b><br>"
                    artist_count += 1
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


                title_list.append(plain_title + " (" + r[2] + ")")

            current_title = title + " (" + r[2] + ")<br>"

            if artist_change:
                full_title = ar_title + current_title
            else:
                full_title = current_title

            #full_title = title +  "<br>" #+ "---->" + r[1] + "  /  " + r[2] + "<br>"
            
            #print("Previous: " + previous_title + " Current: " + full_title)

            if previous_title != current_title:
                title_count += 1
                concordance += full_title
                previous_title = current_title

            #print(title)

        max_char_len = len(max(title_list , key = len))
        print("Max character length: " + str(max_char_len))

        centered = "<p style='text-align: center;'>"

        html_concordance = "<b>" + str(title_count - artist_count) + " hits</b>" + concordance #+ "</p>"

        # Horizontal width
        self.concordance.setLineWrapColumnOrWidth(max_char_len * 8) # Set the width
        self.concordance.setLineWrapMode(QTextEdit.LineWrapMode.FixedPixelWidth)

        new_font = QFont("Consolas", 10)
        self.concordance.setFont(new_font)

        if max_char_len == 0:
            self.concordance.setText("<b>No matches found</b>")
        else:
            self.concordance.setText(html_concordance)

        print("Query: " + self.queryLine.text())

        # [End] on_search

    def on_clear(self):
        self.queryLine.setText("")
        self.concordance.setText("")

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
    ui.show()
    app.exec()
