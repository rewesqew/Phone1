from random import *
class Dog1:
  def __init__(self):
   self.name="BOBIK"
   self.health=100
   self.eat="meat"
  def playing(self):
   print("he is playing")
   self.health+=5
  def eating(self):
   print("He is Eating")
   self.health+=15
  def live(self):
     live_cube=randint(1,2)
     if live_cube==1:
       self.playing()
     if live_cube==2:
       self.eating()
Dog=Dog1()
for I in range(10): 
  Dog.live()