#13. Write a Python program to find repeated items in a tuple.
t1 =[1,5,8,6,7]
t2 =[1,5,9,8,10]
m = []
for i in t1:
    if i in t2:
        m.append(i)

print(m)