#Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa.
s1 = {1,3,85,9,8}
s2 = {8,7,2,25,6}
m = []
for i in s1:
    if i not in s2:
        m.append(i)
for j in s2:
    if j not in s1:
        m.append(j)
print(m)