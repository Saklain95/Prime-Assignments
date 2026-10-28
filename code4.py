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


