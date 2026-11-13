#Write a Python program to convert a given tuple of positive integers into an integer,
# Original tuple: (1, 2, 3)
# Expected output: 123
t = (1,2,3)
m = ""
for i in t:
    #n = int(i)
    m = m + str(i)
    #m = m * 10 + n
print(int(m))