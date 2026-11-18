#Write a Python program to find the second-smallest number in a List.
l = [3,8,9,52,1]
s = l[0]
m = []
for i in l:
    if s >i:
        s = i
m.append(s)
l.remove(s)
s = l[0]
for j in l:
    if s > j:
        s = j
m.append(s)
print(m)