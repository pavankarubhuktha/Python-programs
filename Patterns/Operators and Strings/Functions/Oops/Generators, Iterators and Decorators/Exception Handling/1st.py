#1. Write a program to handle exceptions with Try-Catch Block.
a = 4
b = 0

try:
    result = a/b
    print(result)
except Exception as e:
    print("this is not possable")