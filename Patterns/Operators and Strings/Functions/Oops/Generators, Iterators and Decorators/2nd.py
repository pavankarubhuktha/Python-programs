#2.​ Implement a generator that reads a large file line by line without loading it entirely into memory.

def gen():

    with open("sample.txt", "r") as f:
        for line in f:
            print(line)
            yield line
for i in gen():
    print(i)
