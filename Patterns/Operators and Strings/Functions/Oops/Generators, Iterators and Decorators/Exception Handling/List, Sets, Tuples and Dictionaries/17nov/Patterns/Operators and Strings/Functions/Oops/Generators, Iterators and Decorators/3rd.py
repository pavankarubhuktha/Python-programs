#Write a generator that produces an infinite sequence of prime numbers.

def gen():
    num = 2

    while True:
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count += 1

        if count == 2:
            yield num

        num += 1


obj = gen()

for i in range(10):
    print(next(obj))

