#7.​ Build a decorator to validate function arguments against specified criteria.
def validate(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Arguments must be integers")

        for key, value in kwargs.items():
            if not isinstance(value, int):
                raise ValueError(f"{key} must be an integer")

        return func(*args, **kwargs)

    return wrapper


@validate
def add(a, b):
    return a + b


print(add(10, 20))    
print(add(10, "20")) 