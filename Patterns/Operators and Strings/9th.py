n = input("enter: ")
count = 0
alpha = 0
c = 0
v = 0
s = 0
for i in n:
    if i.isdigit():
        count += 1
    elif i.isalpha():
        alpha += 1
        if i.lower() in "aeiou":
            v += 1
        else:
            s += 1
    elif not i.isalnum() and not i.isspace():
        c += 1

print(count)
print(alpha)
print(c)
print(s)
print(v)