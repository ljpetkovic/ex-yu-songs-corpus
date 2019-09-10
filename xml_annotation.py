from xml.sax.saxutils import escape
import os
from os import listdir 
from os.path import isfile, join
from yattag import Doc, indent

def replace_char_entities(s): 
    return escape(s) 

myroot = '/Users/ljudmilapetkovic/Documents/LyricsMaster'
doc, tag, text = Doc().tagtext()

authors = [dir for dir in listdir(myroot) if not isfile(join(myroot, dir))]

with tag('exYuPesme'):
    
    for author in authors:
        
        curr_path = '{}/{}'.format(myroot, author)
        albums = [dir for dir in listdir(curr_path) if not isfile(join(curr_path, dir))]
        
        with tag('autor', ime=author, brojAlbuma=len(albums), pol="", zanr="", rodnoMesto="", tema=""):
            
            for album in albums:
                with tag('album', naziv=album, godina="", izdavac=""):
                    
                    album_path = '{}/{}'.format(curr_path, album)
                    songs = [f for f in listdir(album_path) if isfile(join(album_path, f))]
                    for song in songs:
                        if not song.startswith('.DS_S'):
                            with tag('pesma', naslovPesme=song[:-4]):
                                song_path = '{}/{}'.format(album_path, song)
                                for stih in open(song_path, encoding="utf8", errors='ignore').read().split('\n')[:-1]:
                                    with tag('li'):
                                        text('{}'.format(replace_char_entities(stih)))
            

result = indent(
doc.getvalue(),
indentation = ' '*4,
newline = '\r\n'
)

print(result)
with open('ExYuKorpus.xml', 'w') as x:
    x.write(result)

