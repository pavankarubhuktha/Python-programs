n = int(input("enter: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print(" " , end=" ")
    for j in range(i-1):
        print(" *" , end=" ")
    print()