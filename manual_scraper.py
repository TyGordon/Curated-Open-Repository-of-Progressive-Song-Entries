import re
import os
import nltk
import string

from deep_translator import GoogleTranslator
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet



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


output_str = ""
output_file = open("manual_albums.txt", 'w', encoding="utf8")



with open("problematic_albums.txt", encoding="utf8") as input_file:
    for input_line in input_file:

        FULL_TRACK_REGEX = '^([0-9]*?[.] )(.*?)( [(][0-9]*?:[0-9]*?[)])( [:]| [*]|.)?$'
        SUB_TRACK_REGEX = '([-] (.*?[.] |.*?[)] )?)(.*?)( [(][0-9]*?:[0-9]*?[)])?$'

        if re.match(FULL_TRACK_REGEX, input_line):
            r = re.compile(FULL_TRACK_REGEX)

            lemmatizer = WordNetLemmatizer()

            
            tokenized = sent_tokenize(re.sub(r, r'\2', input_line))
            output_file.write(str(re.sub(r, r'\1', input_line)))

            # For each tokenized song title, POS tag them
            for j in tokenized:
                output_file.write(j + " ")

                wordsList = nltk.word_tokenize(j)
                tagged = nltk.pos_tag(wordsList)

                # For each word, add the lemma
                k_iter = 0
                for k in tagged:
                    # [Word, POS, Lemma]
                    output_file.write("\n")

                    output_file.write(k[1] + " ")
                    
                    output_file.write(lemmatizer.lemmatize(k[0].lower()) + " ")

                    k_iter += 1

            output_file.write(str(to_seconds(re.sub(r, r'\3', input_line))))
            output_file.write("\n\n")

output_file.close
