#6. Write a program to handle exceptions with Throws Keyword.
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    else:
        print("Eligible to vote")

try:
    age = int(input("Enter your age: "))
    check_age(age)

except ValueError as e:
    print("Exception handled:", e)