# Računarska analiza korpusa tekstova _Yu_ rok pesama<br/>

Cilj istraživanja jeste računarsko prikupljanje i analiza tekstova pesama izvođača iz bivše Jugoslavije. Tekstovi su preuzeti sa sajta LyricWiki metodom _grebanja veba_ (engl. web scraping) i analizirani pomoću tehnika _kopanja po tekstu_ (engl. text mining) i obrade prirodnih jezika, kako bi se stekao uvid u specifičnosti ondašnje jugoslovenske muzičke scene. <br/>

* `grebanje_veba.py`: automatski preuzima tekstove pesama sa sajta LyricWiki pomoću biblioteke `lyricsmaster`;
* `stylometry.r`: generiše vizualni prikaz grupisanja izvođača prema sličnosti tekstova pesama koje interpretiraju;
* `potkorpusi.py`: generiše 30 '.txt' datoteka (potkorpusa) sa tekstovima pesama za svakog izvođača ('Bajaga.txt', 'Bijelo-Dugme.txt' itd.);
* `mala_slova.py`: učitava 30 datoteka iz zadatog direktorijuma i velika slova svodi na mala;
* `xml-anotiranje.py`: vrši anotiranje korpusa u skladu sa XML sintaksom korišćenjem biblioteke `yattag` i zamenu specijalnih karaktera karakterima izlazne sekvence pomoću biblioteke `xml.sax.saxutils`;





