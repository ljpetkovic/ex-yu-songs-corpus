# Computational analysis of the YU rock song lyrics corpus <br/>

The aim of the research is to collect and analyse the song lyrics by the rock artists from the former Yugoslavia. The lyrics were collected from the LyricWiki and MetroLyrics website using web scraping methods. The implementation of text mining and NLP techniques reveals the underlying textual patterns in the corpus, based on which one can explore characteristics of the then-Yugoslav music scene. <br/>

* `lyricwiki.py`: scrapes the lyrics from the LyricWiki website using the `lyricsmaster` library;
* `metrolyrics.py`: scrapes the lyrics from the MetroLyrics website using the `tswift` library;
* `stylometry.r`: generates the dendrogram as a result of clustering the artists by their lyrics' similarity;
* `subcorpora.py`: generates 30 '.txt' files (sub-corpora) with the lyrics for each artist ('Bajaga.txt', 'Bijelo-Dugme.txt' etc.);
* `lowercase.py`: loads 30 files from the defined directory and changes upper case to lower case;
* `xml_annotation.py`: annotates the corpus in the XML format with the `yattag` library, while replacing special characters with the escape sequence characters (see the `xml.sax.saxutils` library);







