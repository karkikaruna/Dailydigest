#del keyword
# used to delete obhect properties or object itself.

# class Student:
#     def __init__(self, name):
#         self.name=name

# s1=Student("sita")

# del s1
# print(s1)

#Private(like) attributes & methods
#conceptual implementation in Python

# class Account:
    
#     def __init__(self, acc_no , acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass= acc_pass #private
    
#     def reset_pass(self):
#         print(self.__acc_pass)

# acc1=Account("12345", "abcde")

# print(acc1.acc_no)
# acc1.reset_pass()
# print(acc1.__acc_pass)
#they are meant to be accessed within the class and not outside the class.
# class Person:
#     __name="anonymous"

#     def __hello(self):
#         print("Hello world")

#     def welcome(self):
#         self.__hello()

# p1=Person()

#Inheritance
#when one class(child/derived) derives the properties & methods of another class(parent/base)

#Single Inheritance

# class Car:
#     color="black"
#     @staticmethod

#     def start():
#         print("Car started..")
    
#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class ToyotaCar(Car):

#     def __init__(self, name):
#         self.name=name
# car1=ToyotaCar("fortuner")
# car2=ToyotaCar("mercedes")

# print(car1.name)
# print(car1.start())
# print(car1.color)

#2. Multi-level Inheritance


# class Car:
#     @staticmethod
#     def start():
#         print("Car started..")
    
#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class ToyotaCar(Car):

#     def __init__(self,brand):
#         self.brand=brand

# class Fortuner(ToyotaCar):
#     def __init__(self , type):
#         self.type=type

# car1=Fortuner("Diesel")

# car1.start()

#3. Multiple Inheritance

# class A:
#     varA="welcome to class A"

# class B:
#     varB="welcome to class B"

# class C(A, B):
#     varC="welcome to class C"

# c1=C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

#Super method

#super() method is used to access method of the parent class.
# class Car:

#     def __init__(self, type):
#         self.type=type
#     @staticmethod
#     def start():
#         print("Car started..")
    
#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class ToyotaCar(Car):

#     def __init__(self,name, type):
        
#         super().__init__(type)
#         self.name=name

#         super().start()
    

# car1=ToyotaCar("prius", "electric")
# print(car1.type)

# class Person:
#     name="anonymous"

#     def changeName(self, name):
#         self.__class__.name="ea"
#         # Person.name=name

# p1=Person()
# p1.changeName("ea hora")
# print(p1.name)

# print(Person.name)

#class method

# A class method is bound to the class as an implicit first argument.
#Note: static method can'taccess or modify class state & generally for urility.

# class Person:
#     name="anonymous"
    
#     @classmethod
#     def changeName(cls, name):
#         cls.name=name

# p1=Person()
# p1.changeName("ea hora")
# print(p1.name)

# print(Person.name)

#Three types of method:
#1. static methods
#2. class methods
#3. instance methods

# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math


#     @property
#     def percentage(self):
#          return str((self.phy+ self.chem+ self.math)/3) + "%"


# stu1=Student(99,98, 97)
# print(stu1.percentage)
# stul1=96


#@getter
#@setter

#Polymorphism: operator overloading
# when the same operator is allowed to have different meaning according to the context
#Implicit overloadig

# print(1+2)
# print(type(1))
# print([2,3,4]+ [5,6,7])
# print(type([1,2,3]))
# print("hello" + "world")
# print(type("hello"))

#Dunder Functions 
#  a.__add__(b)

# class Complex:
#     def __init__(self, real, img):
#         self.real=real
#         self.img=img
#     def display(self):
#         print(self.real, "i +", self.img, "j")

#     def __add__(self, num2):
#         newreal=self.real+ num2.real
#         newimg=self.img+ num2.img
#         return Complex(newreal, newimg)

#     def __sub__(self, num2):
#         newreal=self.real- num2.real
#         newimg=self.img- num2.img
#         return Complex(newreal, newimg)

# num1=Complex(3,4)
# num1.display()

# num2=Complex(1,2)
# num2.display()

# num3=num1+ num2
# num3.display()

# num4=num1-num2
# num4.display()

# class Circle:
#     def __init__(self,r):
#         self.r=r
    
#     def Area(self):
#         area= (22/7)* (self.r**2)
#         print(f"Area of the circle is {area}")
#     def Perimeter(self):
#         perimeter=(22/7)* 2*self.r
#         print(f"Perimeter of the circle is: {perimeter}")

# c1=Circle(2)
# c1.Area()
# c1.Perimeter()

# class Employee:
#     def __init__(self, role, department, salary):
#         self.role=role
#         self.department=department
#         self.salary=salary
#     def showDetails(self):
#         print(f"The role of the employee is {self.role}, Her department is {self.department} and her salary is {self.salary}")

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#         super().__init__("Engineer", "IT", 500000)
#     def showDetails(self):
#         print("Name", self.name)
#         print("Age", self.age)



# engineer=Engineer("Elon Musk", 44)
# engineer.showDetails()

    
class Order:
    def __init__(self, item, price):
        self.item=item
        self.price=price
    
    def __gt__(self, order2):
        return self.price> order2.price

order1=Order("Fridge", 4000)
order2=Order("laptop", 500000)

print(order1> order2)
