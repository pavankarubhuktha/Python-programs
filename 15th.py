i = int(input("enter: "))
total = 0
skip = False
while i>0:
    d = i % 10
    if not skip:
        total += d
    skip = not skip
    i = i // 10
print(total)