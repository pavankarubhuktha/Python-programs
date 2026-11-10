#3. Write a program to handle exceptions with Nested Try.
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