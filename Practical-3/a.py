# string operations
string1 = "This is the first string."
string2 = "This is the second string."

# reversing a string
def rev(s):
    string  = ""
    for i in string1:
        string = i + string
    return string
print(rev(string1))


# mering two strings
new  = string1 + string2
print(new)

# replacing the string
print(string1.replace("first", "Third"))


# finding the character in the string without using loops
print('i' in string1)


# spliting the string into different characters
string3 = "This is the first statement. This is the second statement. This is the third statement. This is the forth statement"
print(string3.split('.'))