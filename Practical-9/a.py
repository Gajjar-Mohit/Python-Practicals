with open("Practical-9/input.txt", "r") as input_file, open("Practical-9/odd.txt", "w") as odd_file, open("Practical-9/even.txt", "w") as even_file:
    for line in input_file:
        num = int(line.strip())
        if num % 2 == 0:
            even_file.write(str(num) + "\n")
        else:
            odd_file.write(str(num) + "\n")
