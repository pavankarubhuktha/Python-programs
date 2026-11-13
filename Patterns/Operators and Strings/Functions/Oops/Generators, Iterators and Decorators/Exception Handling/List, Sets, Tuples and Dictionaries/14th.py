#14. Write a Python program to reverse a tuple.
t1 =[1,5,8,6,7]
m = []
for i in range(len(t1),0,-1):
    m.append(t1[i-1])
m = tuple(m)
print(m)
