#11. Write a Python program to create a tuple with different data types.
m = []


a = int(input("Enter integer: "))
m.append(a)

b = input("Enter string: ")
m.append(b)

c = float(input("Enter float: "))
m.append(c)

d = input("Enter boolean (True/False): ")
m.append(d == "True")

m = tuple(m)
print(m)

