n = int(input("enter: "))
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum += i
if n == sum:
    print("perfert no")
else:
    print("not perfert no")