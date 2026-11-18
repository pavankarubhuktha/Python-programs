#9. Write a Python program to find the maximum and minimum values in a set.
s = [1,5,6,8,9]
max = s[0]
min = s[0]
for i in s:
    if min > i:
        min = i
print(min)
for j in s:
    if max < j:
        max = j
print(max)
