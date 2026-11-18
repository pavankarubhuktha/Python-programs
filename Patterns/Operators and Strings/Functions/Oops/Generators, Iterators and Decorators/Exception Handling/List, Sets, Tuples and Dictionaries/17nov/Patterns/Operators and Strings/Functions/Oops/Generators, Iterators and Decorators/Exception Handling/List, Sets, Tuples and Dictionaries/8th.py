#Write a Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers and use the Python set.
s = {2,5,6,8,4}
p = 0
m = []
for i in s:
    for j in s:
        if i<j:
            product = i * j
            if product > p:
             p = product
             m = [i,j]
 
print(m)