def multi(number):
    return number * 2
number = [1,2,3,4,5]
result = map(multi,number)
print(list(result))