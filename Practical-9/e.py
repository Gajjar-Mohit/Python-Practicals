with open("Practical-9/triangle.txt", "w") as file:
    for i in range(1, 6):
        line = "*" * i
        file.write(line + "\n")
        print(line)