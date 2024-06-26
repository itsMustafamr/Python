class PartyAnimal:

   def __init__(self):
     self.x = 0
     print('I am constructed')

   def party(self) :
     self.x = self.x + 1
     print('So far',self.x)

   def __del__(self):
     print('I am destructed', self.x)

an = PartyAnimal() #here executes till i am constructed
an.party()
an.party()
an = 42 #here an no longer points to that object so it overides and before that line completes it calls the destructor 
print('an contains',an)