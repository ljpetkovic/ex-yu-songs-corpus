import os
import cyrtranslit
from os import listdir 
from os.path import isfile, join

myroot = '/Users/ljudmilapetkovic/Documents/LyricsMaster'

authors = [dir for dir in listdir(myroot) if not isfile(join(myroot, dir))]

def autor_pesme(a, datoteka):
    with open(datoteka, 'w') as x:
        for author in authors:
            curr_path = '{}/{}'.format(myroot, author)
            if curr_path.endswith('{}'.format(a)):
                albums = [dir for dir in listdir(curr_path) if not isfile(join(curr_path, dir))]
                for album in albums:
                    album_path = '{}/{}'.format(curr_path, album)
                    songs = [f for f in listdir(album_path) if isfile(join(album_path, f))]
                    for song in songs:
                        if not song.startswith('.DS_S'):
                            song_path = '{}/{}'.format(album_path, song)
                            for stih in open(song_path, encoding="utf8", errors='ignore').read().split('\n')[:-1]:
                                line = '{}'.format(stih)
                                print(cyrtranslit.to_latin(line))
                                x.write(cyrtranslit.to_latin(line) + '\n') 
            else:
                pass
            
a = [author for author in authors] 
for a2 in a:
    autor_pesme(a2, a2 + '.txt')
