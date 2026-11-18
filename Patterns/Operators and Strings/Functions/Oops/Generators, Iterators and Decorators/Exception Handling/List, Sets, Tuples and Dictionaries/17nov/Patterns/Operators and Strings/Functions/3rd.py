def palindrome(string):
    if string == string[: : -1]:
        print("same")
    else:
        print("not")
sample = input("enter")
palindrome(sample)