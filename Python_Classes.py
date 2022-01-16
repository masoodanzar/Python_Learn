class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

class Personx:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Personx("John", 36)
p1.myfunc()
p1.age = 40 # Modify Parameters
del p1.age # Delete Parameters
del p1 # Delete Object


# Python Inheritance allows us to define a Child class that inherits from Parent class class.
# Create a Parent Class
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()
# Create a Child Class
class Student(Person):
  pass # if you have a class definition with no content, put in the pass statement 
x = Student("Mike", "Olsen")
x.printname()
