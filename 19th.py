n = input("enter: ")
even = 0
odd = 0
for i in range(0,len(n),1):
    if int(n[i]) % 2 == 0:
        even += int(n[i])
    else:
        odd += int(n[i])
print("odd no are", odd)
print("even no are", even)