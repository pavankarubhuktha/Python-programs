n = int(input("enter: "))
a = []
for i in range(n):
    x = int(input("enter no: "))
    a.append(x)
d = a[0]
temp = 0
for i in range(n):
    for j in range(i+1,n):
        if (a[i] < a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)