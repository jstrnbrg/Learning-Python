class PartyAnimal:
    x=0
    sum = 0

    def party(self) :
        self.x = self.x + 1
        print("So far",self.x)

    def addition(self, x, y):
        self.sum = self.sum + x + y
        print(self.sum)


an = PartyAnimal() #create an instance of PartyAnimal called an
be = PartyAnimal()


an.addition(2,5)
be.addition(5,8)
be.addition(5,8)

print ("Type", type(an)) # class
print ("Dir ", dir(an)) # shows attributes and methods of an
print ("Type", type(an.x)) # int
print ("Type", type(an.party)) # method
