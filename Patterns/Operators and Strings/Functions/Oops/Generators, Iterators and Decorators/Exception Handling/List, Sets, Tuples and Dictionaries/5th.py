#Write a Python program to find elements in a given set that are not in another set.
s1 = {1,3,85,9,8}
s2 = {8,7,2,25,6}
m = []
for i in s1:
    if i not in s2:
        m.append(i)
print(m)