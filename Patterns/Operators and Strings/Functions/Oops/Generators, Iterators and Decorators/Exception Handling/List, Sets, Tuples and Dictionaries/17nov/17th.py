n = int(input("enter no: "))
d = int(input("enter dig: "))
coun=0


while n > 0:
    k = n % 10


    if k == d:
        coun += 1

    n = n // 10
if coun > 1:
    print("equal")
else:
    print("not equal")
