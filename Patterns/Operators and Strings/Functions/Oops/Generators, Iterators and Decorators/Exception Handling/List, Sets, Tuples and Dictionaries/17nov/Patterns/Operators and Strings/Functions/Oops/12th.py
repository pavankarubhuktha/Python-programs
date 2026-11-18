#Write a program to explain Dynamic Binding.
class Father:
    def bike(self):
        print("hero honda")
class Son(Father):
    def bike(self):
        print("KTM")
def display(obj):
 obj.bike()

obj = Son()
display(obj)