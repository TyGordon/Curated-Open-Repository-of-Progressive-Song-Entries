# Curated Open Repository of Progressive Song Entries (CORPSE)

### This document covers many components of the CORPSE project including:
1. Information about the project, what is included and how to use it
2. Which bands and albums are used (Roughly 415 Albums)
3. How the entries are tagged

### Table of Contents
1. [Overview](#overview)
2. [Artist List](#artist-list)
    - [The Big Seven](#the-big-seven)
    - [Secondary Bands](#secondary-bands)
    - [Solo Artists](#solo-artists)
    - [Canturbury Scene](#canterbury-scene)
    - [Fusion](#fusion)
    - [Krautrock](#krautrock)
    - [RPI](#rock-progressivo-italiano-rpi)
    - [International](#international)
    - [Artists to Include](#artists-to-include)
3. [Track Tags](#tagging)
4. [Misc](#misc)

## OVERVIEW

### What Is This?
    This is the Curated Open Repository of Progressive Song Entries (CORPSE), which is a project developed for the University of Kentucky Corpus Linguistics course LIN-510. At its core, CORPSE is a collection of XML formatted song titles sourced from progarchives.com within the years 1966 to 1984. It comes with an Explorer utility, which is a Graphical User Interface (GUI) designed to allow any user the ability to search the database in a simple manner. 

    Progressive Rock is a term used to describe a genre of music that was prevalent in the late 60s, to the early 80s. It is usually described as a more complicated and eclectic form of popular music with many influences from genres such as Jazz, Classical, Blues, Folk Baroque, Soul, R&B, Electronic, Experimental, and Rock. This corpus only includes the "classic" era of Progressive Rock, and deliberatly excludes newer forms passed 1984 such as Progressive Metal, Neo-Prog, etc. Progressive Rock itself can be described with various sub-genres. The following links may be helpful for understanding the genre.

[Prog Archives Home](https://www.progarchives.com/)

[What is Progressive Rock?](http://www.progarchives.com/Progressive-rock.asp#definition)

[Top 100 Prog Albums 1966-1984](https://www.progarchives.com/top-prog-albums.asp?ssubgenres=&salbumtypes=1&syears=1984&syears=1983&syears=1982&syears=1981&syears=1980&syears=1979&syears=1978&syears=1977&syears=1976&syears=1975&syears=1974&syears=1973&syears=1972&syears=1971&syears=1970&syears=1969&syears=1968&syears=1967&syears=1966&scountries=&sminratings=0&smaxratings=0&sminavgratings=0&smaxresults=100&x=55&y=7#list)

### What's Included
    The CORPSE Corpus consists of two main tools and the data that makes up the corpus (both raw html and formatted xml files). The tools CORPSE Maker and CORPSE Explorer are made up of the following subcomponents:

    CORPSE MAKER
    1. README.md (This file) - To be used as the source of the URLs.
    2. curl_maker.py - A python program that builds a series of curl commands to fetch web data.
    3. corpus_curl.ps1 - The powershell script output from curl_maker.py. When run it executes the curl commands. 
    4. track_listing_scraper.py - A python program that takes the HTML pages from curl and converts it to formatted XML files to be used in the corpus.
    5. /Albums - A folder of all of the HTML pages used for the corpus.
    6. /Data - A folder of each album represented in an XML format.
    7. /Images - A folder with some images used for the GUI and its development.
    8. full_corpus.xml - An XML file with all of the data. This is used by the CORPSE Explorer.

    CORPSE EXPLORER
    1. corpus_explorer.py - A pyqt application that performs searches over the XML data.
    2. corpus_gui.ui - A QT ui file used for render the explorer GUI.
    3. reasources.qrc- a qrc file used by QT to load images, etc.

    OTHER
    1. 250_finder.py - A python program that finds all of the artists from the list of the top 250 albums from prog archives.
    2. top-250.html and top-250.txt - The input and output of 250_finder.py.

### What's Needed
    These resources are nessessary for re-assembling the corpus:
    - Microsoft Windows 10/11 OS (linux/mac are untested)
    - Curl for Windows (for curl_maker.py to work)
    - Python, pip (for .py programs)
    - NTLK (use pip) (used for POS tagging)
    - deep-translator (use pip) (used for translation)
    - QT and pyqt (use pip) (used for GUI)

    Otherwise, just running the CORPSE_Explorer.exe should work with no added software (full_corpus.xml is still needed)

### How To Use This Project
    1. Open the .exe

### Limitations
    Known Bugs:
    - Track names with a period followed by a space do not play nicely with the POS tagger: the tagger tends to eat them.
    - XML does not like the '&' character, so all instances were replaced with "and"
    - CURL does not like some characters such as '/', which had to be replaced with '-'
    - Many special characters (such as those of the cyrillic variety, or those with uncommon accent markers) had to be latinized
    
    Design Flaws:
    - Many albums are excluded for the following reasons:
        > They do not fit within the time frame (1966-1984).
            Ex. "Invisible Touch" by Genesis
        > They are under a different name.
            Ex. Magma's "Tristan et Iseult" ("Wurdah Itah")
        > The album has a very poor relative rating AND is at the end of the groups "golden era".
            Ex. Jethro Tull's "Under Wraps"
        > The respective group is nieche or borderline prog and only gets one album, with the rest omitted.
            Ex. Return to Forever's albums that are not "Romantic Warrior"
        > The group was not discovered/known about at corpus compiling time.
    - Tracks from foreign groups have to be hand translated in order to be represented. Hand Translation is an art (or at least an imprecise science) and has subjective implications on the corpus data.
    - The automatic XML generation makes any sub-track listed with an index of "-" have no proper index. THESE NEED TO BE FIXED MANUALLY.

## ARTIST LIST

### The "Big Seven"

Pink Floyd [ENG] (12)
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

Genesis [ENG] (12)
+ [From Genesis to Revelation](https://www.progarchives.com/album.asp?id=6)
+ [Trespass](https://www.progarchives.com/album.asp?id=2448)
+ [Nursery Cryme](https://www.progarchives.com/album.asp?id=3)
+ [Foxtrot](https://www.progarchives.com/album.asp?id=2)
+ [Selling England by the Pound](https://www.progarchives.com/album.asp?id=1510)
+ [The Lamb Lies Down on Broadway](https://www.progarchives.com/album.asp?id=1511)
+ [A Trick of the Tail](https://www.progarchives.com/album.asp?id=5)
+ [Wind & Wuthering](https://www.progarchives.com/album.asp?id=1512)
+ [...And Then There Were Three...](https://www.progarchives.com/album.asp?id=1515)
+ [Duke](https://www.progarchives.com/album.asp?id=1516)
+ [Abacab](https://www.progarchives.com/album.asp?id=1517)
+ [Genesis](https://www.progarchives.com/album.asp?id=1519)

Yes [ENG] (11)
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

Rush [ENG] (9)
+ [Rush](https://www.progarchives.com/album.asp?id=3067)
+ [Fly by Night](https://www.progarchives.com/album.asp?id=3068)
+ [Caress of Steel](https://www.progarchives.com/album.asp?id=3069)
+ [2112](https://www.progarchives.com/album.asp?id=3070)
+ [A Farewell to Kings](https://www.progarchives.com/album.asp?id=3072)
+ [Hemispheres](https://www.progarchives.com/album.asp?id=3073)
+ [Permanent Waves](https://www.progarchives.com/album.asp?id=3075)
+ [Moving Pictures](https://www.progarchives.com/album.asp?id=3076)
+ [Signals](https://www.progarchives.com/album.asp?id=3078)

King Crimson [ENG] (10)
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

Jethro Tull [ENG] (14)
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


Emerson Lake and Palmer [ENG] (7)
+ [Emerson Lake & Palmer](https://www.progarchives.com/album.asp?id=1862)
+ [Pictures at an Exhibition](https://www.progarchives.com/album.asp?id=1870)
+ [Tarkus](https://www.progarchives.com/album.asp?id=1863)
+ [Trilogy](https://www.progarchives.com/album.asp?id=1871)
+ [Brain Salad Surgery](https://www.progarchives.com/album.asp?id=1872)
+ [Works Vol. 1](https://www.progarchives.com/album.asp?id=1874)
+ [Works Vol. 2](https://www.progarchives.com/album.asp?id=1875)

### Secondary Bands

Gentle Giant [ENG] (11)
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

Van Der Graaf Generator [ENG] (8)
+ [The Aerosol Grey Machine](https://www.progarchives.com/album.asp?id=1414)
+ [The Least We Can Do Is Wave to Each Other](https://www.progarchives.com/album.asp?id=1415)
+ [H to He, Who am the Only One](https://www.progarchives.com/album.asp?id=1416)
+ [Pawn Hearts](https://www.progarchives.com/album.asp?id=1417)
+ [Godbluff](https://www.progarchives.com/album.asp?id=1419)
+ [Still Life](https://www.progarchives.com/album.asp?id=1420)
+ [World Record](https://www.progarchives.com/album.asp?id=1421)
+ [The Quiet Zone - The Pleasure Dome](https://www.progarchives.com/album.asp?id=1422)

Camel [ENG] (10)
+ [Camel](https://www.progarchives.com/album.asp?id=327)
+ [Mirage](https://www.progarchives.com/album.asp?id=328)
+ [The Snow Goose](https://www.progarchives.com/album.asp?id=329)
+ [Moonmadness](https://www.progarchives.com/album.assp?id=330)
+ [Rain Dances](https://www.progarchives.com/album.asp?id=331)
+ [Breathless](https://www.progarchives.com/album.asp?id=334)
+ [I Can See Your House From Here](https://www.progarchives.com/album.asp?id=335)
+ [Nude](https://www.progarchives.com/album.asp?id=336)
+ [The Single Factor](https://www.progarchives.com/album.asp?id=337)
+ [Stationary Traveller](https://www.progarchives.com/album.asp?id=339)

Alan Parsons Project [ENG] (7)
+ [Tales of Mystery and Imagination](https://www.progarchives.com/album.asp?id=1091)
+ [I Robot](https://www.progarchives.com/album.asp?id=1092)
+ [Pyramid](https://www.progarchives.com/album.asp?id=1093)
+ [Eve](https://www.progarchives.com/album.asp?id=1094)
+ [The Turn of a Friendly Card](https://www.progarchives.com/album.asp?id=1095)
+ [Eye in the Sky](https://www.progarchives.com/album.asp?id=1096)
+ [Ammonia Avenue](https://www.progarchives.com/album.asp?id=1097)

Renaissance [ENG] (9)
+ [Renaissance](https://www.progarchives.com/album.asp?id=3018)
+ [Illusion](https://www.progarchives.com/album.asp?id=3019)
+ [Prologue](https://www.progarchives.com/album.asp?id=3020)
+ [Ashes Are Burning](https://www.progarchives.com/album.asp?id=3021)
+ [Turn of the Cards](https://www.progarchives.com/album.asp?id=3022)
+ [Scheherazade and Other Stories](https://www.progarchives.com/album.asp?id=3023)
+ [Novella](https://www.progarchives.com/album.asp?id=3025)
+ [A Song for All Seasons](https://www.progarchives.com/album.asp?id=3026)
+ [Azure d'Or](https://www.progarchives.com/album.asp?id=3028)

Eloy [ENG] (10)
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

Island [ENG] (1)
+ [Pictures](https://www.progarchives.com/album.asp?id=638)

Focus [ENG] (6)
+ [In and Out of Focus](https://www.progarchives.com/album.asp?id=3449)
+ [Moving Waves](https://www.progarchives.com/album.asp?id=3450)
+ [Focus 3](https://www.progarchives.com/album.asp?id=3451)
+ [Hamburger Concerto](https://www.progarchives.com/album.asp?id=3448)
+ [Mother Focus](https://www.progarchives.com/album.asp?id=3453)
+ [Ship of Memories](https://www.progarchives.com/album.asp?id=3454)

Wishbone Ash [ENG] (5)
+ [Wishbone Ash](https://www.progarchives.com/album.asp?id=11444)
+ [Pilgrimage](https://www.progarchives.com/album.asp?id=11445)
+ [Argus](https://www.progarchives.com/album.asp?id=11446)
+ [Wishbone Four](https://www.progarchives.com/album.asp?id=11447)
+ [There's the Rub](https://www.progarchives.com/album.asp?id=11449)

Curved Air [ENG] (4)
+ [Airconditioning](https://www.progarchives.com/album.asp?id=4795)
+ [Second Album](https://www.progarchives.com/album.asp?id=4796)
+ [Phantasmagoria](https://www.progarchives.com/album.asp?id=4797)
+ [Air Cut](https://www.progarchives.com/album.asp?id=4798)

Tangerine Dream [ENG] (3)
+ [Phaedra](https://www.progarchives.com/album.asp?id=6346)
+ [Rubycon](https://www.progarchives.com/album.asp?id=6347)
+ [Stratosfear](https://www.progarchives.com/album.asp?id=6348)

Hawkwind [ENG] (5)
+ [Hawkwind](https://www.progarchives.com/album.asp?id=3883)
+ [X in Search of Space](https://www.progarchives.com/album.asp?id=3884)
+ [Doremi Fasol Latido](https://www.progarchives.com/album.asp?id=3885)
+ [Hall of the Mountian Grill](https://www.progarchives.com/album.asp?id=3886)
+ [Warrior on the Edge of Time](https://www.progarchives.com/album.asp?id=3888)

Nektar [ENG] (6)
+ [Journey to the Center of the Eye](https://www.progarchives.com/album.asp?id=2730)
+ [A Tab in the Ocean](https://www.progarchives.com/album.asp?id=2731)
+ [...Sounds Like This](https://www.progarchives.com/album.asp?id=2732)
+ [Remember the Future](https://www.progarchives.com/album.asp?id=2733)
+ [Down to Earth](https://www.progarchives.com/album.asp?id=2734)
+ [Recycled](https://www.progarchives.com/album.asp?id=2736)

Triumvirat [ENG] (5)
+ [Mediterranean Tales (Across the Waters)](https://www.progarchives.com/album.asp?id=1683)
+ [Illusions on a Double Dimple](https://www.progarchives.com/album.asp?id=1684)
+ [Spartacus](https://www.progarchives.com/album.asp?id=1685)
+ [Old Loves Die Hard](https://www.progarchives.com/album.asp?id=1686)
+ [Pompeii](https://www.progarchives.com/album.asp?id=1687)

Ekseption [ENG] (8)
+ [Ekseption](https://www.progarchives.com/album.asp?id=6480)
+ [Beggar Julia's Time Trip](https://www.progarchives.com/album.asp?id=6481)
+ [Ekseption 3](https://www.progarchives.com/album.asp?id=6482)
+ [00-04](https://www.progarchives.com/album.asp?id=6483)
+ [Ekspetion 5](https://www.progarchives.com/album.asp?id=6484)
+ [Trinity](https://www.progarchives.com/album.asp?id=6485)
+ [Bingo](https://www.progarchives.com/album.asp?id=6486)
+ [Mindmirror](https://www.progarchives.com/album.asp?id=6487)

Trace [ENG] (2)
+ [Trace](https://www.progarchives.com/album.asp?id=1337)
+ [Birds](https://www.progarchives.com/album.asp?id=1338)

UK [ENG] (2)
+ [UK](https://www.progarchives.com/album.asp?id=1360)
+ [Danger Money](https://www.progarchives.com/album.asp?id=1361)

Supertramp [ENG] (4)
+ [Crime of the Century](https://www.progarchives.com/album.asp?id=1251)
+ [Crisis What Crisis](https://www.progarchives.com/album.asp?id=1252)
+ [Even in the Quietest Moments...](https://www.progarchives.com/album.asp?id=1253)
+ [Breakfast in America](https://www.progarchives.com/album.asp?id=1254)

Strawbs [ENG] ()
+ [Hero and Heroine](https://www.progarchives.com/album.asp?id=2896)
+ [Ghosts](https://www.progarchives.com/album.asp?id=2917)

Led Zeppelin [ENG] (8)
+ [Led Zeppelin](https://www.progarchives.com/album.asp?id=13526)
+ [Led Zeppelin II](https://www.progarchives.com/album.asp?id=13528)
+ [Led Zeppelin III](https://www.progarchives.com/album.asp?id=13531)
+ [Led Zeppelin IV](https://www.progarchives.com/album.asp?id=13535)
+ [Houses of the Holy](https://www.progarchives.com/album.asp?id=13530)
+ [Physical Graffiti](https://www.progarchives.com/album.asp?id=13527)
+ [Presence](https://www.progarchives.com/album.asp?id=13532)
+ [In Through the Out Door](https://www.progarchives.com/album.asp?id=13533)

The Who [ENG] (3)
+ [Tommy](https://www.progarchives.com/album.asp?id=16066)
+ [Who's Next](https://www.progarchives.com/album.asp?id=16064)
+ [Quadrophenia](https://www.progarchives.com/album.asp?id=16065)

Deep Purple [ENG] (11)
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

Uriah Heep [ENG] (6)
+ [Uriah Heep](https://www.progarchives.com/album.asp?id=5919)
+ [Salisbury](https://www.progarchives.com/album.asp?id=5895)
+ [Look At Yourself](https://www.progarchives.com/album.asp?id=5896)
+ [Demons and Wizards](https://www.progarchives.com/album.asp?id=5897)
+ [The Magician's Birthday](https://www.progarchives.com/album.asp?id=5898)
+ [Sweet Freedom](https://www.progarchives.com/album.asp?id=5899)

The Moody Blues [ENG] (1)
+ [Days of Future Passed](https://www.progarchives.com/album.asp?id=1938)

Kansas [ENG] (7)
+ [Kansas](https://www.progarchives.com/album.asp?id=3201)
+ [Song for America](https://www.progarchives.com/album.asp?id=3202)
+ [Masque](https://www.progarchives.com/album.asp?id=3203)
+ [Leftoverture](https://www.progarchives.com/album.asp?id=3204)
+ [Point of Know Return](https://www.progarchives.com/album.asp?id=3205)
+ [Monolith](https://www.progarchives.com/album.asp?id=3207)
+ [Audio Visions](https://www.progarchives.com/album.asp?id=3208)

Styx [ENG] (11)
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

Frank Zappa [ENG] (31)
+ [Freak Out!](https://www.progarchives.com/album.asp?id=5283)
+ [Absolutely Free](https://www.progarchives.com/album.asp?id=5284)
+ [Lumpy Gravy](https://www.progarchives.com/album.asp?id=5285)
+ [We're Only in It for the Money](https://www.progarchives.com/album.asp?id=5328)
+ [Uncle Meat](https://www.progarchives.com/album.asp?id=5329)
+ [Hot Rats](https://www.progarchives.com/album.asp?id=5330)
+ [Burnt Weeny Sandwich](https://www.progarchives.com/album.asp?id=5339)
+ [Weasels Ripped My Flesh](https://www.progarchives.com/album.asp?id=5427)
+ [Chunga's Revenge](https://www.progarchives.com/album.asp?id=5341)
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

Steve Hackett [ENG] (4)
+ [Voyage of the Acolyte](https://www.progarchives.com/album.asp?id=4160)
+ [Please Don't Touch!](https://www.progarchives.com/album.asp?id=4161)
+ [Spectral Mornings](https://www.progarchives.com/album.asp?id=4162)
+ [Defector](https://www.progarchives.com/album.asp?id=4163)

Peter Gabriel [ENG] (4)
+ [Car](https://www.progarchives.com/album.asp?id=3634)
+ [Scratch](https://www.progarchives.com/album.asp?id=3635)
+ [Melt](https://www.progarchives.com/album.asp?id=3636)
+ [Security](https://www.progarchives.com/album.asp?id=3638)

Michael Rutherford [ENG] (1)
+ [Smallcreep's Day](https://www.progarchives.com/album.asp?id=4450)

Anthony Philips [ENG] (7)
+ [The Geese and the Ghost](https://www.progarchives.com/album.asp?id=4105)
+ [Wise After the Event](https://www.progarchives.com/album.asp?id=4106)
+ [Private Parts & Pieces](https://www.progarchives.com/album.asp?id=4108)
+ [Sides](https://www.progarchives.com/album.asp?id=4107)
+ [Private Parts & Pieces II - Back to the Pavillion](https://www.progarchives.com/album.asp?id=4109)
+ [1984](https://www.progarchives.com/album.asp?id=4111)
+ [Private Parts & Pieces III - Antiques](https://www.progarchives.com/album.asp?id=4110)

Chris Squire [ENG] (1)
+ [Fish Out of Water](https://www.progarchives.com/album.asp?id=4442)

Rick Wakeman [ENG] (1)
+ [The Six Wives of Henry VIII](https://www.progarchives.com/album.asp?id=3967)

Bill Bruford [ENG] (2)
+ [Feels Good to Me](https://www.progarchives.com/album.asp?id=4744)
+ [One of a Kind](https://www.progarchives.com/album.asp?id=4745)

Peter Hammill [ENG] (6)
+ [Fool's Mate](https://www.progarchives.com/album.asp?id=2276)
+ [Chameleon in the Shadow of the Night](https://www.progarchives.com/album.asp?id=2277)
+ [The Silent Corner and the Empty Stage](https://www.progarchives.com/album.asp?id=2274)
+ [In Camera](https://www.progarchives.com/album.asp?id=2278)
+ [Nadir's Big Chance](https://www.progarchives.com/album.asp?id=2280)
+ [Over](https://www.progarchives.com/album.asp?id=2281)

Mike Oldfield [ENG] (8)
+ [Tubular Bells](https://www.progarchives.com/album.asp?id=4488)
+ [Hergest Ridge](https://www.progarchives.com/album.asp?id=4891)
+ [Ommadawn](https://www.progarchives.com/album.asp?id=4893)
+ [Incantations](https://www.progarchives.com/album.asp?id=4895)
+ [Platinum](https://www.progarchives.com/album.asp?id=4897)
+ [QE2](https://www.progarchives.com/album.asp?id=4898)
+ [Five Miles Out](https://www.progarchives.com/album.asp?id=4899)
+ [Crises](https://www.progarchives.com/album.asp?id=4900)

Klaus Schultz [ENG] (3)
+ [Timewind](https://www.progarchives.com/album.asp?id=7534)
+ [Moondawn](https://www.progarchives.com/album.asp?id=7633)
+ [Mirage](https://www.progarchives.com/album.asp?id=7630)

### Canterbury Scene

Caravan [ENG] (7)
+ [Caravan](https://www.progarchives.com/album.asp?id=3106)
+ [If I Could Do It All Over Again, I'd Do It All Over You](https://www.progarchives.com/album.asp?id=3107)
+ [In the Land of Grey and Pink](https://www.progarchives.com/album.asp?id=3108)
+ [Waterloo Lily](https://www.progarchives.com/album.asp?id=3109)
+ [For Girls Who Grow Plump in the Night](https://www.progarchives.com/album.asp?id=3110)
+ [Cunning Stunts](https://www.progarchives.com/album.asp?id=3113)
+ [Blind Dog at St. Dunstans](https://www.progarchives.com/album.asp?id=3115)

Soft Machine [ENG] (9)
+ [The Soft Machine](https://www.progarchives.com/album.asp?id=3235)
+ [Volume Two](https://www.progarchives.com/album.asp?id=3236)
+ [Third](https://www.progarchives.com/album.asp?id=3237)
+ [Fourth](https://www.progarchives.com/album.asp?id=3238)
+ [Fifth](https://www.progarchives.com/album.asp?id=3239)
+ [Six](https://www.progarchives.com/album.asp?id=3240)
+ [Seven](https://www.progarchives.com/album.asp?id=3241)
+ [Bundles](https://www.progarchives.com/album.asp?id=3243)
+ [Softs](https://www.progarchives.com/album.asp?id=3244)

Matching Mole [ENG] (2)
+ [Maching Mole](https://www.progarchives.com/album.asp?id=917)
+ [Little Red Record](https://www.progarchives.com/album.asp?id=918)

Robert Wyatt [ENG] (1)
+ [Rock Bottom](https://www.progarchives.com/album.asp?id=5370)

Hatfield and the North [ENG] (2)
+ [Hatfield and the North](https://www.progarchives.com/album.asp?id=558)
+ [The Rotters' Club](https://www.progarchives.com/album.asp?id=559)

National Health [ENG] (2)
+ [National Health](https://www.progarchives.com/album.asp?id=982)
+ [Of Queues and Cures](https://www.progarchives.com/album.asp?id=983)

Quiet Sun [ENG] (1)
+ [Mainstream](https://www.progarchives.com/album.asp?id=8459)

Gryphon [ENG] (5)
+ [Gryphon](https://www.progarchives.com/album.asp?id=477)
+ [Midnight Mushrumps](https://www.progarchives.com/album.asp?id=478)
+ [Red Queen to Gryphon Three](https://www.progarchives.com/album.asp?id=479)
+ [Raindance](https://www.progarchives.com/album.asp?id=480)
+ [Treason](https://www.progarchives.com/album.asp?id=481)

Egg [ENG] (3)
+ [Egg](https://www.progarchives.com/album.asp?id=3501)
+ [The Polite Force](https://www.progarchives.com/album.asp?id=3502)
+ [The Civil Surface](https://www.progarchives.com/album.asp?id=3503)

Khan [ENG] (1)
+ [Space Shanty](https://www.progarchives.com/album.asp?id=5964)

Gong [ENG] (8)
+ [Magick Brother](https://www.progarchives.com/album.asp?id=4623)
+ [Camembert Electrique](https://www.progarchives.com/album.asp?id=4624)
+ [Radio Gnome Invisible Part 1 - Flying Teapot](https://www.progarchives.com/album.asp?id=4626)
+ [Radio Gnome Invisible Part 2 - Angel's Egg](https://www.progarchives.com/album.asp?id=4630)
+ [Radio Gnome Invisible Part 3 - You](https://www.progarchives.com/album.asp?id=4631)
+ [Shamal](https://www.progarchives.com/album.asp?id=4634)
+ [Gazeuse!](https://www.progarchives.com/album.asp?id=4681)
+ [Expresso II](https://www.progarchives.com/album.asp?id=4682)

Steve Hillage [ENG] (1)
+ [Fish Rising](https://www.progarchives.com/album.asp?id=4063)

Magma [ZHL] (7)
+ [Magma](https://www.progarchives.com/album.asp?id=3303)
+ [1001 Centigrades](https://www.progarchives.com/album.asp?id=3304)
+ [Mekanik Destruktiv Kommandoh](https://www.progarchives.com/album.asp?id=3306)
+ [Qurdah Itah](https://www.progarchives.com/album.asp?id=7792)
+ [Kohntarkosz](https://www.progarchives.com/album.asp?id=3307)
+ [Udu Wudu](https://www.progarchives.com/album.asp?id=3309)
+ [Attahk](https://www.progarchives.com/album.asp?id=3310)

### Fusion

Mahavishnu Orchestra [ENG] (4)
+ [The Inner Mounting Flame](https://www.progarchives.com/album.asp?id=3356)
+ [Birds of Fire](https://www.progarchives.com/album.asp?id=3357)
+ [Apocalypse](https://www.progarchives.com/album.asp?id=3359)
+ [Visions of the Emerald Beyond](https://www.progarchives.com/album.asp?id=3360)

Return to Forever [ENG] (1)
+ [Romantic Warrior](https://www.progarchives.com/album.asp?id=5305)

Brand X [ENG] (3)
+ [Unorthodox Behaviour](https://www.progarchives.com/album.asp?id=3473)
+ [Moroccan Roll](https://www.progarchives.com/album.asp?id=3474)
+ [Masques](https://www.progarchives.com/album.asp?id=3476)

Arti E Mestieri [ITA] (1)
+ [Tilt - Immagini Per Un Orecchio](https://www.progarchives.com/album.asp?id=128)

Spin [ENG] (2)
+ [Spin](https://www.progarchives.com/album.asp?id=21776)
+ [Whirlwind](https://www.progarchives.com/album.asp?id=21777)

### Krautrock 

Can [ENG] (3)
+ [Tago Mago](https://www.progarchives.com/album.asp?id=3508)
+ [Ege Bamyasi](https://www.progarchives.com/album.asp?id=3509)
+ [Future Days](https://www.progarchives.com/album.asp?id=3510)

Amon Duul II [ENG] (1)
+ [Yeti](https://www.progarchives.com/album.asp?id=4691)

Neu! [GER] (1)
+ [Neu!](https://www.progarchives.com/album.asp?id=3574)

### Rock Progressivo Italiano (RPI)

Premiata Forneria Marconi [ITA] (Award-Winning Marconi Bakery) (3)
+ [Storia Di Un Minuto](https://www.progarchives.com/album.asp?id=1984)
+ [Per Un Amico](https://www.progarchives.com/album.asp?id=1985)
+ [L'Isola Di Niente](https://www.progarchives.com/album.asp?id=2060)

Banco Del Mutuo Soccorso [ITA] (Bank of Mutual Trust) (3)
+ [Banco Del Mutuo Soccorso](https://www.progarchives.com/album.asp?id=1800)
+ [Darwin!](https://www.progarchives.com/album.asp?id=1801)
+ [Io Sono Nato Libero](https://www.progarchives.com/album.asp?id=170)

Le Orme [ITA] (The Footsteps) (4)
+ [Collage](https://www.progarchives.com/album.asp?id=2301)
+ [Uomo Di Pezza](https://www.progarchives.com/album.asp?id=2297)
+ [Felona E Sorona](https://www.progarchives.com/album.asp?id=2302)
+ [Contrappunti](https://www.progarchives.com/album.asp?id=2304)

Area [ITA] (4)
+ [Arbeit Macht Frei](https://www.progarchives.com/album.asp?id=102)
+ [Caution Radiation Area](https://www.progarchives.com/album.asp?id=104)
+ [Crac!](https://www.progarchives.com/album.asp?id=103)
+ [Meledetti](https://www.progarchives.com/album.asp?id=107)

Franco Battiato [ITA] (4)

+ [Fetus](https://www.progarchives.com/album.asp?id=8755)
+ [Pollution](https://www.progarchives.com/album.asp?id=8756)
+ [Sulle Corde Di Aries](https://www.progarchives.com/album.asp?id=8597)
+ [Clic](https://www.progarchives.com/album.asp?id=8757)

Quella Vecchia Locanda [ITA] (That Old Inn) (2)
+ [Quella Vecchia Locanda](https://www.progarchives.com/album.asp?id=1137)
+ [Il Tempo della Gioia](https://www.progarchives.com/album.asp?id=1138)

Museo Rosenbach [ITA] (Rosenbach Museum) (1)
+ [Zarathustra](https://www.progarchives.com/album.asp?id=967)

Il Balletto Di Bronzo [ITA] (The Bronze Ballet) (1)
+ [Ys](https://www.progarchives.com/album.asp?id=155)

Il Paesi Di Ballochi [ITA] (The Land of Toys) (1)
+ [Il Paese Dei Balocchi](https://www.progarchives.com/album.asp?id=3499)

L'Uovo Di Columbo [ITA] (The Egg of Columbus) (1)
+ [L'Uovo Di Columbo](https://www.progarchives.com/album.asp?id=2650)

Biglietto Per L'Inferno [ITA] (Ticket to Hell) (1)
+ [Biglietto Per L'Inferno](https://www.progarchives.com/album.asp?id=223)

New Trolls [ITA] (4)
+ [Concerto Grosso Per I New Trolls](https://www.progarchives.com/album.asp?id=2842)
+ [Searching for a Land](https://www.progarchives.com/album.asp?id=2844)
+ [UT](https://www.progarchives.com/album.asp?id=2843)
+ [Concerto Grosso No 2](https://www.progarchives.com/album.asp?id=2845)

Formula 3 [ITA] (1)
+ [Sognando e Risognando](https://www.progarchives.com/album.asp?id=2683)

Il Volo [ITA] (2)
+ [Il Volo](https://www.progarchives.com/album.asp?id=2484)
+ [Essere O Non Essere ?](https://www.progarchives.com/album.asp?id=2485)

Maxophone [ITA] (1)
+ [Maxophone](https://www.progarchives.com/album.asp?id=922)

Alphataurus [ITA] (1)
+ [Alphataurus](https://www.progarchives.com/album.asp?id=2463)

Osana [ITA] (2)
+ [L'Uomo](https://www.progarchives.com/album.asp?id=1029)
+ [Palepoli](https://www.progarchives.com/album.asp?id=1030)

Blocco Mentale [ITA] (Mental Block) (1)
+ [POA](https://www.youtube.com/watch?v=1UsgljrA4Ss&list=LL&index=168&t=1013s)

Raccomandata con Ricevuta di Ritorno [ITA] (Registered Mail with Return Receipt) (1)
+ [Per... Un Mondo Di Cristallo](https://www.progarchives.com/album.asp?id=2701)

Picchio Dal Pozzo [ITA] (Woodpecker from the Well) (1)
+ [Picchio Dal Pozzo](https://www.progarchives.com/album.asp?id=2566)

Semiramis [ITA] (1)
+ [Dedicato A Frazz](https://www.progarchives.com/album.asp?id=1214)

Celeste [ITA] (1)
+ [Principe Di Un Giorno](https://www.progarchives.com/album.asp?id=191)

Metamorfosi [ITA] (Metamophosis) (1)
+ [Inferno](http://www.progarchives.com/album.asp?id=926)

Locanda Delle Fate [ITA] (Fairy Inn) (1)
+ [Forse Le Lucciole Non Si Amano Più](https://www.progarchives.com/album.asp?id=819)

Il Rovescio Della Medaglia [ITA] (The Reverse of a Coin) (1)
+ [Contaminazione](https://www.progarchives.com/album.asp?id=1181)

Reale Academia Di Musica [ITA] (Royal Academy of Music) (1)
+ [Reale Academia Di Musica](https://www.progarchives.com/album.asp?id=4739)

Apoteosi [ITA] (Apotheosis) (1)
+ [Apoteosi](https://www.progarchives.com/album.asp?id=2807)

Campo Di Marte [ITA] (Field of Mars) (1)
+ [Campo Di Marte](https://www.progarchives.com/album.asp?id=2500)

Murple [ITA] (1)
+ [Io Sono Murple](https://www.progarchives.com/album.asp?id=2825)

### International

Bubu [SPA] (1)
+ [Anabelas](https://www.progarchives.com/album.asp?id=3184)

Crucis [SPA] (Cross) (2)
+ [Crucis](https://www.progarchives.com/album.asp?id=2496)
+ [Los Delirios Del Mariscal](https://www.progarchives.com/album.asp?id=2497)

Fusioon [SPA] (3)
+ [Fusioon](https://www.progarchives.com/album.asp?id=4395)
+ [Fusioon 2](https://www.progarchives.com/album.asp?id=4396)
+ [Minorisa](https://www.progarchives.com/album.asp?id=4397)

Harmonium [FRE] (1)
+ [Si On Avait Besoin D'une Cinquième Saison](https://www.progarchives.com/album.asp?id=3160)

Avtograf [RUS] (Autograph) (2)
+ [Avtograf 1](https://www.progarchives.com/album.asp?id=10660)
- [Avtograf 2](https://www.youtube.com/watch?v=HG4pLt8ZppI) <-- YouTube Link (Add Manually)

East [HUN] (2)
+ [Jatekok](https://www.progarchives.com/album.asp?id=279)
+ [Huseg](https://www.progarchives.com/album.asp?id=280)

### Artists To Include:
    - The Who ✓
    - Frank Zappa ✓
        Shut up 'n play yer guitar 1, 2, 3 (NOT THE BOX SET)
    - Deep Purple ✓
    - Uriah Heep ✓

## TAGGING

### Artist Tags
    artist-name
        Name of the artist.
    sub-genre
        Prog archives sub-genre.

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
    tr-length
        - Duration of the track.
    w-count
        - Word count of the track.
    *?tr-type (could be automated)
        - standard
        - main-track
        - part-track
        - compound-track

    Manual Tags:
        has-pun="true"
        made-up="true"
        poorly-formed="true"
        non-semantic="true"
        not-english="true"

        imprecise-translation="true"
        title-track="true"
        hidden-track="true"
        single="true"

### Word Tags
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

## Potential Tags:

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

## MISC

### Misc Code
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

### Helpful Links
[POS Tagging - geeksforgeeks](https://www.geeksforgeeks.org/part-speech-tagging-stop-words-using-nltk-python/)

[Xpath tips](http://www.whitebeam.org/library/guide/TechNotes/xpath.rhtm)

[Xpath parser](http://xpather.com/)

### Xpath Code
    //artist/al[rating>0.0][length>0][@date]/tr[w/@lemma][length>0]