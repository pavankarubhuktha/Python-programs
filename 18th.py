n = input("enter: ")
con = 0
for i in range(0,len(n),1):
    if i == 0 or i == len(n)-1:
        con += int(n[i])
print(con)