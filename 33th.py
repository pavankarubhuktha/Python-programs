n = int(input("enter: "))
a = []
for i in range(n):
    x = int(input("enter no: "))
    a.append(x)
sum = 0
for i in range(n):
    sum += a[i]
    
print(sum)