class Human:
  def __init__(self):
   self.health=100
   self.brain=100
   self.name=None
  def Go_To_School(self):
    print("They Are Going To School")
    self.brain+=5
    self.health-=3
  def Sleeping(self):
   print("They Are Sleeping")
   self.brain+=1
   self.health+=5
class Teacher (Human):
  def Talking(self):
   print("New Topic")
  def __init__(self):
   super().__init__()
   self.every_month_take_a_money=15000
class Student (Human):
   def Study(self):
    print("He Is Studing")
   def __init__(self): 
    super().__init__()
    self.everyday_have_a_homework=True

TeacherOBJ=Teacher()
StudentOBJ=Student()
TeacherOBJ.Talking()
TeacherOBJ.Go_To_School()
TeacherOBJ.Sleeping()
print(TeacherOBJ.health)