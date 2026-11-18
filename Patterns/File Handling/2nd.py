#2. Read from data into a file in Different ways?
f1 = open("file_1","r")
print(f1.read())
f1.close()

with open("file_1","r") as f1:
    print(f1.read())

f1 = open("file_1","r+")
print(f1.read())
f1.close()

f1 = open("file_1","r")
print(f1.readline())
f1.close()

f1 = open("file_1","r")
print(f1.readlines())
f1.close()
