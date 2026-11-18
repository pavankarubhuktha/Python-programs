def count_letters(string):
    u = 0  # Uppercase counter
    l = 0  # Lowercase counter

    for char in string:
        if char.isupper():
            u += 1
        elif char.islower():
            l += 1

    print("No. of uppercase characters:", u)
    print("No. of Lower-case Characters:", l)


sample = "The quick Brown Fox"
count_letters(sample)
