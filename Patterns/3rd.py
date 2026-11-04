n = int(input("enter: "))
for i in range(1,n+1,2):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print(" *",end="")
    print()