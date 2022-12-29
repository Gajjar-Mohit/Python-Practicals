# creating the empty list
testList = []
noOfEle = int(input("Enter numner of elements: "))

# storing the elemnts in the list
for i in range(noOfEle):
    ele = input("Enter the element: ")
    testList.append(ele)

print(testList)

# extending the list
extendedEle = input("Enter the elemnt to extend the list: ")
testList.extend(extendedEle)


