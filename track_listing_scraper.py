import re
import os
import nltk

from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

DATE_LINE = 55 - 1
LISTING_LINE = 57 - 1


#dirname = os.path.dirname(__file__)
#filename = os.path.join(dirname, 'relative/path/to/file/you/want')

# Iterate over all files in "/Albums"
for i in os.listdir("Albums"):
    
    if "[Hatfield_and_the_North]Hatfield_and_the_North" in i:
        path = ("Albums/" + str(i))

        has_tracks = False
        has_title = False

        artist_string = date_string = output_string = listing_string = ""

        with open(path, 'r') as input_file:
            line_num = 0
            for input_line in input_file:

                if has_title:
                    has_title = False

                    date_string = input_line[input_line.index(" (") - (len(" (") - 4):]
                    date_string = date_string[:date_string.index(")")]

                    # Cull everything after the song title
                    input_line = input_line[:input_line.index(" (") - (len(" (") - 2)]

                    artist_string = input_line[:input_line.index(" - ") - (len(" - ") - 3)]

                    artist_string = artist_string[artist_string.index("content=\"") - (len("content=\"") - 18):]

                    # Cull everything before the song title
                    input_line = input_line[input_line.index(" - ") - (len(" - ") - 6):]

                    #print(artist_string + " | " + date_string + " | " + input_line)
                    
                    output_string = "<album name=\"" + input_line + "\" date=\"" + date_string + "\">\n"

                if has_tracks:
                    has_tracks = False

                    # Cull everything after "Total Time"
                    input_line = input_line[:input_line.index("Total Time") - (len("Total Time") - 2)]
                
                    # Cull all <br> and replace with \n
                    input_line = input_line.replace("<br>", "\n")

                    # Cull everything before track 1.
                    input_line = "1." + input_line[input_line.index("1.") + len("1."):]

                    # Format to xml
                    line_array = input_line.splitlines()
                    data_array = []


                    # Split the data into the following format:
                    #   [track number, time, [array, of, words]]
                    j = 0
                    for i in line_array:

                        data_array.append([])

                        i = re.sub(r':$',"", i)

                        if i != "" and i[0]== "-":
                            r = re.compile(r'(-)(.*?)(.*?)$')
                            #data_array[j].append(r.sub(r'\1 ', i))
                            #data_array[j].append("-")
                            data_array[j].append("-")
                            data_array[j].append("-")
                            data_array[j].append(r.sub(r'\3', i))
                        else:
                            r = re.compile(r'([0-9]+.)(.*?)(\([^)]*\))$')
                            data_array[j].append(r.sub(r'\1 ', i))
                            data_array[j].append(r.sub(r'\3', i))
                            data_array[j].append(r.sub(r'\2', i))

                        #print(r.sub(r'\1 |\3|\2', i))
                        

                        data_array[j][0] = data_array[j][0].replace(" ", "")
                        data_array[j][0] = re.sub(r'\.$', '', data_array[j][0])
                        data_array[j][1] = data_array[j][1].replace("(", "").replace(")", "").replace(" ", "")

                        data_array[j][2] = re.sub(r'^.\s', '', data_array[j][2])
                        data_array[j][2] = re.sub(r' $', '', data_array[j][2])
                        #data_array[j][2] = data_array[j][2].split(" ")

                        tokenized = sent_tokenize(data_array[j][2])
                        #data_array[j][2] = ["0"]
                        del data_array[j][-1]
                        #print(data_array[j])

                        lemmatizer = WordNetLemmatizer()

                        for i in tokenized:
                        
                            #  Using a Tagger. Which is part-of-speech 
                            # tagger or POS-tagger. 
                            tagged = nltk.pos_tag(nltk.word_tokenize(i))

                            for w in tagged:
                                w = ([w[0], w[1], lemmatizer.lemmatize(w[0].lower())])
                                #print(lemmatizer.lemmatize(w[0].lower()))
                                    #print(lemmatizer.lemmatize(w[0]))
                                print(w)

                            #data_array[j].append(tagged + tuple(lemmatizer.lemmatize("fishes")))

                            #print(tagged)   


                        #print(data_array[j]) # DEBUG

                        j += 1

                    xml_string = ""

                    for i in data_array:
                        
                        xml_string += ("\t<tr index=\"" + str(i[0]) + "\" length=\"" + str(i[1]) + "\" style=\"\">\n")
                            
                        for j in i[2]:
                            if j != "":
                                xml_string += "\t\t<w pos=\"\" lemma=\"" + str(j).lower() + "\">" + str(j) + "</w>\n"
                            
                        xml_string += "\t</tr>\n"

                    #print(xml_string) # DEBUG
                    output_string = output_string + xml_string + "</album>\n"
                    #print (output_string)
                

                if line_num == DATE_LINE:

                    # REGEX-out the date
                    r = re.compile(r'(.*?in )([0-9]*?)(<.*)')
                    date_string = re.sub(r, r'\2', input_line)

                    print(date_string)

                elif line_num == LISTING_LINE:

                    # REGEX-out the track listing
                    r = re.compile(r'(.*?">)(.*?)(Total Time.*?)$')
                    listing_string = re.sub(r, r'\2', input_line).replace("<br>", "\n")[0:-2]

                    listing_array = listing_string.splitlines()
                    formatted_array = []

                    # MAGIC REGEX CONSTANTS
                    FULL_TRACK_REGEX = '^([0-9]*?[.] )(.*?)( [(][0-9]*?:[0-9]*?[)])( [:]| [*])?$'
                    SUB_TRACK_REGEX = '([-] (.*?[.] |.*?[)] )?)(.*?)( [(][0-9]*?:[0-9]*?[)])?$'

                    # Parse each song listing
                    for i in listing_array:
                        if (re.match(FULL_TRACK_REGEX, i)): # Match whole tracks
                            r = re.compile(FULL_TRACK_REGEX)                                 
                            formatted_array.append([r.sub( r'\1', i).replace(". ",""), 
                                                     r.sub(r'\3', i).replace(" (","").replace(")",""), 
                                                     r.sub(r'\2', i)])

                        elif (re.match(SUB_TRACK_REGEX, i)): # Match sub-tracks
                            r = re.compile(SUB_TRACK_REGEX)                  
                            formatted_array.append([r.sub(r'\1', i).replace("- ","").replace(".","").replace(")",""), 
                                                     r.sub(r'-', i), 
                                                     r.sub(r'\3', i)])

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
                                tagged[k_iter] = [k[0], k[1], lemmatizer.lemmatize(k[0].lower())]
                                k_iter += 1

                        i[2] = tagged 

                    for i in formatted_array:
                        print(i)

                    #print(listing_array)



                if (re.search("Songs / Tracks Listing", input_line)):
                    has_tracks = False

                if (re.search("og:type", input_line)):
                    has_title = False

                line_num += 1


        output_path = "Data/" + artist_string + ".xml"

        # Output to file
        output_file = open(output_path, "a")
        output_file.write(output_string)
        output_file.close