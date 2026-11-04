n = int(input("enter: "))
a=[]
for i in range(n):
    x = int(input("enter the no: "))
    a.append(x)

for i in range(n):
    count = 0
    for j in range(n):

        if (a[i] == a[j]):
            count += 1
print(a[i] ,"appears" , count, "times")