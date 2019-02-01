# #FUNCTIONS
#
# def say_hi(name):
#     """
#     This function say hi to the name
#     """
#     print("Hi, {}".format(name))
# #
# say_hi("Don")
#
#
# print(say_hi.__doc__) # the doc is giving the text in quote marks inserted
# #the doc string exists even if nothing is inserted specifically for it
#
# #ANNOTATIONS
#
# def say_hello(name: str) -> str:
#     """
#     DOCSTRING
#     """
#     return "Hi" + name
#
# print(say_hello.__doc__)
# print(say_hello.__annotations__)
# print()
# print(say_hello(" D"))


#WITH OR WITHOUT return

# def add1(*args):
#     sum = 0
#     for arg in args:
#         sum = sum + arg
#     return sum
#
# example1 = add1(1,2,3,4,5)
# print(example1)
#
# def add2(*args):
#     sum = 0
#     for arg in args:
#         sum = sum + arg
#     print(sum)
# example2 = add2(1,2,3,4,5)
#
# def add3(*args):
#     sum = 0
#     for arg in args:
#         sum = sum + arg
#
# example3 = add3(1,2,3,4,5)
# print(example3)
#
# def missing_char(str, n):
#     return str[0:n]+str[n+1:len(str)-1]
#     return str.replace(str[n],"")
#


#MODULES - 3 ways of importing a file

# import day4_modules as d4 or
# from day4_modules import car, car_detail
# print(day4_modules.car)
#
# car = "Audi"
# manu = "Germany"
# year = 2007
#
# day4_modules.car_detail(car,manu,year)

# import datetime as dt
# print(dt.datetime)

# Package = folder with many scripts that can be imported instead of a single module

#CLASSES has a collection of objects/instances
#instantiate is the action of interaction between objects

# class PythonProgrammer():
#     beard = "not so much"
#     pass
#
# daniel = PythonProgrammer() #instances of class
# kim = PythonProgrammer()
#
# print(daniel)
# print(kim)
#
# daniel.beard = "a lot"
#
# print(daniel.beard)
# print(kim.beard)



# class PythonProgrammer():
#     course = "Python 0 to 1"
#
#     def __init__(self, beautiful_name, nice_age, last_name):
#         self.name = beautiful_name
#         self.age = nice_age
#         # self.email = beautiful_name+"."+nice_age+"gmail.com"
#         self.email = f"{beautiful_name}.{nice_age}@gmail.com"
#         self.lastname = last_name
#
#
# dev1 = PythonProgrammer("Daniel",25,"Sexton")
# dev2 = PythonProgrammer("Daeun",20, "kim")
#
# dev1.course = "Python 0 to 2" ##class inheritance, taking a variable as the own
# # if a funct is defined inside a class it becomes a method if outside it is a function
# print(dev1.lastname)
# print(dev1.lastname)
# print(dev1.course)
# print(dev1.__dict__)
# print(dev2.course)
# print(dev2.__dict__)
# print(PythonProgrammer.course)
# print(PythonProgrammer.__dict__)

class Car:
    def __init__(self, brandname, year, origin): #there can only be one init constructor
        self.year = year
        self.origin = origin

    def stats(self): #regular method
        print("This is {}, it is made in {} in {}".format(self.brand, self.origin, self.year))


    def just_for_fun(self):
        sel.forFun = self.brand + "is stupid!"


my_car = Car("BMW", 2000, "Germany")
my_friends_car = Car("Audi", 2007, "Germany")
help(my_car)

#
# print(my_car.forFUn
# my_car.stats()
# my_friends_car.stats()



 # if a funct is defined inside a class it becomes a method if outside it is a function
