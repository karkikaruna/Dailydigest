# Class is a blueprint for creating objects.

# A constructor is invoked when a object is being created.
# All classes hve a function __init__()which is automatically invoked when a object is created.

# the self parameter is a reference to the current
#instance of the class, and is used toaccess variables 
#thatbelongs to the class.

#attributes: variables, data that is inside class is known as attributes

#Methods : are functions that belong to objects.

#Staric methods : methods that dont use the self parameter (work at class level)

# class Student:

#     #default construcotrs
#     def __init__(self):
#         pass

#     college_name="ERC"
#     name="anonymous"

#     #parameterized constructor
#     def __init__(self,fullname, marks):
#         self.name=fullname
#         self.marks=marks
#         print("Adding new student in database.")
    
#     name="sita lama"

# s1=Student("sita", 99)
# print(s1.name, s1.marks)

# s2=Student("nitila",98)
# print(s2.name, s2.marks)

# Class & Instance Attributes

# class Student:
#     college_name="ERC"
#     #parameterized constructor
#     def __init__(self,fullname, marks):
#         self.name=fullname
#         self.marks=marks
        
#     def welcome(self):
#         print("Welcome student, ")

#     def get_marks(self):
#         return self.marks
# s1=Student("sita", 99)
# print(s1.name, s1.marks)
# s1.welcome()
# print(s1.get_marks())

# class Student:
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks
    
#     @staticmethod
#     def hello():
#         print("hello")
    
#     def average(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print("HI", self.name, "Your average score is: ", sum/3)
        

# s=Student("sita",[99,98,97])
# s.name="spiderwoman"
# s.average()
# s.hello()

#Importand: 4 pillars of OOPs
#Abstraction: Hiding the implementation details of a class and only showing the essential features to the user.

# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk=False
#         self.clutch= False
#     def start(self):
#         self.clutch= True
#         self.acc=True
#         print("Car started..")

# car1=Car()
# car1.start()

#Encapsulation: Wrapping data and related functions into a single unit(object).

class Account:

    def __init__(self, balance, accountno):
        self.balance=balance
        self.accountno=accountno
    
    def debit(self, amount):
        self.balance-=amount
        print("Rs.", amount , "was debited")
        print("Totalbalance =", self.get_balance())
    
    def credit(self, amount):
        self.balance+=amount
        print("Rs.", amount , "was credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance
a=Account(10000000000000, 7384950)
a.debit(3000)
a.credit(4000000000000000)

