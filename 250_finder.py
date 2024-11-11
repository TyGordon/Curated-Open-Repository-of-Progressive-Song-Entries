import re

output_file = open("top-250.txt", 'w')
artists = []

# Open the top-250.html file and extract the artist names
with open("top-250.html") as input_file:
    for input_line in input_file:

        # Line is an artist
        REGEX = r'^(.*?)<[/]a>(.*?)">(.*?)<[/]a><[/]td>$'

        if re.match(REGEX, input_line):

            # Divide into groups
            r = re.compile(REGEX)

            band_name = re.sub(r, r'\3', input_line)

            if not band_name in artists:
                artists.append(band_name)
            
    for artist in artists:
        output_file.write(artist)
            
output_file.close