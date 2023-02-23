#addition
def addition(a,b):
    return a+b

#subtraction
def subtraction(a,b):
    return a-b

#multiplication
def multiplication(a,b):
    return a*b

#division
def division(a,b):
    return a/b

#factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#fibonacci series
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)