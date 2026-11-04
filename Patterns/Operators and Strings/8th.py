n = int(input("enter: "))
a = []

for i in range(n):
    x = int(input("enter no: "))
    a.append(x)
min = a[0]
max = a[0]
for i in a:
    if i < min:
        min = i

    elif i > max:
        max = i
print(min)
print(max)