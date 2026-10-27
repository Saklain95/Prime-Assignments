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




