n = 5
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        if i == 1 or j == 0 or j == i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for j in range(i):
        if i == 1 or j == 0 or j == i-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()