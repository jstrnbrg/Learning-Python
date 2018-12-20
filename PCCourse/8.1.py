#Fuction that creates dictionary with optional tracks arghument
def make_album(artist, title, tracks = ""):
    if tracks:
        print({"Artist name": artist, "Album title": title, "Tracks": tracks})
    else:
        print({"Artist name": artist, "Album title": title})

#make_album("Amy", "New World", 7)
# make_album("John", "New Buzz")

while True:
    artist = input("Name of artist: ")
    if artist == "q":
        break
    title = input("Name of album: ")
    if title == "q":
        break
    tracks = input("How many tracks?: ")
    if tracks:
        make_album(artist, title, tracks)
        print(bool(tracks)) #A non empty var is True
    else:
        make_album(artist, title)
        print(bool(tracks)) #An empty var is False
