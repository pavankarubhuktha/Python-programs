n =1
for i in range(1,5):
    for j in range(i):
        print(n,end=" ")
        n += 1
    print()
for i in range(4,0,-1):
    s = i *( i-1)// 2 + 1
    for k in range(s,s+i):
        print(k,end=" ")
    print()