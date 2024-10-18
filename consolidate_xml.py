import os

OUTPUT_PATH = "full_corpus.xml"

output_file = open(OUTPUT_PATH, "a")
            
output_file.write("<corpus>\n")

# Iterate over all files in "/Data"
for d in os.listdir("Data"):
    path = ("Data/" + str(d))

    with open(path, 'r') as input_file:
        for input_line in input_file:
            output_file.write(input_line)
    
output_file.write("</corpus>")

output_file.close