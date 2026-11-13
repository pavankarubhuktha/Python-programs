#Write a Python program to replace the last value of the tuples in a list [(10, 20,40), (40, 50, 60), (70, 80, 90)] Expected Output: [(10, 20, 100), (40, 50, 100),(70, 80, 100)].
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
m = []
for i in l:
    m.append((i[0],i[1],100))
print(m)
