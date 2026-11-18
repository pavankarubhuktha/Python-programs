#Write a program to get the Largest Number in the List.
l = [11,25,40,35,80]
large = l[0]
for i in l:
    if large < i:
        large = i
print(large)