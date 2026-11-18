#Program to Show Use of Super Keyword in Class

class Father:
    def bike(self):
        print("hero honda")
class Son(Father):
    def bike(self):
        super().bike()
def display(obj):
 obj.bike()


obj = Son()
display(obj)