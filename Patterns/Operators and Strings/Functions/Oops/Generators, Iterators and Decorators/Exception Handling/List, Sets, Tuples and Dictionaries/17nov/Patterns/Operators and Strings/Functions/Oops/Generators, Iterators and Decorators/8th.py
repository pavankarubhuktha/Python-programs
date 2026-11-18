#Create a class-based decorator that counts how many times a function is called.
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Function called {self.count} times")
        return self.func(*args, **kwargs)


@CountCalls
def greet(name):
    print("Hello", name)


greet("Alice")
greet("Bob")
greet("Charlie")

print("Total function calls:", greet.count)