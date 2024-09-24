import re

path1 = "Albums/album_piper_at_the_gates_of_dawn.html"
path2 = "Albums/album_foxtrot.html"
input_file = open(path2, "r")

has_tracks = False
has_title = False

for i in range(0, 400):
    input_line = input_file.readline()

    if has_title:
        pass

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

            if i[0] == "-":
                r = re.compile(r'(-)( .*? )(.*?)$')
                #data_array[j].append(r.sub(r'\1 ', i))
                #data_array[j].append("-")
                data_array[j].append("-")
                data_array[j].append("-:-")
                data_array[j].append(r.sub(r'\3', i))
            else:
                r = re.compile(r'([0-9]+.)(.*?)(\([^)]*\))')
                data_array[j].append(r.sub(r'\1 ', i))
                data_array[j].append(r.sub(r'\3', i))
                data_array[j].append(r.sub(r'\2', i))

            #print(r.sub(r'\1 |\3|\2', i))
            
            

            data_array[j][0] = data_array[j][0].replace(" ", "")
            data_array[j][0] = re.sub(r'\.$', '', data_array[j][0])
            data_array[j][1] = data_array[j][1].replace("(", "").replace(")", "").replace(" ", "")

            data_array[j][2] = re.sub(r'^.\s', '', data_array[j][2])
            data_array[j][2] = re.sub(r' $', '', data_array[j][2])
            data_array[j][2] = data_array[j][2].split(" ")

            print(data_array[j]) # DEBUG

            j += 1

        xml_string = ""

        for i in data_array:
            xml_string += ("<tr index=\"" + str(i[0]) + "\" length=\"" + str(i[1]) + "\" style=\"\">\n")
            
            for j in i[2]:
                xml_string += "\t<w pos=\"\" lemma=\"" + str(j).lower() + "\">" + str(j) + "</w>\n"
            
            xml_string += "</tr>\n"


        #print(xml_string) # DEBUG

    if (re.search("Songs / Tracks Listing", input_line)):
        has_tracks = True

    if (re.search("og:title", input_line)):
        has_title = True