# class BankAccount:
#     def __init__(self, acc_num, name, bal):
#         self.account_number = acc_num
#         self.owner_name = name
#         self.balance = bal
#     def check_balance(self):
#         return self.balance
#     def deposit(self, amount):
#         if amount <= 0:
#             print("Deposit amount must be positive")
#             return
#         self.balance += amount
#         print("Deposited amount =", amount)
#         print("Current balance =", self.balance)
#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal amount must be positive")
#         elif self.balance < amount:
#             print("Insufficient balance!")
#         else:
#             self.balance -= amount
#             print("Withdrawn amount =", amount)
#             print("Current balance =", self.balance)
# emp1 = BankAccount(1234, "Alex", 5000)
# emp2 = BankAccount(1233, "Bob", 10000)
# print(emp1.check_balance())
# print(emp2.check_balance())
# emp1.deposit(1500)
# emp2.deposit(5000)
# print(emp1.check_balance())
# print(emp2.check_balance())
# emp1.withdraw(500000)
# emp2.withdraw(500)




# class Book:
#     def __init__(self, title, author, reviews):
#         self.title = title
#         self.author = author
#         self.reviews = reviews
#     def countReviews(self):
#         return len(self.reviews)
#     def displayReviews(self):
#         for r in self.reviews:
#             print(r)
#     def addReview(self, review):
#         self.reviews.append(review)
# b1 = Book("Rich Dad Poor Dad", "RC", ["Good", "Excellent", "Superb"])
# print(b1.countReviews())
# b1.displayReviews()
# b1.addReview("Mind blowing")
# b1.displayReviews()








# class Student:
#     def __init__(self, name, roll_no, marks):
#         if name != "":
#             self.__name = name
#         else:
#             print("Name cannot be empty")
#             self.__name = None

#         if roll_no in range(1, 101):
#             self.__roll_no = roll_no
#         else:
#             print("Roll Number range should be 1 to 100")
#             self.__roll_no = None

#         if marks >= 0:
#             self.__marks = marks
#         else:
#             print("Marks cannot be negative")
#             self.__marks = None

#     def getName(self):
#         return self.__name

#     def getRollNo(self):
#         return self.__roll_no

#     def getMarks(self):
#         return self.__marks

# s1 = Student("     ", 221, -95)
# print(s1.getName())
# print(s1.getRollNo())
# print(s1.getMarks())





# Concept: Inheritance
# Q5. Create a base class Vehicle with attributes like brand and model.
# Create two subclasses Car and Bike that add extra attributes - seats (in Car) &
# engine_cc (in Bike).

# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

# class Car(Vehicle):
#     def __init__(self, brand, model, seats):
#         super().__init__(brand, model)
#         self.seats = seats

# class Bike(Vehicle):
#     def __init__(self, brand, model, engine_cc):
#         super().__init__(brand, model)
#         self.engine_cc = engine_cc

# car1 = Car("Toyota", "Innova", 7)
# bike1 = Bike("Honda", "Shine", 125)

# print(car1.model, car1.brand, car1.seats)
# print(bike1.model, bike1.brand, bike1.engine_cc)













# Concept: Abstraction
# Q6. Create an abstract class Employee with an abstract method
# calculate_salary.
# Create subclasses Intern, FullTimeEmployee, and ContractEmployee that
# implement the method differently.

# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass

# class Intern(Employee):
#     def calculate_salary(self):
#         self.salary = "2 LPA"
#         return self.salary

# class FullTimeEmployee(Employee):
#     def calculate_salary(self):
#         self.salary = "3.2 LPA"
#         return self.salary

# class ContractEmployee(Employee):
#     def calculate_salary(self):
#         self.salary = "2.8 LPA"
#         return self.salary


# intern = Intern()
# fte = FullTimeEmployee()
# contract = ContractEmployee()

# print(intern.calculate_salary())
# print(fte.calculate_salary())
# print(contract.calculate_salary())




# Concept: Function Overriding
# Q4. Create a class Shape with a method area().
# Create subclasses Circle, Rectangle, and Triangle that override the area() method.

# Concept: Function Overriding

# class Shape:
#     def area(self):
#         print("Area of Shape")

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius * self.radius

# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#     def area(self):
#         return self.length * self.breadth

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def area(self):
#         return 0.5 * self.base * self.height
    
# s = Shape()
# c = Circle(5)
# r = Rectangle(10, 5)
# t = Triangle(8, 4)
# s.area()
# print("Area of Circle:", c.area())
# print("Area of Rectangle:", r.area())
# print("Area of Triangle:", t.area())








# Concept: Constructor Overloading (with Default Parameters)
# Q7. Create a class Person that allows the constructor to work with:
# • name only
# • name + age
# • name + age + address
# As direct constructor overloading (multiple constructors) are not allowed but
# we have to use default parameters to simulate constructor overloading.

# class Person:
#     def __init__(self, name, age = 0, address = "India"):
#         self.name = name
#         self.age = age
#         self.address = address
#     def display(self):
#         return f"{self.name}\n{self.age}\n{self.address}"

# p = Person("Saklain")
# print(p.display())
# p1 = Person("Saklain", 25)
# print(p1.display())
# p2 = Person("Saklain", 24, "Mysuru")
# print(p2.display())







# Concept: Instance & Class Attributes
# Q8. Create a class Player with:
# • a class variable player_count
# • instance variables name and level
# Track how many players were created.

# class Player:
#     player_count = 0  # Class attribute
#     def __init__(self, name, level):
#         self.name = name
#         self.level = level
#         Player.player_count += 1  # Update class attribute

# p = Player("alex", 1)
# print(p.player_count)
# p1 = Player("bob", 3)
# print(p1.player_count)
# print("Total players:", Player.player_count)





# Concept: Multiple Inheritance
# Q9. Create the following classes: Herbivore, Carnivore, Omnivore with some
# attributes & methods. Then create a class Bear that inherits from all the above
# classes to showcase how multiple inheritance works.

# class Herbivore:
#     type = "Herbivore"
#     def eats(self):
#         return "Eats grass"

# class Carnivore:
#     type = "Carnivore"
#     def eats(self):
#         return "Eats meat"

# class Omnivore:
#     type = "Omnivore"
#     def eats(self):
#         return "Eats both grass and meat"

# class Bear(Herbivore, Carnivore, Omnivore):
#     pass

# b = Bear()
# print(b.type)
# print(b.eats())
# print(Bear.mro())

