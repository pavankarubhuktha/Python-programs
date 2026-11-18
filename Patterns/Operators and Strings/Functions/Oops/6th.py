#overriding
class Father:
    def bike(self):
        print("hero honda")
class Son(Father):
    def bike(self):
        print("KTM")

obj = Son()
obj.bike()