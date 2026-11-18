#4. Write a program to execute a statement using Finally Block.
n = int(input("Enter: "))
m = int(input("Enter: "))

try:
    result = n / m
    print(result)

    try:
        result = n + c
        print(result)

    except NameError as e:
        print("The variable is not defined")

except ZeroDivisionError as e:
    print("This is not possible")
finally:
    print("Finally block is executed")