import re
import os
import nltk
import string

from deep_translator import GoogleTranslator
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

# Line number constants

OFFSET = 1

ARTIST_LINE = 6 - OFFSET
#RATING_LINE = 20 - OFFSET
RATING_LINE = 45 - OFFSET
#DATE_LINE = 55 - OFFSET
DATE_LINE = 98 - OFFSET
#LISTING_LINE = 57 - OFFSET
LISTING_LINE = 101 - OFFSET

should_write = True

# Converts time strings in the format NN:NN to seconds (int type)
def to_seconds(input_string: str) -> int:
    TIME_REGEX = '^([0-9]*?):([0-9]*?)$'
    HOUR_REGEX = '^([0-9]*?):([0-9]*?):([0-9]*?)$'
    SECONDS_IN_MINUTE = 60
    SECONDS_IN_HOUR = 3600

    input_string = input_string.replace(" ", "").replace("(", "").replace(")", "")

    if input_string == "-":
        return 0

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
        return 1

    r = re.compile(TIME_REGEX)
    minutes = int(re.sub(r, r'\1', input_string))
    seconds = int(re.sub(r, r'\2', input_string))
    
    output = ((minutes * SECONDS_IN_MINUTE) + seconds)

    return output


#dirname = os.path.dirname(__file__)
#filename = os.path.join(dirname, 'relative/path/to/file/you/want')

# Iterate over all files in "/Albums"
for d in os.listdir("Albums"):
    
    if True: #"Ummagumma" in d:
        path = ("Albums/" + str(d))

        has_tracks = False
        has_title = False

        artist_name_string = artist_genre_string = language_string = ""
        album_name_string = album_len_string = date_string = rating_string = ""

        artist_header_string = output_string = ""
        formatted_array = []

        #ALBUM_REGEX = '^[[](.*?)[]](.*?).html$'
        ALBUM_REGEX = '^[[](.*?)(_[[].*?[]])[]](.*?).html$'
        r = re.compile(ALBUM_REGEX)
        album_name_string = re.sub(r, r'\3', d).replace("_", " ").replace("&", "and")
        artist_name_string = re.sub(r, r'\1', d)
        language_string = re.sub(r, r'\2', d).replace("_[", "").replace("]", "")

        output_path = "Data/" + artist_name_string + ".xml"

        artist_name_string = artist_name_string.replace("_", " ")

        with open(path, 'r') as input_file:
            line_num = 0
            for input_line in input_file:

                if line_num == ARTIST_LINE:
                    ARTIST_REGEX = '^.*?[0-9]["]>(.*?)<[/]a>.*?[;]["]>(.*?)<[/]h2>.*?$'
                    r = re.compile(ARTIST_REGEX)

                    artist_genre_string = re.sub(r, r'\2', input_line)

                elif line_num == DATE_LINE:

                    # REGEX-out the date
                    DATE_REGEX = '(.*?in )([0-9]*?)(<.*)'
                    r = re.compile(DATE_REGEX)
                    date_string = re.sub(r, r'\2', input_line)

                    #print("Date: " + date_string) # DEBUG

                elif line_num == RATING_LINE:

                    # REGEX-out the rating
                    RATING_REGEX = '^(.*?)([0-9].[0-9][0-9])([0-9]*?[)][;])$'
                    r = re.compile(RATING_REGEX)
                    rating_string = re.sub(r, r'\2', input_line)

                    #print("Rating: " + rating_string) # DEBUG

                elif line_num == LISTING_LINE:

                    # REGEX-out the album duration
                    ALBUM_LENGTH_REGEX = '^.*?[T|t]otal [T|t]ime[:]? (.*?)<.*?$'
                    r = re.compile(ALBUM_LENGTH_REGEX)
                    album_len_string = re.sub(r, r'\1', input_line)
                    album_len_string = str(to_seconds(album_len_string))

                    # REGEX-out the track listing
                    LISTING_REGEX = '(.*?">)(.*?)([T|t]oa?ta?l [T|t]ime.*?)$'   # Check for "Toatl Time" (sic)
                    r = re.compile(LISTING_REGEX)
                    listing_string = re.sub(r, r'\2', input_line).replace("<br>", "\n")[0:-2]

                    listing_array = listing_string.splitlines()

                    # MAGIC REGEX CONSTANTS
                    FULL_TRACK_REGEX = '^([0-9]*?[.] )(.*?)( [(][0-9]*?:[0-9]*?[)])( [:]| [*]|.)?$'
                    SUB_TRACK_REGEX = '([-] (.*?[.] |.*?[)] )?)(.*?)( [(][0-9]*?:[0-9]*?[)])?$'

                    # Parse each song listing
                    for i in listing_array:
                        #print(i) # DEBUG, Print listings line by line

                        # [Index, Length, Track Components]
                        if (re.match(FULL_TRACK_REGEX, i)): # Match whole tracks
                            r = re.compile(FULL_TRACK_REGEX)                                 
                            formatted_array.append([r.sub( r'\1', i).replace(". ",""), 
                                                     r.sub(r'\3', i).replace(" (","").replace(")",""), 
                                                     r.sub(r'\2', i).replace("&", "and").replace(". ",", "), #[BUG] Tagger eats periods
                                                     "Native"])

                        elif (re.match(SUB_TRACK_REGEX, i)): # Match sub-tracks
                            r = re.compile(SUB_TRACK_REGEX)                  
                            formatted_array.append([r.sub(r'\1', i).replace("- ","").replace(". ","").replace(")",""), 
                                                     r.sub(r'-', i), 
                                                     r.sub(r'\3', i).replace("&", "and").replace(". ",", "), #[BUG] Tagger eats periods
                                                     "Native"])
                    
                    for i in formatted_array:
                        if language_string != "en":
                            i[3] = i[2]
                            translated = GoogleTranslator(source='it', target='en').translate(i[2])
                            i[2] = translated

                    # For each song title, tokenize
                    for i in formatted_array:
                        lemmatizer = WordNetLemmatizer()
                        tokenized = sent_tokenize(i[2])
                        tagged = []

                        # For each tokenized song title, POS tag them
                        for j in tokenized:
                            wordsList = nltk.word_tokenize(j)
                            tagged = nltk.pos_tag(wordsList)

                            # For each word, add the lemma
                            k_iter = 0
                            for k in tagged:
                                # [Word, POS, Lemma]
                                
                                tagged[k_iter] = [k[0], k[1], lemmatizer.lemmatize(k[0].lower())]
                                k_iter += 1

                        i[2] = tagged 
                        
                        #print(i) # DEBUG

                    # Correct listings that reset index after side change
                    last = -1
                    for i in range(0, len(formatted_array)):
                        formatted_array[i][0].replace(" ", "")
                        
                        if formatted_array[i][0].isdigit():
                            #print ("Last: " + str(last) + " Current: " + str(formatted_array[i][0])) # DEBUG

                            if int(formatted_array[i][0]) <= last:
                                formatted_array[i][0] = str(last + 1)

                            last = int(formatted_array[i][0])

                # [BUG] artist_genre_string has a \n char appended to it
                if not os.path.exists(output_path):
                    artist_header_string = ("<artist name=\"" + artist_name_string 
                    + "\" genre=\"" + artist_genre_string[0:-1] 
                    + "\" lang=\"" + language_string + "\">\n")

                xml_string = album_xml = tracks_xml = ""

                # [BUG] For some reason, date_sting and rating_string have \n chars appended to them
                album_xml = (("\t<al name =\"" + album_name_string + "\" date=\"" + date_string[0:-1] + "\">\n") 
                            + ("\t\t<length>" + album_len_string + "</length>\n")
                            + ("\t\t<rating>" + rating_string[0:-1] + "</rating>\n"))
                

                for i in formatted_array:

                    track_len_seconds = to_seconds(i[1])
                        
                    tracks_xml += (("\t\t<tr index=\"" + str(i[0]) + "\">\n") 
                                  + ("\t\t\t<length>" + str(track_len_seconds) + "</length>\n"))
                        
                    if language_string != "en": # Has translation
                        tracks_xml += "\t\t\t<trans>" + i[3] + "</trans>\n"

                    for j in i[2]:
                        if j[1] != "":
                            if (len(j[1]) == 1) and (j[1] in string.punctuation): 
                                tracks_xml += "\t\t\t<punc pos=\"" + j[1] + "\" lemma=\"" + j[2] + "\">" + j[0] + "</punc>\n"
                            else:
                                tracks_xml += "\t\t\t<w pos=\"" + j[1] + "\" lemma=\"" + j[2] + "\">" + j[0] + "</w>\n"
                        
                    tracks_xml += "\t\t</tr>\n" 

                xml_string = album_xml + tracks_xml + "\t</al>\n"

                line_num += 1

        # Decide if the header should be included
        if not os.path.exists(output_path):
            output_string = artist_header_string + xml_string
        else:
            output_string = xml_string

        should_write = True

        # Output to file
        if should_write:
            output_file = open(output_path, "a")
            output_file.write(output_string)
            output_file.close
        else:
            print(output_string)

if should_write:
    APPEND_CLOSING_TAG = "</artist>\n"

    for d in os.listdir("Data"):
        file_path = "Data/" + d

        output_file = open(file_path, "a")
        output_file.write(APPEND_CLOSING_TAG)
        output_file.close
