def sum_no(n):
    if n == 0:
        return 0
    return n % 10 + sum_no(n // 10)
n = int(input("enter"))
print(sum_no(n))