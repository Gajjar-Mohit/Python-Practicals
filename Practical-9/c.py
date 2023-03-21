
with open("Practical-9/example.txt", "w") as file:
    file.write("This is an example file.\nIt contains some text.")

with open("Practical-9/example.txt", "r") as file:
    contents = file.read()
    print(contents)
