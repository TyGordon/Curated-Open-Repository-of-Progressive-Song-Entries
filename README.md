# Curated Open Repository of Progressive Song Entries

This document covers many components of the CORPSE project including:
+ Which bands and albums to use
+ How to tag the words

## ARTISTS TO INCLUDE:

### The "Big Seven"

Pink Floyd
+ [The Piper at the Gates of Dawn](https://www.progarchives.com/album.asp?id=1433)
+ [A Saucerful of Secrets](https://www.progarchives.com/album.asp?id=1434)
+ [More](https://www.progarchives.com/album.asp?id=1435)
+ [Ummagumma](https://www.progarchives.com/album.asp?id=1436)
+ [Atom Heart Mother](https://www.progarchives.com/album.asp?id=1437)
+ [Meddle](https://www.progarchives.com/album.asp?id=1438)
+ [Obscured by Clouds](https://www.progarchives.com/album.asp?id=1439)
+ [The Dark Side of the Moon](https://www.progarchives.com/album.asp?id=1440)
+ [Wish You Were Here](https://www.progarchives.com/album.asp?id=1441)
+ [Animals](https://www.progarchives.com/album.asp?id=1442)
+ [The Wall](https://www.progarchives.com/album.asp?id=1443)
+ [The Final Cut](https://www.progarchives.com/album.asp?id=1444)

Genesis\
Yes\
Rush\
King Crimson\
Jethro Tull\
Emerson Lake and Palmer

### Secondary Bands

Gentle Giant\
Van Der Graaf Generator\
Camel\
Alan Parsons Project\
Renaissance\
Eloy\
Focus\
Wishbone Ash\
Curved Air\
Hawkwind\
Nektar\
Triumvirate\
Spin\
Kansas\
Styx?\
UK

### Solo Artists

Frank Zappa\
Steve Hackett\
Peter Gabriel\
Anthony Philips\
Chris Squire\
Rick Wakeman\
Peter Hammill\
Mike Oldfield\
Robert Wyatt

### Canterbury Scene

Caravan\
Soft Machine\
Hatfield and the North\
National Health\
Matching Mole\
Gryphon\
Egg\
Khan\
Gong\
Magma - May exclude

### Fusion Bands

Mahavishnu Orchestra\
Return to Forever\
Brand X\
Tilt

### Krautrock 

Can\
Neu!

### Rock Progressivo Italiano (RPI)

Premiata Forneria Marconi\
Banco Del Mutuo Soccorso\
Le Orme\
Area\
Quella Vecchia Locanda\
Museo Rosenbach\
Il Balletto Di Bronzo\
Il Paesi Di Ballochi\
L'Uovo Di Columbo\
Biglietto Per L'Inferno\
New Trolls\
Maxophone\
Alphataurus\
Osana\
Picchio Dal Pozzo\
Semiramis\
Celeste\
Metamorphosi\
Reale Academia Di Musica\
Apoteosi\
Campo Di Marte\
Murple

### International

Crucis\
Fusioon\
Avtograf\
East


## TRACK TAGS
    index
        - The total index of the track in the album. Do not restart count when the side changes.
    length
        - Duration of the track.
    count
        - Word count of the track.
    type
        - stantard
        - main-track
        - part-track
        - compound-track


    has-pun="true"
    made-up="true"
    poorly-formed="true"
    non-semantic="true"
    not-english="true"

    imprecise-translation="true"
    title-track="true"
    hidden-track="true"
    single="true"


    

## WORD TAGS
    pos
        - Part of Speech of the word (using an auto-tagger).
    lemma
        - The lemmatized form of the word (ie. Dogs, doggies, dog, dawg -> lemma="dog").
    



## Manual Tagging Procedure

Before tagging, wget the page, translate (if applicable), pass through track_listing_scraper.py, then tag as follows:

1. Correct glaring mistakes, determine style, check if title-track and proper-noun 
2. Do manual POS tagging (Godspeed)
3. Check if part-track, sub-track, hidden-track
4. Do the other tags
5. Profit?

## TITLE STYLES:

    nounless-word
        - "If"
    nounless-phrase
        - "Why Not"
    single-word
        - "Echoes", "Alucard"
    dual-word
        - "Funny Ways", "Black Napkins"
    single-phrase
        - "Thick as a Brick", "A Plague of Lighthouse Keepers"
    full-sentence
        - "Bobby Brown Goes Down"
    compound-phrase
        - "Several Species of Small Furry Animals Gathered Together in a Cave and Grooving with a Pict"
    list-phrase
        - "The House, The Street, The Room"
    single-acronym
        - "RDNZL"
    medley
        - "Nimrodel / The Procession / The White Rider"
    other
        - "P-Qb4"


## TAG TYPES:

    REFERENCES:
        > contemporary-reference
            "Punky's Whips"
        > classics-reference
            "The Fountain of Salmacis"
    NATURE:
        * > humorous
            - "The Adventures of Greggory Peccory"   
        > has-pun
            - "Bossa Nochance"
        > made-up
            - "Arubaluba", "Zoot Allures"
        > eclectic
            - "Lobster in Cleavage Probe"
        > poorly-formed
            - "H to He who am the Only One"
        > non-semantic
            - "RDNZL"
    GRAMMAR:
        > leading-prep
            - "In the Wake of Posideon"
        > leading-part
            - "Burning Bridges"
        > imperaive
            - "Speak to Me"
        > question
            - "Isn't It Quiet and Cold?"
        > quote
            - "Ed Ora Io Domando Tempo Al Tempo Ed Egli Mi Risponde ... Non Ne Ho!"
        > parenthetical
            - "Let's Eat (Real Soon)"
        > proper-noun
            - "Darwin!"
        > different-language
            - "Io Sono Nato Libero"
        > non-precise
            - "La Conquista Della Posizione Eretta" > "The Conquest of the Upright Position"
    META:
        > title-track
            - "In the Land of Grey and Pink"
        > compound-track
            - "The Three Fates"
        > part-track
            - "Another Brick in the Wall, Part 1"
        > sub-track
            - "a. Clotho (Royal Festival Hall organ)"
        ** > overlaps
            - "Harlequin"
        ** > ends-cold
            - "I Want You (She's So Heavy)"
        > hidden-track
            - "In a Glass House"
        * > single
            - "Sylvia"
    MISC:
        > suggestive
            - "Friendly Little Finger"
        > crass
            - "Going Up to People and Tinkling"
        > explicit
            - "Broken Hearts are for Assholes"



## MISC CODE
    wget -c https://www.progarchives.com/album.asp?id=1433 -O [PINK_FLOYD]_piper_at_the_gates_of_dawn.html
    wget -c https://www.progarchives.com/album.asp?id=1434 -O [PINK_FLOYD]_a_saucerful_of_secrets.html
    wget -c https://www.progarchives.com/album.asp?id=1435 -O [PINK_FLOYD]_more.html
    wget -c https://www.progarchives.com/album.asp?id=1436 -O [PINK_FLOYD]_ummagumma.html
    wget -c https://www.progarchives.com/album.asp?id=1437 -O [PINK_FLOYD]_atom_heart_mother.html
    wget -c https://www.progarchives.com/album.asp?id=1438 -O [PINK_FLOYD]_meddle.html
    wget -c https://www.progarchives.com/album.asp?id=1439 -O [PINK_FLOYD]_obscured_by_clouds.html
    wget -c https://www.progarchives.com/album.asp?id=1440 -O [PINK_FLOYD]_the_dark_side_of_the_moon.html
    wget -c https://www.progarchives.com/album.asp?id=1441 -O [PINK_FLOYD]_wish_you_were_here.html
    wget -c https://www.progarchives.com/album.asp?id=1442 -O [PINK_FLOYD]_animals.html
    wget -c https://www.progarchives.com/album.asp?id=1443 -O [PINK_FLOYD]_the_wall.html
    wget -c https://www.progarchives.com/album.asp?id=1444 -O [PINK_FLOYD]_the_final_cut.html

https://www.geeksforgeeks.org/part-speech-tagging-stop-words-using-nltk-python/
https://www.geeksforgeeks.org/python-lemmatization-with-nltk/#

WARNING: The script nltk.exe is installed in 'C:\Users\tygor\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.