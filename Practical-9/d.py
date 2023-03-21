with open("example.txt", "r") as file:
    contents = file.read()
    words = contents.split()
    for i in range(5):
        print(words[i])
