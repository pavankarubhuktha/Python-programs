#4. What are all the different approaches to reading files?
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

with open("file_1", "r") as f1:
    for line in f1:
        print(line, end="")