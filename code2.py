# a = float(input("Enter your salary : "))
# if a < 30000:
#     print(a * 5//100)
# elif a > 30_000 and a <= 70000:
#     print(a * 15//100)
# elif a > 70_000:
#     print(a * 25//100)


# a = int(input("Enter the number : "))
# b = int(input("Enter the number : "))
# for x in range(a,b+1):
#     if x % 2 == 0:
#         print(x)



# a = int(input("Enter the number : "))
# c = 0
# sum = 0
# while a > 0:
#     print(a % 10)
#     sum += (a % 10)
#     a//=10
#     c+=1
# print("count = ", c)
# print("sum = ", sum)


# for x in range(15,100,15):
#     print(x)


# n = input("Enter the number : ")
# while n != "Quit":
#     num = int(n)
#     print("Positive") if num % 2 == 0 else print("Negative")
#     n = input("Enter the number : ")



# def calculator(a,b,operand):
#     if operand == "+":
#         return a + b
#     elif operand == "-":
#         return a - b
#     elif operand == "*":
#         return a * b
#     elif operand == "/":
#         return a / b
#     elif operand == "%":
#         return a % b
#     elif operand == "//":
#         return a // b
#     else:
#         return "Unknown operand"

# a = int(input("Enter the numner "))
# b = int(input("Enter the number "))
# operand = input("Enter the operand ")
# print(calculator(a,b,operand))





# def isPrime(n):
#     if n <= 1:
#         return False
#     if n == 2 or n == 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False

#     for i in range(5, int(n**0.5) + 1, 6):
#         if n % i == 0 or n % (i + 2) == 0:
#             return False

#     return True

# n = int(input("Enter the number: "))
# print("Prime") if isPrime(n) else print("Not Prime")






# import random
# system = random.randint(1, 10)
# n = int(input("Enter the number (1-10): "))
# c = 1
# while n != system:
#     if n < system:
#         print("Too low !!!!!")
#     else:
#         print("Too high !!!")
#     n = int(input("Enter the number again: "))
#     c += 1
# print("Correct guess!!!!")
# print("You guessed it on", c, "th try")













    


    