n = int(input("enter: "))
a = []
for i in range(n):
    x = int(input("enter no: "))
    a.append(x)
for i in range(n-1,-1,-1):
    print(a[i])