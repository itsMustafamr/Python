class PartyAnimal:
   x = 0
   print("i will be constructed")

   def __init__(self):
    self.x = 0
    print("i was constructed")

   def party(self) :
     self.x = self.x + 1
     print("So far",self.x)

an = PartyAnimal() #
an.party()
an.party()
an.party()
print("dir is ", dir(an))