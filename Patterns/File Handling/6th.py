#6. Read the count of lines in a file?
count = 0
with open("largefile","r") as largefile:
    for lines in largefile:
        count = count + 1
print(count)