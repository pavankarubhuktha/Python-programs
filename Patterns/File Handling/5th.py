#5. Read a Specific Line from a File?
with open("largefile","r") as largefile:
    lines = largefile.readlines()
    print(lines[7])