#Write a Python program to remove an item from a set if it is present in the set.
s = {1,2,3,4,5}
r = 5
if r in s:
   s.remove(r)
print(s)

