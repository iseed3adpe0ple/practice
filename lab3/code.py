#Functions
# def my_function(fname):
#   print("Hello " + fname)
# my_function("Deniyel")
# my_function("Vladimir")
# my_function("Iskander")

# def my_function(food):
#   for x in food:
#     print(x)
# fruits = ["apple", "banana", "cherry"]
# my_function(fruits)

# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)
# my_function(5, 6, c = 7, d = 8)

#Lambda
# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))

# def myfunc(n):
#   return lambda a : a * n
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(11))
# print(mytripler(11))

#Class & Objects
# class myclass:
#     x = 5
# p1 = myclass()
# print(p1.x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age) 

#Inheritance
# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#   def __str__(self):
#     return f"{self.name}({self.age})"
# p1 = Person("John", 36)
# print(p1)

# class Student(Person):
#     pass
# p2 = Student("Dan", 18)
# print(p2)


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    def __str__(self):
        return f"{self.fname} {self.lname}"
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.fname, self.lname, "to the class of", self.graduationyear)
p2 = Student("dan", 18, 2019)    
p2.welcome()
