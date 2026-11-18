#1. Write data into a file in Different ways?
f1 = open("file_1","w")
f1.write("hi")
f1.close()
f1 = open("file_1","r")
print(f1.read())

with open("file_1","r+") as f1:
    f1.write("hello")
with open("file_1","r") as f1:
    print(f1.read())

f1 = open("file_1","r+")
f1.write("hey,how are you")
f1 = open("file_1","r")
print(f1.read())

f1 = open("file_1", "a")
f1.write("\niam fine")
f1.close()
f1 = open("file_1", "r")
print(f1.read())
f1.close()

f1 = open("file_1", "w")
data = ["Hello\n", "Python\n", "Programming"]
f1.writelines(data)
f1.close()
f1 = open("file_1", "r")
print(f1.read())
f1.close()