def build_album1(artist, album, year=None, num_song=None):
    album = {'Artist': artist.title(), "Album": album.title()}
    if year: 
        album['Year'] = year 
    if num_song: 
        album['Num_song'] = num_song
    print(album) 