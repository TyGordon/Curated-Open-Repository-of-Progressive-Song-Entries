import re

output_str = ""
output_file = open("corpus_curl.ps1", 'w', encoding="utf8")
band_name = "BAND_NAME"

with open("README.md", encoding="utf8") as input_file:
    for input_line in input_file:

        # Line is an album URL
        if re.match('(\+ )(\[.*?\])(\(.*?\))', input_line):

            # Divide into groups (+ ) (album_name) (//https/url)
            r = re.compile(r'(\+ )(\[.*?\])(\(.*?\))')

            # Make the command string and write it
            curl_line = "curl.exe " + re.sub(r, r'\3', input_line)[1:-2] + " | Select -First 562 | Select -Last 112 | Set-Content -LiteralPath " + "\"Albums/" + band_name + re.sub(r, r'\2', input_line)[1:-2].replace(" ", "_") + ".html\""
            output_file.write(curl_line + "\n")

        # Line is a band name
        elif re.match('^(.*?)( \([0-9]*?\))', input_line):

            # Divide into groups (band_name) (optional translation) (number of albums)
            r = re.compile(r'^(.*?)( \(.*?\))?( \([0-9]*?\))$')

            # Find the band name and format it
            band_name = "[" + re.sub(r, r'\1', input_line)[0:-1].replace(" ", "_") + "]"

output_file.close