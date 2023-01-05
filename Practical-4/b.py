a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
c = int(input('Enter number 3: '))


def find_max(a, b, c):
    if (a > b):
        return a
    elif (b < c):
        return c
    else:
        return b

print(find_max(a, b, c), 'is Max')
