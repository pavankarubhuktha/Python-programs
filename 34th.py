n = int(input("Enter size: "))
a = []

for i in range(n):
    x = int(input("Enter no: "))
    a.append(x)

for i in range(n):
    if a[i] % 2 != 0:
        print(a[i])
print("Odd numbers:")

for i in range(n):
    if a[i] % 2 == 0:
        print(a[i])
print("Even numbers:")
