
def add(num1 , num2):
    return num1 + num2

def sub(num1 , num2):
    return num1 - num2

list1 = [6, 5, 3, 9]
list2 = [0, 1, 7, 7]

addition = map(add, list1, list2)
subtraction = map(sub, list1, list2)

result = list(zip(addition, subtraction))

print(result)