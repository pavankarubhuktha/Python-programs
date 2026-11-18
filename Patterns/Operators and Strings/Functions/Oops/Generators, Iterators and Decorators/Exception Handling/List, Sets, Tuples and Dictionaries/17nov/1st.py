n = 10
for i in range(1,n+1):
    for j in range(i,n):
        print(j,end=" ")
    for k in range(1,i):
        print(k,end=" ")
    print()