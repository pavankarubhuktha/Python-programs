n = input("enter")
a = n.split()
for i in a:
    x = chr(ord(i[0]) - 1) + i[1:]
   
    print(x,end=" ")

