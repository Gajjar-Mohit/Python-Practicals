# Create an empty list
testList = []


# Add apple, orange, banana, pineapple, watermelon, kiwi in above created list

testList.append("apple")
testList.append("orange")
testList.append("banana")
testList.append("pineapple")
testList.append("watermelon")
testList.append("kiwi")

# Find length of the list
print(len(testList))

# Retrieve 4th element of list using positive index
print(testList[3])

# Retrieve 4th element of list using negative index
print(testList[-3])

# Add strawberry to the list
testList.append("strawberry")

# Unpacking the list such that A1 has 1st element of list A2 has 2nd element of list AL has last element of list and AR has all other element of list
a1, a2, 
a1 = testList[0]
print(a1)

a2 = testList[2]
print(a2)

al = testList.pop()
print(al)

ar = al
print(al)

# Retrieve the 2nd to 4th element of list
print(testList[2], testList[4])

# Find banana in list
find = "banana"
print(testList.__contains__(find))

# Find mango in list
find1 = "mango"
print(testList.__contains__(find1))

# Replace banana with mango
testList[2] = "mango"
print(testList)

# Remove last element of the list
testList.pop()

# Remove pineapple from the list
testList.remove("pineapple")

# Remove 2nd item of the list
testList.remove(2)

# Clear the list
testList.clear()
