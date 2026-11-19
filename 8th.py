n = 5
previous = []

for i in range(n):

    current = [1]

    for j in range(1, len(previous)):
        current.append(previous[j-1] + previous[j])

    if i > 0:
        current.append(1)

    for j in range(n-i-1):
        print("  ", end="")

    for num in current:
        print(num, end="   ")

    print()

    previous = current