n = int(input("enter: "))
s = 0
for i in range(1,n+1,1):
    
    s += 1/i**(n-1)
print(s)