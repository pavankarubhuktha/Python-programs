##
n = int(input("Enter a number: "))
d = int(input("Enter the digit to find: "))
coun=0


while n> 0:
    k = n % 10


    if k == d:
      coun += 1
    n = n // 10
print(coun)
