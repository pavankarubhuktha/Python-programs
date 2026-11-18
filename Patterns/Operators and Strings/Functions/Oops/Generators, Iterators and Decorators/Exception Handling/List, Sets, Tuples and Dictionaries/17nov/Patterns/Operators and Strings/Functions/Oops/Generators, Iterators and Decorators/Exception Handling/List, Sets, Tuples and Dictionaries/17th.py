#Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples,
# Original list of tuples: [(1, 2), (2, 3), (3, 4)]
# Sum of all the elements of each tuple [3, 5, 7]
l = [(1, 2), (2, 3), (3, 4)]
s = []
for i in l:
    sum = 0
    for j in i:
        sum = sum + j
    s.append(sum)
print(s)