n= int(input("enter: "))
m= int(input("enter: "))
for i in range(n,m+1,1):
    sum = 0
    for j in range(1,i+1,1):
        if i % j == 0 and i != j:
            sum += j
    if sum == i:
        print(i)