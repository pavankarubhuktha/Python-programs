n = int(input("enter: "))
a = []
for i in range(n):
    x = int(input("enter no: "))
    a.append(x)
l = a[0]
s = a[0]
for i in range(n):
    if (a[i] < s):
        s = a[i]
    elif (a[i] > l):
        l = a[i]
print(l)
print(s)