#Remove Common Elements from two Lists.
l1 = [2,3,5,4,8]
l2 = [2,10,5,4,58]
s = []
for i in l1:
    if i not in l2:
        s.append(i)
for j in l2:
    if j not in l1:
        s.append(j)
print(s)