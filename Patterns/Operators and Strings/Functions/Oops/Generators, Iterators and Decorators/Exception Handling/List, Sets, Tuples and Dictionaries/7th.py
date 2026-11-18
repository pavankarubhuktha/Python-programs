#Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.
l = [2, 4, 6, 8, 10]
target = 12
m = []
for i in l:
    for j in l:
        if i < j and i + j == target:
            m.append((i, j))
print(m)