class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

song1 = ["Happy birthday to you",
        "I don't want to get sued",
        "So I'll stop right there"]

happy_bday = Song(song1)

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

#what does lyrics do? Where does its content come from?
