# # creating the empty list
# testList = []
# noOfEle = int(input("Enter numner of elements: "))

# # storing the elemnts in the list
# for i in range(noOfEle):
#     ele = input("Enter the element: ")
#     testList.append(ele)

# print(testList)

# # extending the list
# extendedEle = input("Enter the elemnt to extend the list: ")
# testList.extend(extendedEle)

# # Taking Principal amount from user
# p = int(input("Enter the Principal amount: "))
# #Taking Rate of Interest from user
# r = int(input("Enter the rate: "))
# #Taking number of years from user
# n = int(input("Number of years: "))
# #Calculating simple interest rate
# i = (p*r*n)/100
# #Printing the simple interest rate
# print("Simple Interest for given data is: " , i)

# Creation and initialization of list l
l = [1, 5, 2, 3, 4, 9, 6]
# Printing list l
print("list l:", l)
# append() will add a new element at the end of the list
l.append(8)
l.append(7)
print("Updated list after append():", l)
# printing list l with for loop
# for i in l:
# print(i)
# extend() method will add multiple elements in the list
l.extend([11, 15, 12, 13])
print("Updated list after extend():", l)
# Remove() will remove specified element
l.remove(11)
l.remove(13)
l.remove(12)
l.remove(15)
print("Updated list after remove():", l)
# Reverse() will reverse all elements in list
l.reverse()
print("reverse() the list:", l)
# Printing list in ascending order
l.sort()
