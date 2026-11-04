#Program to Show Use of This Keyword in Class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("name: ",self.name)
        print("age: ",self.age)
obj = Person("pavan",22)
obj.display()
        