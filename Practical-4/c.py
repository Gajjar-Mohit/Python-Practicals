# # declaration of findMax function
# def findMax(a, b):
#     if a < b:
#         return b
#     else:
#         return a

# for i in range(3):
#     # taking multiple input using split
#     x, y, z = (input("Enter three nubers:").split())
#     # Printing the maximum value
#     print("Maximum Number is :", findMax(x, findMax(y, z)))

# Declaring function count
def count(fName, lName):

    cntUpper = 0
    cntLower = 0
    for i in fName:
        # checking character is in upper or not
        if (i.isupper()):
            cntUpper += 1
        else:
            cntLower += 1

    print("\nUpper case in fname:", cntUpper, "\nLower case in fname:", cntLower)
    cntUpper = 0
    cntLower = 0
    for i in lName:
        # check character is in lower or not
        if (i.islower()):
            cntLower += 1
        else:
            cntUpper += 1

    print("\nUpper case in lname:", cntUpper, "\nLower case in lname: ", cntLower ,"\n")
# Taking input from user
fName, lName = input("Enter your full name: ").split()
# calling the count function
count(fName, lName)
