from lyricsmaster import LyricWiki

provider = LyricWiki()
izvodjaci = ['Bajaga', 'Bajaga & Instruktori', 'Bebi Dol', 'Bijelo Dugme',  'Dino Merlin', 'Divlje Jagode', 'Elektricni Orgazam', 'Galija', 'Goran Bregovic', 'Goran Karan', 'Hari Mata Hari', 'Haustor', 'Idoli', 'Indexi', 'Josipa Lisac', 'Kerber', 'Madame Piano', 'Mirzino Jato', 'Negative (RS)', 'Neverne Bebe', 'Nina Badric', 'Oktobar 1864', 'Partibrejkers', 'Prljavo Kazaliste', 'Rani Mraz', 'Smak', 'Van Gogh', 'Vesna Pisarovic', 'YU Grupa', 'Zabranjeno Pusenje', 'Zana', 'Zdravko Colic', 'Zeljko Joksimovic'] # lista izvođača čiji tekstovi se preuzimaju

def korpus(izvodjaci): 
    for izvodjac in izvodjaci:
        try:
            discography = provider.get_lyrics(izvodjac)
            for album in discography:    
                print('Album: ', album.title)
                for song in album:
                    print('Song: ', song.title)
                    print('Lyrics: ', song.lyrics)
                    discography.save() # čuvanje tekstova u {user}/Documents/lyricsmaster/
        except: # ukoliko na sajtu postoji samo naslov pesme, ali ne i sadržaj teksta 
            continue

korpus(izvodjaci)
