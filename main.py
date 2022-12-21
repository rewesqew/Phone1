class Tourist:
  def __init__ (self):
   self.name= None
   self.age=None
   self.health=75
   self.moode=80
   self.IQ=None
  def walking(self):
   print("he is walking")
  def eating(self):
   print("he is eating")
  def sleeping(self):
    print("he is sleeping")

Tourist1=Tourist()
Tourist1.walking()
Tourist1.sleeping()
Tourist1.eating()
class teacher(Tourist):
 def __init__(self):
  super().__init__()
  self.money=1000
  self.age=51
  self.name= "Nikolay"
 def Talking(self):
  print("He Is Talking")

teacher1=teacher()
teacher1.walking()
teacher1.sleeping()
teacher1.eating()
teacher1.Talking()

