n = int(input("enter: "))
a=[]
d = 0
for i in range(n):
    x = int(input("enter the no: "))
    a.append(x)
for i in range(n-1):
    if(a[i] == a[i+1]):
        d += 1
if(d == 0):
    print("no dup")
else:
    print("{} dup val" . format(d))