s = int(input("enter: "))
big = 0
while s > 0:
    l = s % 10
    if l > big:
        big = l
    else: 
         s = s // 10
print(big)
    
