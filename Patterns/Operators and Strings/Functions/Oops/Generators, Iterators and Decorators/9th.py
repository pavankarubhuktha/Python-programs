n = 4
for i in range(1,n+1):
    print("  " * (n-i),end="")
    for j in range(n-i+1,n+1):
        print(j,end=" ")
    for k in range(n-1,n-i,-1):
        print(k,end=" ")
    print()
for i in range(n-1,0,-1):
    print("  " * (n-i),end="")
    for j in range(n-i+1,n+1):
        print(j,end=" ")
    for k in range(n-1,n-i,-1):
        print(k,end=" ")
    print()