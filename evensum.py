n = int(input("enter:"))
total = 0
for i in range(1,n+1):
    if i % 2 == 0:
        total = i + total
        print("sum:",total)