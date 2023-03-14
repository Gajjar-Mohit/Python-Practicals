# taking marks from the user
# print('-------------------------------------')
# print('Enter Points you secured below.')
# print('-------------------------------------')
# mathsPoints = int(input('Points for Maths: '))
# javaPoints = int(input('Points for Java: '))
# dcnPoints = int(input('Points for DCN: '))
# mcoPoints = int(input('Points for MCO: '))
# print('-------------------------------------')
# print('Enter Credits you secured below.')
# print('-------------------------------------')
# mathsCredit = int(input('Credits for Maths: '))
# javaCredit = int(input('Credits for Java: '))
# dcnCredit = int(input('Credits for DCN: '))
# mcoCredit = int(input('Credits for MCO: '))

# maths = mathsCredit * mathsPoints
# java = javaCredit * javaPoints
# dcn = dcnCredit * dcnPoints
# mco = mcoCredit * mcoPoints

# sum = maths + java + dcn + mco

# sumOfCredits = mathsCredit+javaCredit+dcnCredit+mcoCredit

# sgpa = sum/sumOfCredits

# print('=====================================')
# print('you scored', sgpa)
# print('=====================================')


# # declaration of lambda function

# def Square(x): return x*x
# # declaration of square function
# def squareOfList(list):


#     for i in range(5):
#         list[i] = Square(list[i])
#         return l

# l = []
# # taking list input
# for i in range(5):
#     l.append(int(input("Enter a number:")))

# print("\nList:", l, "\n")
# print("New list:", squareOfList(l), "\n")



# def printTable(number):
#     for i in range(1, 11):
#         print(number, " x ",i, " = ",(number*i))
# #Taking input from user
# n = int(input("Table of number: "))
# #printing table of inputted number
# printTable(n)

# Creating a function which calculates sum of list elements

# def sumOfList(list):
#     sum = 0
#     for i in list:
#         sum += int(i)
#     return sum
# # Taking length of list
# n = int(input("\nEnter length of list:"))
# print()
# l = []
# # Taking a list input from the user
# for i in range(n):
#     l.append(int(input("Enter number:")))
# # Printing the sum of list elements
# print("\nSum of list elements is", sumOfList(l), "\n")



# Declaring a comprehensive
def comprehension():
    ListOfEven = []
    ListOfOdd = []
    List = []
    # separating even and odd numbers
    for i in range(1, 51):
        if i % 2 == 0:
            ListOfEven.append(i)
        else:
            ListOfOdd.append(i)
    for i in range(1, 101):
        if i % 5 == 0:
            List.append(i)

    return ListOfEven, ListOfOdd, List
l1, l2, l3 = comprehension()
# Printing list items.
print("\nEven List:", l1, "\n\nOdd List:", l2, "\n\nList:", l3,
"\n")