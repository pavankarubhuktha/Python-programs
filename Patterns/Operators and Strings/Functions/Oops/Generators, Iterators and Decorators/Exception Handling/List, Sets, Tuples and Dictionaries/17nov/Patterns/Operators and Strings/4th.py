n = int(input("Enter size: "))
a = []

for i in range(n):
    x = int(input("Enter no: "))
    a.append(x)
sum = 0
for i in range(n):
    if a[i] >= 0:
        sum += a[i]
print("sum: ",sum)
sub = a[0]
for i in range(1,n):
    if a[i] >= 0:
        sub = sub - a[i]
print("sub: ",sub)
mod = a[0]
for i in range(n):
    if a[i] >= 0:
        mod %= a[i]
print("mod: ",mod)
div = a[0]
for i in range(n):
    if a[i] >= 0:
        div /= a[i]
print("div: ",div)