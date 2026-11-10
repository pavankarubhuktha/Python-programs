#2. Write a program to handle exceptions with Multiple Catch Block.
a = 10
b = 0

try:
    result = a / b
    print(result)

except ZeroDivisionError as e:
    print("This is not possible")

except ValueError as e:
    print("This value is not given")

except Exception as e:
    print("Some other error occurred")