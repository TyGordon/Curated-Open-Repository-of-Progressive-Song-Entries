# Curated Open Repository of Progressive Song Entries (CORPSE)

### This document covers many components of the CORPSE project including:
1. Information about the project, what is included and how to compile it
2. How to use the CORPSE Explorer
3. Which bands and albums are included (Roughly 415 Albums)
4. How the entries are tagged

#### CORPSE Author
    Ty Gordon

#### Most Recent Update
    12/10/2024

#### Number of Artists Included:
    101

#### Number of Albums Included:
    422

#### Number of Tracks Included:
    3,741

#### Number of Words Included:
    11,480


### Table of Contents
1. [Overview](#overview)
2. [Usage Guide](#usage-guide)
3. [Artist List](#artist-list)
    - [The Big Seven](#the-big-seven)
    - [Secondary Bands](#secondary-bands)
    - [Solo Artists](#solo-artists)
    - [Canturbury Scene](#canterbury-scene)
    - [Fusion](#fusion)
    - [Krautrock](#krautrock)
    - [RPI](#rock-progressivo-italiano-rpi)
    - [International](#international)
    - [Artists to Include](#artists-to-include)
4. [Tagging](#tagging)

## OVERVIEW

### What Is This?
    This is the Curated Open Repository of Progressive Song Entries (CORPSE), which is a project developed for the
    University of Kentucky Corpus Linguistics course LIN-510. At its core, CORPSE is a collection of XML 
    formatted song titles sourced from progarchives.com within the years 1966 to 1984. It comes with an explorer 
    utility, which amounts to a Graphical User Interface (GUI) designed to allow any user the ability to search 
    the database in a simple manner (unlike CQP, RegEx, etc). 

    Progressive Rock is a term used to describe a genre of music that was prevalent in the late 60s, to the early 
    80s. It is usually described as a more complicated and eclectic form of popular music with many influences 
    from genres such as Jazz, Classical, Blues, Folk Baroque, Soul, R&B, Electronic, Experimental, and Rock. This 
    corpus only includes the "classic" era of Progressive Rock, and deliberatly excludes newer forms passed 1984 
    such as Progressive Metal, Neo-Prog, etc. Progressive Rock itself can be described with various sub-genres. 
    The following links may be helpful for understanding the genre.

[Prog Archives Home](https://www.progarchives.com/)

[What is Progressive Rock?](http://www.progarchives.com/Progressive-rock.asp#definition)

[Top 100 Prog Albums 1966-1984](https://www.progarchives.com/top-prog-albums.asp?ssubgenres=&salbumtypes=1&syears=1984&syears=1983&syears=1982&syears=1981&syears=1980&syears=1979&syears=1978&syears=1977&syears=1976&syears=1975&syears=1974&syears=1973&syears=1972&syears=1971&syears=1970&syears=1969&syears=1968&syears=1967&syears=1966&scountries=&sminratings=0&smaxratings=0&sminavgratings=0&smaxresults=100&x=55&y=7#list)

### Purpose
    The corpus was built to answer questions about the stylistic conventions of progressive rock titles. The 
    contents of the CORPSE corpus are far too limited to make any generalizations about english or how english is 
    generally used. It is, however, adequete for answering questions about progressive rock song titles since it 
    encompasses a significant portion of all progressive rock titles from the classic era. The querying systems 
    makes use of abundant meta-data to compensate for the lack of large sums of data, and accurate tagging. 
    Questions such as "Do prog songs generally get shorter over time" or "Do long prog songs have shorter titles" 
    are the kinds of questions that this corpus aspires to help answer.

### What's Included
    The CORPSE Corpus consists of two main tools and the data that makes up the corpus (both raw html and 
    formatted xml files). The tools CORPSE Maker and CORPSE Explorer are made up of the following subcomponents:

    CORPSE MAKER
    1. README.md (This file) - To be used as the source of the URLs.
    2. curl_maker.py - A python program that builds a series of curl commands to fetch web data.
    3. corpus_curl.ps1 - The powershell script output from curl_maker.py. When run it executes the curl commands. 
    4. track_listing_scraper.py - A python program that takes the HTML pages from curl and converts it to 
        formatted XML files to be used in the corpus.
    5. /Albums - A folder of all of the HTML pages used for the corpus.
    6. /Data - A folder of each album represented in an XML format.
    7. /Images - A folder with some images used for the GUI and its development.
    8. full_corpus.xml - An XML file with all of the data. This is used by the CORPSE Explorer.

    CORPSE EXPLORER
    1. corpus_explorer.py - A pyqt application that performs searches over the XML data.
    2. corpus_gui.ui - A QT ui file used for render the explorer GUI.
    3. reasources.qrc- a qrc file used by QT to load images, etc.

    OTHER
    1. 250_finder.py - A python program that finds all of the artists from the list of the top 250 albums from 
        prog archives.
    2. top-250.html and top-250.txt - The input and output of 250_finder.py.
    3. manual_scraper.py - A script to convert manually typed albums into lemmas, POS, etc
    4. manual_albums.txt - The output of the manual scraper
    5. problematic_albums.txt - A list of problematic albums

### What's Needed
    These resources are nessessary for re-assembling the corpus:
    - Microsoft Windows 10/11 OS (linux/mac are untested)
    - Curl for Windows (for curl_maker.py to work)
    - Python, pip (for .py programs)
    - NTLK (use pip) (used for POS tagging)
    - deep-translator (use pip) (used for translation)
    - QT and pyqt (use pip) (used for GUI)
    - Pyinstaller for making .exe
        ==> Use this command: 
        pyinstaller.exe --onefile --name="CORPSE Explorer" --add-data="full_corpus.xml:." --add-data="resources.qrc:." --add-data="corpus_gui.ui:." --add-data="Images:Images" --icon="Images/uk_icon.ico" corpus_explorer.py

    Otherwise, just running the CORPSE_Explorer.exe should work with no added software.
        (full_corpus.xml, reasource.qrc, and corpus_gui.ui need to be in the same directory to work)

### Limitations
    Known Bugs:
    - Track names with a period followed by a space do not play nicely with the POS tagger: the tagger tends to 
    eat them.
    - XML does not like the '&' character, so all instances were replaced with "and"
    - CURL does not like some characters such as '/', which had to be replaced with '-'
    - Many special characters (such as those of the cyrillic variety, or those with uncommon accent markers) are  
    not compatible with the character encoding used. They are either left unchanged, or hand-corrected.
    - The format of the souced HTML pages can change, and did in-fact change upon the second corpus compilation on
    Nov 15th. The spacing in the source code for HTML elements may change over time as was the case here. New 
    features could also have been added to the website, which could change what lines are needed for data extraction.
    - Albums with multiple sub-tracks of the same index may show the wrong track since they share indexes.
    - Upon compilation, the corpus may have some ratings and/or indexes set to a string (since the data is 
    inconsistent). This results in a crash when using the explorer. These have to be manually corrected for now. 
    - Some tracks may have an asterisk to indicate additional information. Sometimes these tracks get filtered 
    out such as "Incantations Part 3*" from Mike Oldfield on the album "Incantations".
    - QT spews font errors for some reason. This does not impact the functionality of the program
    
    Design Flaws:
    - Many albums are excluded for the following reasons:
        > They do not fit within the time frame (1966-1984).
            Ex. "Invisible Touch" by Genesis
        > They are under a different name.
            Ex. Magma's "Tristan et Iseult" ("Wurdah Itah")
        > The album has a very poor relative rating AND is at the end of the group's "golden era".
          (This is done because many groups tended to switch genres away from Prog rock, so these
          albums are typically not representative of the genre this corpus encompasses)
            Ex. Jethro Tull's "Under Wraps"
        > The respective group is nieche or borderline prog and only gets one album, with the rest omitted.
            Ex. Return to Forever's albums that are not "Romantic Warrior"
        > The group was not discovered/known about at corpus compiling time.
    - Tracks from foreign groups may need to be translated by the auto-translator. This is prone to mistakes and 
    may influence the style of foreign titles (ie. romance languages adding a surplus of the word "of", etc).
    - Albums with more than 12 sub-tracks under one main track are not supported. a-l and i-xii are the only 
    sub-track alphabet index characters that are converted into a numeric index.
    - The automatic XML generation makes any sub-track listed with an index of "-" have no proper index. 
        THESE NEED TO BE FIXED MANUALLY.
    - Some album entries do not follow the common format and are problematic. Some examples are:
        Joe's Garage Act, I - Frank Zappa
            => Has no track times
        Roxy & Elsewhere - Frank Zappa
            => Misspelt "Total Time"
        Who's Next - The Who
            => No "Total Time"
        Private Parts and Pieces III - Anthony Philips
            => No period after numerals
    - Cyrillic characters do not work with the translation step currently, so entries from Aftograf are excluded
    - The "chain-search" feature

    Flaws With 3rd Party Utilities:
    - The lemmatizer used was either incorectly used or is generally bad. Many lemmas are wrong such as:
        was -> wa
        does -> doe
        has -> ha
       These are not corrected.
    - The POS tagger is also often wrong. Most song titles are capitalized, and are thus tagged as NNS.
    - The translator translates everything. This wasn't the original plan, but this is how it is.

    THE FOLLOWING ALBUMS ARE PROBLEMATIC AND NEED TO BE HAND-CORRECTED UPON CORPUS COMPILATION:
    (List Format: [Album Title] - [Artist], '\n' '\t' '\t' => [Notes on why the title is an issue])

    - Joe's Garage Act, I - Frank Zappa ✓
        => Tracks lack numbers
    - Roxy & Elsewhere - Frank Zappa ✓
        => Misspelt "Total Time"
    - Who's Next - The Who ✓
        => No "Total Time"
        => Track Times use a period, not a colon
    - Private Parts and Pieces III - Anthony Philips ✓
        => No period after numerals
    - More - Pink Floyd ✓
        => Unknown failure
    - Per Un Amico - Premiata Forneria Marconi ✓
        => Unknown failure
    - Magick Brother - Gong ✓
        => Side names may be the issue
    - Klaus Schultz - Moondawn ✓
        => Unkown failure
    - Jatekok - East ✓
        => Non-Latin characters, translation provided
    - Huseg - East ✓
        => Non-Latin characters, translation provided
    - Avtograf - 1 ✓
        => Cyrillic characters, translation provided
        => MANUALLY CHANGE DATE TO 1982 FOR ACCURACY
    - Avtograf - 2 ✓
        => No Prog archives entry. Use the youtube link
        => This album was released informally as a "magnito-album" <<Магнитоальбом>> with an imprecise  
        track-listing. The Youtube version will be used as the source for the data.
    - Magma
        => This group invented a con-lang in order to foil my corpus plans. The special characters do not play 
        nice with the scraping tools and thus may appear as unknown characters.

### Lessons Learned
    A lot had to be learned to make this project what it is since many unfimiliar tools were needed. Here is a 
    list of the skills gained and practiced during development:

    - Python Programming
        => Reading Files
        => Writing to Files
        => Using 3rd party libraries such as:
            NLTK
            Deep Translator
            Element Tree
            lxml
            Pyqt 6
    - QT 6
        => Designing a functional GUI
        => Implementing a GUI in QT
        => Connecting GUI elements to python functions
        => Using QT signals
    - Web Scraping
        => Navigating HTML code
        => Using Wget and Curl to fetch webpages
        => Using (lots of) RegEx to clean the html data
    - XML Formatting
        => Designing an XML database
        => Formatting input into XML tags
    - XML Querying
        => Building Xpath expressions
        => Using Xpath to find entries
        => Filtering by XML tags
    - Programming Practices
        => Implementing parallel processing
        => Building and querying databases
        => Documenting a project
        => Using markdown
        => Using version control (Git)
        => Using Gen AI resources to help implement a solution
        => Coming up with great names and acronyms
    - Corpus Creation
        => Designing a corpus
        => Metadata collection
        => Translation
        => Lemmatization 
        => PoS tagging
    - Corpus Investigation
        => Making informative queries
        => Using statistics to analyze patterns
        => Writing investigation reports
    

### Future Work
    This project is by no means complete. Several features and ideas are left incomplete, non-functional or 
    untouched. Even the functionality provided is inherently flawed, and could be reworked for a better product.
    Here are some features that were planned to be added if develpment were to continue:

    - Chain-Search
        ==> Almost implemented, but scrapped due to time and implementation difficulty. Would allow the user to 
        "chain" or "stack" queries whereby the results of one query would be stored as a "subset-corpus" and be 
        fed as the input for a subsequent query.
    - Multi-Word Search
        ==> Instead of, or alongside the "chained-search" feature, support for searching multiple consecutive 
        words would be a great feature to have.
    - Track-Type Tag
        ==> Some implementation (GUI). Would allow the user to sort by tracks that are sub-tracks or parts of a   
        larger track. Or lets them filter them out if undesired. These tags are not present in full_corpus.xml
    - Search by Last Word
        ==> Implement a way to search by the last index.
    - "Misc" Tags
        ==> Tag the titles for extra meta information such as "has-pun", "comedic", "explicit language", 
        "contains reference", "non-semantic phrase", etc.
    - Semantic Tagging
        ==> Add a semantic tagger to add these tags within the track scraper.
    - Semantic Trees
        ==> Add a system to store the titles as trees and visualize them in other windows.
    - N-Gram Search
        ==> Add a way to search N-Grams
    - Multiple tabs
        ==> Add multiple tabs within the application to allow the user to preserve old searchs and settings.
    - Visual Graphs
        ==> Allow the user to make graphs in a new window to visualize queries.
    - Concordance
        ==> Add a setting to visually line up the titles by a keyword.
    - Super Corpus
        ==> Crawl the entire Prog Archives website for all entries within established criteria and make a "Super 
        Corpus" with much more data to use.
    - Text Click
        ==> Allow the user to click a word in the explorer to see tagging info.
    - Album Covers
        ==> Allow the user to see covers associated with a selected album/track.
    - Query Optimizations
        ==> Optimize the search functionality to be faster.
    - GUI Overhaul
        ==> Make a more appealing/functional GUI.
    - Add/Remove Entries
        ==> Add more entries to the corpus, and remove problematic ones

### Generative Artificial Intelligence (Gen-AI) Usage Disclaimer
    It can be assumed that Gen-AI was not used to generate neither prose, nor code related to this assignment 
    with the following explicit exceptions in the file:

    ==> corpus_explorer.py
        Gen-AI tools (ChatGPT-4) were used for: 
            - The design of the search functionality (only for the layout of tag filtering statments)
            - Code and ideas for the loading bar and parallel processing (worker functions, etc)
            - Pyqt signals related to the functionality listed above
            - and the unmodified save_subset function (unused) for the umimplemented chain-search feature

    Precicely no input from Gen-AI sources was used for any other files associate with this project.

### Sub-Genres Included

+ Symphonic Prog
+ Eclectic Prog
+ Heavy Prog
+ Psychedelic/Space Rock
+ Progressive Electronic
+ Prog Folk
+ Jazz Rock/Fusion
+ Canterbury Scene
+ Rock Progressivo Italiano
+ Krautrock
+ Zeuhl
+ RIO/Avant-Prog
+ Crossover Prog
+ Proto-Prog
+ Neo-Prog
+ Prog Related


## USAGE GUIDE

### First Row

- **Search Bar Text Field**

    This is where you type the word to search for in the corpus. Multiple words are not supported.

- **Stats Button**

    This button changes the View Window to show word frequencies in a "Corpus Statistics" page.

- **Part of Speech (POS) Dropdown**

    This dropdown lets you select the POS tag to be searched that is assocciated with the word entered in the 
    Search Bar. The tagset used is the NLTK tagset, which is a modified Penn tagset.

### Second Row

- **Search Button**

    This button starts the search.

- **Clear Button**

    This button clears the Search Box and the View Window

- **Case Checkbox**

    This checkbox toggles Case-Sensitive searching. Checked means that the the search is Case-Sensitive

- **Lemma Search Checkbox**

    This checkbox toggles the Lemma Search functionality. Checked means that only lemmas are searched in the 
    corpus. You must put a lower-case lemma in the Search Bar to use this feature.

- **Word Index Checkbox**

    This checkbox toggles the Word Index Search. It tells the explorer to only return results that match the 
    Searched word at the specific number typed in the Word Index Text Field. Ex. In the sentence "The fox is 
    hungry," the word "fox" is at index 2, and the word "hungry" is at index 4.

- **Word Index Text Field**

    This text field is where you enter the index for the Word Index Search.

### Dates Tags

- **"All" Button**

    This button checks all date checkboxes

- **"None" Button**

    This button unchecks all date checkboxes

- **Date Checkboxes**

    These checkboxes allow you to search by the album release date.

### Artist Tags

- **Artist Name Search**

    The checkbox toggles the search using the text field to the right. This line is for searching by Artist name 
    (Not Case-Sensitive).

- **Artist Sub-Genre Search**

    The checkbox toggles the search using the dropdown to the right. This line is for searching by Sub-Genre (As 
    appears on Prog Archives).

- **Artist Language Search**

    The checkbox toggles the search using the dropdown to the right. This line is for searching by language. In 
    many cases the group may have a different native language than is listed within the corpus. The language 
    option indicates the primary language used for the album, even if it isn't the native language of the artist.

### Album Tags

- **Album Name Search**

    The checkbox toggles the search using the text field to the right. This line is for searching by Album name 
    (Not Case-Sensitive).

- **Album Rating Search**

    The checkbox toggles the search using the text field to the right. The operator dropdown allows searching 
    using the symbols ">", "=", "<" whereby the ">" returns results greater than the input, and the "<" returns 
    results less than the input. This line is for searching by Album rating (As appears on Prog Archives) in the 
    form "X.XX" where each "X" is a digit from 0-9. The scale used only goes from 1.00 to 5.00, and most results 
    lie in the 3.XX range or the 4.XX range.

- **Album Length Search**

    The checkbox toggles the search using the text field to the right. The operator dropdown allows searching 
    using the symbols ">", "=", "<" whereby the ">" returns results greater than the input, and the "<" returns 
    results less than the input. This line is for searching by Album length either in the form of seconds 
    (integer) or in the styles "MM:SS", or "H:MM:SS" where H is the number of hours, MM is the number of minutes 
    (2 digits), and SS is the number of seconds (2 digits).

### Track Tags

- **Track Index Search**

    The checkbox toggles the search using the text field to the right. The operator dropdown allows searching 
    using the symbols ">", "=", "<" whereby the ">" returns results greater than the input, and the "<" returns 
    results less than the input. This line is for searching by a numeric Track index (integer). Tracks originally 
    listed with positions "a-g" or "i-vii" are converted to numeric form automatically.

- **Track Length Search**

    The checkbox toggles the search using the text field to the right. The operator dropdown allows searching 
    using the symbols ">", "=", "<" whereby the ">" returns results greater than the input, and the "<" returns 
    results less than the input. This line is for searching by Track length either in the form of seconds 
    (integer) or in the style "MM:SS" where MM is the number of minutes (2 digits), and SS is the number of 
    seconds (2 digits).   

- **Word Count Search**

    The checkbox toggles the search using the text field to the right. The operator dropdown allows searching 
    using the symbols ">", "=", "<" whereby the ">" returns results greater than the input, and the "<" returns 
    results less than the input. This line is for searching by Track Word Count (integer). It tells the corpus to 
    only return tracks that have the amount of words that satisfies the input. Some special punctuation cases are 
    considered words (such as double-quotes).

- **Exclude Sub-Tracks**

    When checked, filters out all sub-tracks in the corpus. This can be usefull when looking for tracks that are  
    less than a given time, since sub-tracks have a length of zero and will show up, skewing results.

### View Window

Upon a normal search, the following information may appear:

- **"Hits"**

    Indicates how many results (tracks) were matched.

- **"Lemma Frequency"**

    Indicates the frequency that the lemma of the searched word appears. 

- **"Title Frequency"**

    Indicates the number of titles (hits) that contain the searched word.

- **Corpus Entry**

#### The entries should appear in this format:

    - = - Group Name - = -

    Track **Title** (Album Name)

    ==> *Original Text* If Translated
    

## ARTIST LIST

### The "Big Seven"

Pink Floyd [en] (12)
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

Genesis [en] (12)
+ [From Genesis to Revelation](https://www.progarchives.com/album.asp?id=6)
+ [Trespass](https://www.progarchives.com/album.asp?id=2448)
+ [Nursery Cryme](https://www.progarchives.com/album.asp?id=3)
+ [Foxtrot](https://www.progarchives.com/album.asp?id=2)
+ [Selling enland by the Pound](https://www.progarchives.com/album.asp?id=1510)
+ [The Lamb Lies Down on Broadway](https://www.progarchives.com/album.asp?id=1511)
+ [A Trick of the Tail](https://www.progarchives.com/album.asp?id=5)
+ [Wind & Wuthering](https://www.progarchives.com/album.asp?id=1512)
+ [...And Then There Were Three...](https://www.progarchives.com/album.asp?id=1515)
+ [Duke](https://www.progarchives.com/album.asp?id=1516)
+ [Abacab](https://www.progarchives.com/album.asp?id=1517)
+ [Genesis](https://www.progarchives.com/album.asp?id=1519)

Yes [en] (11)
+ [Yes](https://www.progarchives.com/album.asp?id=1823)
+ [Time and a Word](https://www.progarchives.com/album.asp?id=1824)
+ [The Yes Album](https://www.progarchives.com/album.asp?id=1826)
+ [Fragile](https://www.progarchives.com/album.asp?id=1825)
+ [Close to the Edge](https://www.progarchives.com/album.asp?id=1827)
+ [Tales from Topographic Oceans](https://www.progarchives.com/album.asp?id=1828)
+ [Relayer](https://www.progarchives.com/album.asp?id=1829)
+ [Going for the One](https://www.progarchives.com/album.asp?id=1831)
+ [Tormato](https://www.progarchives.com/album.asp?id=1832)
+ [Drama](https://www.progarchives.com/album.asp?id=1833)
+ [90125](https://www.progarchives.com/album.asp?id=1836)

Rush [en] (9)
+ [Rush](https://www.progarchives.com/album.asp?id=3067)
+ [Fly by Night](https://www.progarchives.com/album.asp?id=3068)
+ [Caress of Steel](https://www.progarchives.com/album.asp?id=3069)
+ [2112](https://www.progarchives.com/album.asp?id=3070)
+ [A Farewell to Kings](https://www.progarchives.com/album.asp?id=3072)
+ [Hemispheres](https://www.progarchives.com/album.asp?id=3073)
+ [Permanent Waves](https://www.progarchives.com/album.asp?id=3075)
+ [Moving Pictures](https://www.progarchives.com/album.asp?id=3076)
+ [Signals](https://www.progarchives.com/album.asp?id=3078)

King Crimson [en] (10)
+ [In the Court of the Crimson King](https://www.progarchives.com/album.asp?id=1903)
+ [In the Wake of Poseidon](https://www.progarchives.com/album.asp?id=1904)
+ [Lizard](https://www.progarchives.com/album.asp?id=1905)
+ [Islands](https://www.progarchives.com/album.asp?id=1906)
+ [Larks' Tongues in Aspic](https://www.progarchives.com/album.asp?id=1909)
+ [Starless and Bible Black](https://www.progarchives.com/album.asp?id=1910)
+ [Red](https://www.progarchives.com/album.asp?id=1911)
+ [Dicipline](https://www.progarchives.com/album.asp?id=1914)
+ [Beat](https://www.progarchives.com/album.asp?id=1915)
+ [Three of a Perfect Pair](https://www.progarchives.com/album.asp?id=1916)

Jethro Tull [en] (14)
+ [This Was](https://www.progarchives.com/album.asp?id=2015)
+ [Stand Up](https://www.progarchives.com/album.asp?id=2016)
+ [Benefit](https://www.progarchives.com/album.asp?id=2017)
+ [Aqualung](https://www.progarchives.com/album.asp?id=2018)
+ [Thick as a Brick](https://www.progarchives.com/album.asp?id=2019)
+ [A Passion Play](https://www.progarchives.com/album.asp?id=2022)
+ [War Child](https://www.progarchives.com/album.asp?id=2021)
+ [Minstrl in the Gallery](https://www.progarchives.com/album.asp?id=2023)
+ [Too Old To Rock 'n' Roll Too Young to Die!](https://www.progarchives.com/album.asp?id=2025)
+ [Songs from the Wood](https://www.progarchives.com/album.asp?id=2027)
+ [Heavy Horses](https://www.progarchives.com/album.asp?id=2028)
+ [Stormwatch](https://www.progarchives.com/album.asp?id=2030)
+ [A](https://www.progarchives.com/album.asp?id=2031)
+ [The Broadsword and the Beast](https://www.progarchives.com/album.asp?id=2032)


Emerson Lake and Palmer [en] (7)
+ [Emerson Lake & Palmer](https://www.progarchives.com/album.asp?id=1862)
+ [Pictures at an Exhibition](https://www.progarchives.com/album.asp?id=1870)
+ [Tarkus](https://www.progarchives.com/album.asp?id=1863)
+ [Trilogy](https://www.progarchives.com/album.asp?id=1871)
+ [Brain Salad Surgery](https://www.progarchives.com/album.asp?id=1872)
+ [Works Vol. 1](https://www.progarchives.com/album.asp?id=1874)
+ [Works Vol. 2](https://www.progarchives.com/album.asp?id=1875)

### Secondary Bands

Gentle Giant [en] (11)
+ [Gentle Giant](https://www.progarchives.com/album.asp?id=1144)
+ [Aquiring the Taste](https://www.progarchives.com/album.asp?id=1145)
+ [Three Friends](https://www.progarchives.com/album.asp?id=1146)
+ [Octopus](https://www.progarchives.com/album.asp?id=616)
+ [In a Glass House](https://www.progarchives.com/album.asp?id=1147)
+ [The Power and the Glory](https://www.progarchives.com/album.asp?id=1148)
+ [Free Hand](https://www.progarchives.com/album.asp?id=1149)
+ [Interview](https://www.progarchives.com/album.asp?id=1151)
+ [The Missing Piece](https://www.progarchives.com/album.asp?id=1152)
+ [Giant for a Day](https://www.progarchives.com/album.asp?id=1153)
+ [Civilian](https://www.progarchives.com/album.asp?id=1154)

Van Der Graaf Generator [en] (8)
+ [The Aerosol Grey Machine](https://www.progarchives.com/album.asp?id=1414)
+ [The Least We Can Do Is Wave to Each Other](https://www.progarchives.com/album.asp?id=1415)
+ [H to He, Who am the Only One](https://www.progarchives.com/album.asp?id=1416)
+ [Pawn Hearts](https://www.progarchives.com/album.asp?id=1417)
+ [Godbluff](https://www.progarchives.com/album.asp?id=1419)
+ [Still Life](https://www.progarchives.com/album.asp?id=1420)
+ [World Record](https://www.progarchives.com/album.asp?id=1421)
+ [The Quiet Zone - The Pleasure Dome](https://www.progarchives.com/album.asp?id=1422)

Camel [en] (10)
+ [Camel](https://www.progarchives.com/album.asp?id=327)
+ [Mirage](https://www.progarchives.com/album.asp?id=328)
+ [The Snow Goose](https://www.progarchives.com/album.asp?id=329)
+ [Moonmadness](https://www.progarchives.com/album.asp?id=330)
+ [Rain Dances](https://www.progarchives.com/album.asp?id=331)
+ [Breathless](https://www.progarchives.com/album.asp?id=334)
+ [I Can See Your House From Here](https://www.progarchives.com/album.asp?id=335)
+ [Nude](https://www.progarchives.com/album.asp?id=336)
+ [The Single Factor](https://www.progarchives.com/album.asp?id=337)
+ [Stationary Traveller](https://www.progarchives.com/album.asp?id=339)

Alan Parsons Project [en] (7)
+ [Tales of Mystery and Imagination](https://www.progarchives.com/album.asp?id=1091)
+ [I Robot](https://www.progarchives.com/album.asp?id=1092)
+ [Pyramid](https://www.progarchives.com/album.asp?id=1093)
+ [Eve](https://www.progarchives.com/album.asp?id=1094)
+ [The Turn of a Friendly Card](https://www.progarchives.com/album.asp?id=1095)
+ [Eye in the Sky](https://www.progarchives.com/album.asp?id=1096)
+ [Ammonia Avenue](https://www.progarchives.com/album.asp?id=1097)

Renaissance [en] (9)
+ [Renaissance](https://www.progarchives.com/album.asp?id=3018)
+ [Illusion](https://www.progarchives.com/album.asp?id=3019)
+ [Prologue](https://www.progarchives.com/album.asp?id=3020)
+ [Ashes Are Burning](https://www.progarchives.com/album.asp?id=3021)
+ [Turn of the Cards](https://www.progarchives.com/album.asp?id=3022)
+ [Scheherazade and Other Stories](https://www.progarchives.com/album.asp?id=3023)
+ [Novella](https://www.progarchives.com/album.asp?id=3025)
+ [A Song for All Seasons](https://www.progarchives.com/album.asp?id=3026)
+ [Azure d'Or](https://www.progarchives.com/album.asp?id=3028)

Eloy [en] (10)
+ [Eloy](https://www.progarchives.com/album.asp?id=505)
+ [Inside](https://www.progarchives.com/album.asp?id=506)
+ [Floating](https://www.progarchives.com/album.asp?id=507)
+ [Power and the Passion](https://www.progarchives.com/album.asp?id=509)
+ [Dawn](https://www.progarchives.com/album.asp?id=510)
+ [Ocean](https://www.progarchives.com/album.asp?id=511)
+ [Silent Cries and Mighty Echoes](https://www.progarchives.com/album.asp?id=513)
+ [Colours](https://www.progarchives.com/album.asp?id=514)
+ [Planets](https://www.progarchives.com/album.asp?id=515)
+ [Time to Turn](https://www.progarchives.com/album.asp?id=516)

Island [en] (1)
+ [Pictures](https://www.progarchives.com/album.asp?id=638)

Focus [en] (6)
+ [In and Out of Focus](https://www.progarchives.com/album.asp?id=3449)
+ [Moving Waves](https://www.progarchives.com/album.asp?id=3450)
+ [Focus 3](https://www.progarchives.com/album.asp?id=3451)
+ [Hamburger Concerto](https://www.progarchives.com/album.asp?id=3448)
+ [Mother Focus](https://www.progarchives.com/album.asp?id=3453)
+ [Ship of Memories](https://www.progarchives.com/album.asp?id=3454)

Wishbone Ash [en] (5)
+ [Wishbone Ash](https://www.progarchives.com/album.asp?id=11444)
+ [Pilgrimage](https://www.progarchives.com/album.asp?id=11445)
+ [Argus](https://www.progarchives.com/album.asp?id=11446)
+ [Wishbone Four](https://www.progarchives.com/album.asp?id=11447)
+ [There's the Rub](https://www.progarchives.com/album.asp?id=11449)

Curved Air [en] (4)
+ [Airconditioning](https://www.progarchives.com/album.asp?id=4795)
+ [Second Album](https://www.progarchives.com/album.asp?id=4796)
+ [Phantasmagoria](https://www.progarchives.com/album.asp?id=4797)
+ [Air Cut](https://www.progarchives.com/album.asp?id=4798)

Tangerine Dream [en] (3)
+ [Phaedra](https://www.progarchives.com/album.asp?id=6346)
+ [Rubycon](https://www.progarchives.com/album.asp?id=6347)
+ [Stratosfear](https://www.progarchives.com/album.asp?id=6348)

Hawkwind [en] (5)
+ [Hawkwind](https://www.progarchives.com/album.asp?id=3883)
+ [X in Search of Space](https://www.progarchives.com/album.asp?id=3884)
+ [Doremi Fasol Latido](https://www.progarchives.com/album.asp?id=3885)
+ [Hall of the Mountian Grill](https://www.progarchives.com/album.asp?id=3886)
+ [Warrior on the Edge of Time](https://www.progarchives.com/album.asp?id=3888)

Nektar [en] (6)
+ [Journey to the Center of the Eye](https://www.progarchives.com/album.asp?id=2730)
+ [A Tab in the Ocean](https://www.progarchives.com/album.asp?id=2731)
+ [...Sounds Like This](https://www.progarchives.com/album.asp?id=2732)
+ [Remember the Future](https://www.progarchives.com/album.asp?id=2733)
+ [Down to Earth](https://www.progarchives.com/album.asp?id=2734)
+ [Recycled](https://www.progarchives.com/album.asp?id=2736)

Triumvirat [en] (5)
+ [Mediterranean Tales (Across the Waters)](https://www.progarchives.com/album.asp?id=1683)
+ [Illusions on a Double Dimple](https://www.progarchives.com/album.asp?id=1684)
+ [Spartacus](https://www.progarchives.com/album.asp?id=1685)
+ [Old Loves Die Hard](https://www.progarchives.com/album.asp?id=1686)
+ [Pompeii](https://www.progarchives.com/album.asp?id=1687)

Ekseption [en] (8)
+ [Ekseption](https://www.progarchives.com/album.asp?id=6480)
+ [Beggar Julia's Time Trip](https://www.progarchives.com/album.asp?id=6481)
+ [Ekseption 3](https://www.progarchives.com/album.asp?id=6482)
+ [00-04](https://www.progarchives.com/album.asp?id=6483)
+ [Ekspetion 5](https://www.progarchives.com/album.asp?id=6484)
+ [Trinity](https://www.progarchives.com/album.asp?id=6485)
+ [Bingo](https://www.progarchives.com/album.asp?id=6486)
+ [Mindmirror](https://www.progarchives.com/album.asp?id=6487)

Trace [en] (2)
+ [Trace](https://www.progarchives.com/album.asp?id=1337)
+ [Birds](https://www.progarchives.com/album.asp?id=1338)

UK [en] (2)
+ [UK](https://www.progarchives.com/album.asp?id=1360)
+ [Danger Money](https://www.progarchives.com/album.asp?id=1361)

Supertramp [en] (4)
+ [Crime of the Century](https://www.progarchives.com/album.asp?id=1251)
+ [Crisis What Crisis](https://www.progarchives.com/album.asp?id=1252)
+ [Even in the Quietest Moments...](https://www.progarchives.com/album.asp?id=1253)
+ [Breakfast in America](https://www.progarchives.com/album.asp?id=1254)

Strawbs [en] ()
+ [Hero and Heroine](https://www.progarchives.com/album.asp?id=2896)
+ [Ghosts](https://www.progarchives.com/album.asp?id=2917)

Led Zeppelin [en] (8)
+ [Led Zeppelin](https://www.progarchives.com/album.asp?id=13526)
+ [Led Zeppelin II](https://www.progarchives.com/album.asp?id=13528)
+ [Led Zeppelin III](https://www.progarchives.com/album.asp?id=13531)
+ [Led Zeppelin IV](https://www.progarchives.com/album.asp?id=13535)
+ [Houses of the Holy](https://www.progarchives.com/album.asp?id=13530)
+ [Physical Graffiti](https://www.progarchives.com/album.asp?id=13527)
+ [Presence](https://www.progarchives.com/album.asp?id=13532)
+ [In Through the Out Door](https://www.progarchives.com/album.asp?id=13533)

The Who [en] (3)
+ [Tommy](https://www.progarchives.com/album.asp?id=16066)
+ [Who's Next](https://www.progarchives.com/album.asp?id=16064)
+ [Quadrophenia](https://www.progarchives.com/album.asp?id=16065)

Deep Purple [en] (11)
+ [Shades of Deep Purple](https://www.progarchives.com/album.asp?id=9116)
+ [The Book of Taliesyn](https://www.progarchives.com/album.asp?id=9117)
+ [Deep Purple](https://www.progarchives.com/album.asp?id=9118)
+ [Deep Purple in Rock](https://www.progarchives.com/album.asp?id=9120)
+ [Fireball](https://www.progarchives.com/album.asp?id=9121)
+ [Machine Head](https://www.progarchives.com/album.asp?id=9223)
+ [Who Do We Think We Are](https://www.progarchives.com/album.asp?id=9213)
+ [Burn](https://www.progarchives.com/album.asp?id=9214)
+ [Stormbringer](https://www.progarchives.com/album.asp?id=9176)
+ [Come Taste the Band](https://www.progarchives.com/album.asp?id=9215)
+ [Perfect Strangers](https://www.progarchives.com/album.asp?id=9216)

Uriah Heep [en] (6)
+ [Uriah Heep](https://www.progarchives.com/album.asp?id=5919)
+ [Salisbury](https://www.progarchives.com/album.asp?id=5895)
+ [Look At Yourself](https://www.progarchives.com/album.asp?id=5896)
+ [Demons and Wizards](https://www.progarchives.com/album.asp?id=5897)
+ [The Magician's Birthday](https://www.progarchives.com/album.asp?id=5898)
+ [Sweet Freedom](https://www.progarchives.com/album.asp?id=5899)

The Moody Blues [en] (1)
+ [Days of Future Passed](https://www.progarchives.com/album.asp?id=1938)

Kansas [en] (7)
+ [Kansas](https://www.progarchives.com/album.asp?id=3201)
+ [Song for America](https://www.progarchives.com/album.asp?id=3202)
+ [Masque](https://www.progarchives.com/album.asp?id=3203)
+ [Leftoverture](https://www.progarchives.com/album.asp?id=3204)
+ [Point of Know Return](https://www.progarchives.com/album.asp?id=3205)
+ [Monolith](https://www.progarchives.com/album.asp?id=3207)
+ [Audio Visions](https://www.progarchives.com/album.asp?id=3208)

Styx [en] (11)
+ [Styx](https://www.progarchives.com/album.asp?id=2186)
+ [Styx II](https://www.progarchives.com/album.asp?id=2198)
+ [The Serphent Is Rising](https://www.progarchives.com/album.asp?id=9262)
+ [Man of Miracles](https://www.progarchives.com/album.asp?id=2200)
+ [Equinox](https://www.progarchives.com/album.asp?id=2188)
+ [Crystal Ball](https://www.progarchives.com/album.asp?id=2189)
+ [The Grand Illusion](https://www.progarchives.com/album.asp?id=2190)
+ [Pieces of Eight](https://www.progarchives.com/album.asp?id=2191)
+ [Cornerstone](https://www.progarchives.com/album.asp?id=2192)
+ [Paradise Theatre](https://www.progarchives.com/album.asp?id=2193)
+ [Kilroy Was Here](https://www.progarchives.com/album.asp?id=2194)

### Solo Artists

Frank Zappa [en] (31)
+ [Freak Out!](https://www.progarchives.com/album.asp?id=5283)
+ [Absolutely Free](https://www.progarchives.com/album.asp?id=5284)
+ [Lumpy Gravy](https://www.progarchives.com/album.asp?id=5285)
+ [We're Only in It for the Money](https://www.progarchives.com/album.asp?id=5328)
+ [Uncle Meat](https://www.progarchives.com/album.asp?id=5329)
+ [Hot Rats](https://www.progarchives.com/album.asp?id=5330)
+ [Burnt Weeny Sandwich](https://www.progarchives.com/album.asp?id=5339)
+ [Weasels Ripped My Flesh](https://www.progarchives.com/album.asp?id=5427)
+ [Chunga's Revene](https://www.progarchives.com/album.asp?id=5341)
+ [200 Motels](https://www.progarchives.com/album.asp?id=5447)
+ [Waka - Jawaka](https://www.progarchives.com/album.asp?id=5426)
+ [The Grand Wazoo](https://www.progarchives.com/album.asp?id=5416)
+ [Over-Nite Sensation](https://www.progarchives.com/album.asp?id=5404)
+ [Apostrophe (')](https://www.progarchives.com/album.asp?id=5334)
+ [Roxy & Elsewhere](https://www.progarchives.com/album.asp?id=5406)
+ [One Size Fits All](https://www.progarchives.com/album.asp?id=5331)
+ [Bongo Fury](https://www.progarchives.com/album.asp?id=5336)
+ [Zoot Allures](https://www.progarchives.com/album.asp?id=5441)
+ [Zappa in New York](https://www.progarchives.com/album.asp?id=5439)
+ [Studio Tan](https://www.progarchives.com/album.asp?id=5414)
+ [Sleep Dirt](https://www.progarchives.com/album.asp?id=5410)
+ [Sheik Yerbouti](https://www.progarchives.com/album.asp?id=5407)
+ [Orchestral Favorites](https://www.progarchives.com/album.asp?id=5403)
+ [Joe's Garage Act I](https://www.progarchives.com/album.asp?id=5485)
+ [Joe's Garage Acts II & III](https://www.progarchives.com/album.asp?id=5486)
+ [Tinsel Town Rebellion](https://www.progarchives.com/album.asp?id=5425)
+ [Shut Up 'N Play Yer Guitar](https://www.progarchives.com/album.asp?id=5488)
+ [Shut Up 'N Play Yer Guitar Some More](https://www.progarchives.com/album.asp?id=5489)
+ [Return Of The Son Of Shut Up 'N Play Yer Guitar](https://www.progarchives.com/album.asp?id=5512)
+ [You Are What You Is](https://www.progarchives.com/album.asp?id=5428)
+ [Ship Arriving Too Late to Save a Drowning Witch](https://www.progarchives.com/album.asp?id=5408)

Steve Hackett [en] (4)
+ [Voyage of the Acolyte](https://www.progarchives.com/album.asp?id=4160)
+ [Please Don't Touch!](https://www.progarchives.com/album.asp?id=4161)
+ [Spectral Mornings](https://www.progarchives.com/album.asp?id=4162)
+ [Defector](https://www.progarchives.com/album.asp?id=4163)

Peter Gabriel [en] (4)
+ [Car](https://www.progarchives.com/album.asp?id=3634)
+ [Scratch](https://www.progarchives.com/album.asp?id=3635)
+ [Melt](https://www.progarchives.com/album.asp?id=3636)
+ [Security](https://www.progarchives.com/album.asp?id=3638)

Michael Rutherford [en] (1)
+ [Smallcreep's Day](https://www.progarchives.com/album.asp?id=4450)

Anthony Philips [en] (7)
+ [The Geese and the Ghost](https://www.progarchives.com/album.asp?id=4105)
+ [Wise After the Event](https://www.progarchives.com/album.asp?id=4106)
+ [Private Parts & Pieces](https://www.progarchives.com/album.asp?id=4108)
+ [Sides](https://www.progarchives.com/album.asp?id=4107)
+ [Private Parts & Pieces II - Back to the Pavillion](https://www.progarchives.com/album.asp?id=4109)
+ [1984](https://www.progarchives.com/album.asp?id=4111)
+ [Private Parts & Pieces III - Antiques](https://www.progarchives.com/album.asp?id=4110)

Chris Squire [en] (1)
+ [Fish Out of Water](https://www.progarchives.com/album.asp?id=4442)

Rick Wakeman [en] (1)
+ [The Six Wives of Henry VIII](https://www.progarchives.com/album.asp?id=3967)

Bill Bruford [en] (2)
+ [Feels Good to Me](https://www.progarchives.com/album.asp?id=4744)
+ [One of a Kind](https://www.progarchives.com/album.asp?id=4745)

Peter Hammill [en] (6)
+ [Fool's Mate](https://www.progarchives.com/album.asp?id=2276)
+ [Chameleon in the Shadow of the Night](https://www.progarchives.com/album.asp?id=2277)
+ [The Silent Corner and the Empty Stage](https://www.progarchives.com/album.asp?id=2274)
+ [In Camera](https://www.progarchives.com/album.asp?id=2278)
+ [Nadir's Big Chance](https://www.progarchives.com/album.asp?id=2280)
+ [Over](https://www.progarchives.com/album.asp?id=2281)

Mike Oldfield [en] (8)
+ [Tubular Bells](https://www.progarchives.com/album.asp?id=4488)
+ [Hergest Ridge](https://www.progarchives.com/album.asp?id=4891)
+ [Ommadawn](https://www.progarchives.com/album.asp?id=4893)
+ [Incantations](https://www.progarchives.com/album.asp?id=4895)
+ [Platinum](https://www.progarchives.com/album.asp?id=4897)
+ [QE2](https://www.progarchives.com/album.asp?id=4898)
+ [Five Miles Out](https://www.progarchives.com/album.asp?id=4899)
+ [Crises](https://www.progarchives.com/album.asp?id=4900)

Klaus Schultz [en] (3)
+ [Timewind](https://www.progarchives.com/album.asp?id=7534)
+ [Moondawn](https://www.progarchives.com/album.asp?id=7633)
+ [Mirage](https://www.progarchives.com/album.asp?id=7630)

### Canterbury Scene

Caravan [en] (7)
+ [Caravan](https://www.progarchives.com/album.asp?id=3106)
+ [If I Could Do It All Over Again, I'd Do It All Over You](https://www.progarchives.com/album.asp?id=3107)
+ [In the Land of Grey and Pink](https://www.progarchives.com/album.asp?id=3108)
+ [Waterloo Lily](https://www.progarchives.com/album.asp?id=3109)
+ [For Girls Who Grow Plump in the Night](https://www.progarchives.com/album.asp?id=3110)
+ [Cunning Stunts](https://www.progarchives.com/album.asp?id=3113)
+ [Blind Dog at St. Dunstans](https://www.progarchives.com/album.asp?id=3115)

Soft Machine [en] (9)
+ [The Soft Machine](https://www.progarchives.com/album.asp?id=3235)
+ [Volume Two](https://www.progarchives.com/album.asp?id=3236)
+ [Third](https://www.progarchives.com/album.asp?id=3237)
+ [Fourth](https://www.progarchives.com/album.asp?id=3238)
+ [Fifth](https://www.progarchives.com/album.asp?id=3239)
+ [Six](https://www.progarchives.com/album.asp?id=3240)
+ [Seven](https://www.progarchives.com/album.asp?id=3241)
+ [Bundles](https://www.progarchives.com/album.asp?id=3243)
+ [Softs](https://www.progarchives.com/album.asp?id=3244)

Matching Mole [en] (2)
+ [Maching Mole](https://www.progarchives.com/album.asp?id=917)
+ [Little Red Record](https://www.progarchives.com/album.asp?id=918)

Robert Wyatt [en] (1)
+ [Rock Bottom](https://www.progarchives.com/album.asp?id=5370)

Hatfield and the North [en] (2)
+ [Hatfield and the North](https://www.progarchives.com/album.asp?id=558)
+ [The Rotters' Club](https://www.progarchives.com/album.asp?id=559)

National Health [en] (2)
+ [National Health](https://www.progarchives.com/album.asp?id=982)
+ [Of Queues and Cures](https://www.progarchives.com/album.asp?id=983)

Quiet Sun [en] (1)
+ [Mainstream](https://www.progarchives.com/album.asp?id=8459)

Gryphon [en] (5)
+ [Gryphon](https://www.progarchives.com/album.asp?id=477)
+ [Midnight Mushrumps](https://www.progarchives.com/album.asp?id=478)
+ [Red Queen to Gryphon Three](https://www.progarchives.com/album.asp?id=479)
+ [Raindance](https://www.progarchives.com/album.asp?id=480)
+ [Treason](https://www.progarchives.com/album.asp?id=481)

Egg [en] (3)
+ [Egg](https://www.progarchives.com/album.asp?id=3501)
+ [The Polite Force](https://www.progarchives.com/album.asp?id=3502)
+ [The Civil Surface](https://www.progarchives.com/album.asp?id=3503)

Khan [en] (1)
+ [Space Shanty](https://www.progarchives.com/album.asp?id=5964)

Gong [en] (8)
+ [Magick Brother](https://www.progarchives.com/album.asp?id=4623)
+ [Camembert Electrique](https://www.progarchives.com/album.asp?id=4624)
+ [Radio Gnome Invisible Part 1 - Flying Teapot](https://www.progarchives.com/album.asp?id=4626)
+ [Radio Gnome Invisible Part 2 - Angel's Egg](https://www.progarchives.com/album.asp?id=4630)
+ [Radio Gnome Invisible Part 3 - You](https://www.progarchives.com/album.asp?id=4631)
+ [Shamal](https://www.progarchives.com/album.asp?id=4634)
+ [Gazeuse!](https://www.progarchives.com/album.asp?id=4681)
+ [Expresso II](https://www.progarchives.com/album.asp?id=4682)

Steve Hillage [en] (1)
+ [Fish Rising](https://www.progarchives.com/album.asp?id=4063)

Magma [en] (7)
+ [Magma](https://www.progarchives.com/album.asp?id=3303)
+ [1001 Centigrades](https://www.progarchives.com/album.asp?id=3304)
+ [Mekanik Destruktiv Kommandoh](https://www.progarchives.com/album.asp?id=3306)
+ [Qurdah Itah](https://www.progarchives.com/album.asp?id=7792)
+ [Kohntarkosz](https://www.progarchives.com/album.asp?id=3307)
+ [Udu Wudu](https://www.progarchives.com/album.asp?id=3309)
+ [Attahk](https://www.progarchives.com/album.asp?id=3310)

### Fusion

Mahavishnu Orchestra [en] (4)
+ [The Inner Mounting Flame](https://www.progarchives.com/album.asp?id=3356)
+ [Birds of Fire](https://www.progarchives.com/album.asp?id=3357)
+ [Apocalypse](https://www.progarchives.com/album.asp?id=3359)
+ [Visions of the Emerald Beyond](https://www.progarchives.com/album.asp?id=3360)

Return to Forever [en] (1)
+ [Romantic Warrior](https://www.progarchives.com/album.asp?id=5305)

Brand X [en] (3)
+ [Unorthodox Behaviour](https://www.progarchives.com/album.asp?id=3473)
+ [Moroccan Roll](https://www.progarchives.com/album.asp?id=3474)
+ [Masques](https://www.progarchives.com/album.asp?id=3476)

Arti E Mestieri [it] (1)
+ [Tilt - Immagini Per Un Orecchio](https://www.progarchives.com/album.asp?id=128)

Spin [en] (2)
+ [Spin](https://www.progarchives.com/album.asp?id=21776)
+ [Whirlwind](https://www.progarchives.com/album.asp?id=21777)

### Krautrock 

Can [en] (3)
+ [Tago Mago](https://www.progarchives.com/album.asp?id=3508)
+ [Ege Bamyasi](https://www.progarchives.com/album.asp?id=3509)
+ [Future Days](https://www.progarchives.com/album.asp?id=3510)

Amon Duul II [en] (1)
+ [Yeti](https://www.progarchives.com/album.asp?id=4691)

Neu! [de] (1)
+ [Neu!](https://www.progarchives.com/album.asp?id=3574)

### Rock Progressivo Italiano (RPI)

Premiata Forneria Marconi [it] (Award-Winning Marconi Bakery) (3)
+ [Storia Di Un Minuto](https://www.progarchives.com/album.asp?id=1984)
+ [Per Un Amico](https://www.progarchives.com/album.asp?id=1985)
+ [L'Isola Di Niente](https://www.progarchives.com/album.asp?id=2060)

Banco Del Mutuo Soccorso [it] (Bank of Mutual Trust) (3)
+ [Banco Del Mutuo Soccorso](https://www.progarchives.com/album.asp?id=1800)
+ [Darwin!](https://www.progarchives.com/album.asp?id=1801)
+ [Io Sono Nato Libero](https://www.progarchives.com/album.asp?id=170)

Le Orme [it] (The Footsteps) (4)
+ [Collage](https://www.progarchives.com/album.asp?id=2301)
+ [Uomo Di Pezza](https://www.progarchives.com/album.asp?id=2297)
+ [Felona E Sorona](https://www.progarchives.com/album.asp?id=2302)
+ [Contrappunti](https://www.progarchives.com/album.asp?id=2304)

Area [it] (4)
+ [Arbeit Macht Frei](https://www.progarchives.com/album.asp?id=102)
+ [Caution Radiation Area](https://www.progarchives.com/album.asp?id=104)
+ [Crac!](https://www.progarchives.com/album.asp?id=103)
+ [Meledetti](https://www.progarchives.com/album.asp?id=107)

Franco Battiato [it] (4)

+ [Fetus](https://www.progarchives.com/album.asp?id=8755)
+ [Pollution](https://www.progarchives.com/album.asp?id=8756)
+ [Sulle Corde Di Aries](https://www.progarchives.com/album.asp?id=8597)
+ [Clic](https://www.progarchives.com/album.asp?id=8757)

Quella Vecchia Locanda [it] (That Old Inn) (2)
+ [Quella Vecchia Locanda](https://www.progarchives.com/album.asp?id=1137)
+ [Il Tempo della Gioia](https://www.progarchives.com/album.asp?id=1138)

Museo Rosenbach [it] (Rosenbach Museum) (1)
+ [Zarathustra](https://www.progarchives.com/album.asp?id=967)

Il Balletto Di Bronzo [it] (The Bronze Ballet) (1)
+ [Ys](https://www.progarchives.com/album.asp?id=155)

Il Paesi Di Ballochi [it] (The Land of Toys) (1)
+ [Il Paese Dei Balocchi](https://www.progarchives.com/album.asp?id=3499)

L'Uovo Di Columbo [it] (The Egg of Columbus) (1)
+ [L'Uovo Di Columbo](https://www.progarchives.com/album.asp?id=2650)

Biglietto Per L'Inferno [it] (Ticket to Hell) (1)
+ [Biglietto Per L'Inferno](https://www.progarchives.com/album.asp?id=223)

New Trolls [it] (4)
+ [Concerto Grosso Per I New Trolls](https://www.progarchives.com/album.asp?id=2842)
+ [Searching for a Land](https://www.progarchives.com/album.asp?id=2844)
+ [UT](https://www.progarchives.com/album.asp?id=2843)
+ [Concerto Grosso No 2](https://www.progarchives.com/album.asp?id=2845)

Formula 3 [it] (1)
+ [Sognando e Risognando](https://www.progarchives.com/album.asp?id=2683)

Il Volo [it] (2)
+ [Il Volo](https://www.progarchives.com/album.asp?id=2484)
+ [Essere O Non Essere ?](https://www.progarchives.com/album.asp?id=2485)

Maxophone [it] (1)
+ [Maxophone](https://www.progarchives.com/album.asp?id=922)

Alphataurus [it] (1)
+ [Alphataurus](https://www.progarchives.com/album.asp?id=2463)

Osana [it] (2)
+ [L'Uomo](https://www.progarchives.com/album.asp?id=1029)
+ [Palepoli](https://www.progarchives.com/album.asp?id=1030)

Blocco Mentale [it] (Mental Block) (1)
+ [POA](https://www.progarchives.com/album.asp?id=174)

Raccomandata con Ricevuta di Ritorno [it] (Registered Mail with Return Receipt) (1)
+ [Per... Un Mondo Di Cristallo](https://www.progarchives.com/album.asp?id=2701)

Picchio Dal Pozzo [it] (Woodpecker from the Well) (1)
+ [Picchio Dal Pozzo](https://www.progarchives.com/album.asp?id=2566)

Semiramis [it] (1)
+ [Dedicato A Frazz](https://www.progarchives.com/album.asp?id=1214)

Celeste [it] (1)
+ [Principe Di Un Giorno](https://www.progarchives.com/album.asp?id=191)

Metamorfosi [it] (Metamophosis) (1)
+ [Inferno](http://www.progarchives.com/album.asp?id=926)

Locanda Delle Fate [it] (Fairy Inn) (1)
+ [Forse Le Lucciole Non Si Amano Più](https://www.progarchives.com/album.asp?id=819)

Il Rovescio Della Medaglia [it] (The Reverse of a Coin) (1)
+ [Contaminazione](https://www.progarchives.com/album.asp?id=1181)

Reale Academia Di Musica [it] (Royal Academy of Music) (1)
+ [Reale Academia Di Musica](https://www.progarchives.com/album.asp?id=4739)

Apoteosi [it] (Apotheosis) (1)
+ [Apoteosi](https://www.progarchives.com/album.asp?id=2807)

Campo Di Marte [it] (Field of Mars) (1)
+ [Campo Di Marte](https://www.progarchives.com/album.asp?id=2500)

Murple [it] (1)
+ [Io Sono Murple](https://www.progarchives.com/album.asp?id=2825)

### International

Bubu [es] (1)
+ [Anabelas](https://www.progarchives.com/album.asp?id=3184)

Crucis [es] (Cross) (2)
+ [Crucis](https://www.progarchives.com/album.asp?id=2496)
+ [Los Delirios Del Mariscal](https://www.progarchives.com/album.asp?id=2497)

Fusioon [es] (3)
+ [Fusioon](https://www.progarchives.com/album.asp?id=4395)
+ [Fusioon 2](https://www.progarchives.com/album.asp?id=4396)
+ [Minorisa](https://www.progarchives.com/album.asp?id=4397)

Harmonium [fr] (1)
+ [Si On Avait Besoin D'une Cinquième Saison](https://www.progarchives.com/album.asp?id=3160)

Avtograf [ru] (Autograph) (2)
- [Avtograf 1](https://www.progarchives.com/album.asp?id=10660) <-- Add cyrillic manually
- [Avtograf 2](https://www.youtube.com/watch?v=HG4pLt8ZppI) <-- YouTube Link (Add Manually)

Horizont [ru] (Horizon) (1)
+ [Summer in Town](https://www.progarchives.com/album.asp?id=4942)

East [hu] (2)
+ [Jatekok](https://www.progarchives.com/album.asp?id=279)
+ [Huseg](https://www.progarchives.com/album.asp?id=280)

### Artists To Include:
    - The Who ✓
    - Frank Zappa ✓
        Shut up 'n play yer guitar 1, 2, 3 (NOT THE BOX SET)
    - Deep Purple ✓
    - Uriah Heep ✓
    - Horizont ✓

## TAGGING

### Artist Tags
    artist-name
        Name of the artist.
    sub-genre
        Prog archives sub-genre.
    language
        Main language of the artist

### Album Tags
    album-name
        - Name of the album.
    album-rating
        - Prog archives cumulative user rating.
    album-length
        - Duration of the album.

### Track Tags
    tr-index
        - The total index of the track in the album. Do not restart count when the side changes.
    tr-lenth
        - Duration of the track.
    w-count
        - Word count of the track.
    *?tr-type (could be automated, NOT IMPLEMENTED)
        - standard
        - main-track
        - part-track
        - compound-track

### Word Tags
    pos
        - Part of Speech of the word (using an auto-tagger).
    lemma
        - The lemmatized form of the word (ie. Dogs, doggies, dog, dawg -> lemma="dog").
    