# s = input("Enter the string : ")
# rev = ""
# for ch in s:
#     rev = ch + rev
# print("Palindrome") if rev == s else print("Not Palindrome")
# # or 
# print("Palindrome") if s == s[::-1] else print("Not Palindrome")


# l = [10,20,30,40,50,60,70,80,90]
# avg = 0
# for x in l:
#     avg += x
# print("avg = ", avg/len(l))


# list1 = list(map(int, input("Enter the first list of integers: ").split()))
# list2 = list(map(int, input("Enter the second list of integers: ").split()))
# i,j,k=0,0,0
# res=[]
# while i<len(list1) and j<len(list2):
#     if list1[i] == list2[j]:
#         res.append(list1[i])
#         i+=1
#         j+=1
#     elif list1[i] < list2[j]:
#         res.append(list1[i])
#         i+=1
#     else:
#         res.append(list2[j])
#         j+=1
# while i<len(list1):
#     res.append(list1[i])
#     i+=1
# while j<len(list2):
#     res.append(list2[j])
#     j+=1
# print(res)




# tup = (1, 5, 6, 8, 9, 4, 7, 2, 3)
# even = []
# odd = []
# for x in tup:
#     even.append(x) if x % 2 == 0 else odd.append(x)
# even = tuple(even)
# odd = tuple(odd)
# print("Even tuple =", even)
# print("Odd tuple =", odd)




# students = {
#     "alex": 78,
#     "bob": 77,
#     "costa": 67
# }
# while True:
#     print("\n--- Student Marks Menu ---")
#     print("A - Add a student")
#     print("B - Update marks")
#     print("C - Search for a student")
#     print("D - Display all students and marks")
#     print("E - Exit")
#     choice = input("Enter your choice: ").strip().upper()
#     if choice == 'A':
#         name = input("Enter the student name: ").strip()
#         if name in students:
#             print("Student already exists!")
#         else:
#             try:
#                 marks = int(input("Enter the marks: "))
#                 students[name] = marks
#                 print("Student added successfully!")
#             except ValueError:
#                 print("Please enter valid integer marks.")
#     elif choice == 'B':
#         name = input("Enter the student name: ").strip()
#         if name in students:
#             try:
#                 marks = int(input("Enter the updated marks: "))
#                 students[name] = marks
#                 print("Marks updated successfully!")
#             except ValueError:
#                 print("Please enter valid integer marks.")
#         else:
#             print("Student not found!")
#     elif choice == 'C':
#         name = input("Enter the student name to search: ").strip()
#         if name in students:
#             print(f"{name}: {students[name]} marks")
#         else:
#             print("Student not found!")
#     elif choice == 'D':
#         if students:
#             print("\nStudent Name - Marks")
#             for name, marks in students.items():
#                 print(f"{name} - {marks}")
#         else:
#             print("No students available.")
#     elif choice == 'E':
#         print("Exiting the program...")
#         break
#     else:
#         print("Invalid choice! Please select A, B, C, D, or E.")



# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# dict = {}
# for ch in words:
#     dict[ch] = len(ch)
# print(dict)



# s = input("Ente rthe string with spaces : ")
# x = 0
# for ch in s:
#     if ch == " ":
#         x+=1
# print("Space in the string are ", x)






# list1 = list(map(int, input("Enter the first list: ").split()))
# list2 = list(map(int, input("Enter the second list: ").split()))
# set1 = set(list1)
# set2 = set(list2)
# if set1.isdisjoint(set2):
#     print("Lists share no common elements")
# else:
#     print("Lists share common elements")



# l = [1,2,2,2,5,5,8,7,9,3,6,6]
# seen = set()
# duplicates = set()
# for x in l:
#     if x in seen:
#         duplicates.add(x)
#     else:
#         seen.add(x)
# print("Duplicate elements = ", duplicates)






# str = input("Ente rht estring : ")
# seen = set()
# for ch in str:
#     if ch not in seen:
#         seen.add(ch)
# print(seen, len(seen))
        