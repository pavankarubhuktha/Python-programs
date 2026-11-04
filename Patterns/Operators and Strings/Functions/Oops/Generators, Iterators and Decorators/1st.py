#1.​ Create a generator function that yields Fibonacci numbers up to a specified limit.
def gen():
    n = int(input("enter: "))
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        yield a
        a = b
        b = c
for i in gen():
    print(i,end=" ")
