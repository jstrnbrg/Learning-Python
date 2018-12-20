from party import PartyAnimal

class CricketFan(PartyAnimal):
    points = 0

    def six(self):
        self.points += 6
        self.party()
        print(self.name,"has",self.points, "points")



s = PartyAnimal("Sally") # create ibstance of PartyAnimal
s.party() #invoke party method on s
j = CricketFan("Jim") # create instance of CricketFan
j.party() # invoke party menthod on j (inherited from PartyAnimal)
j.six() # invoke six on j
print(dir(j)) #print available methods and attributes of j
print(dir(s))
