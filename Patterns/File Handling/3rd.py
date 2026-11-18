#3. Read a Large File?
with open("largefile","r") as largefile:
    for line in largefile:
        print(line,end="")
