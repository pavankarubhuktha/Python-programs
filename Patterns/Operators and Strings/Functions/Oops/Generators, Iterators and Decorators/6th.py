#Create a retry decorator that attempts to execute a function multiple times if it fails.

def deco(func):
    def wrapper():
        for i in range(3):
            try:
                return func()
            except Exception as e:
                print(f"attemt {i+1} failed: ")
        print("all three attempts are fail")
    return wrapper
@deco
def pavan():
    print("hey buddy")
    raise ValueError("something went worng")
pavan()