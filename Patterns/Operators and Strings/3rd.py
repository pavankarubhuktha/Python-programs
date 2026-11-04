n = int(input("enter: "))
a = []
for i in range(n):
    x = int(input("enter no: "))
    a.append(x)
print("even no")
sum = 0
for i in range(n):
    if a[i] % 2 == 0:
        sum += a[i]
print(sum)
