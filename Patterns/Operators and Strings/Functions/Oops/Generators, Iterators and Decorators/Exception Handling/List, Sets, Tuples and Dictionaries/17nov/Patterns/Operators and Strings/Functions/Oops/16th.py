#Program to Show Usage of Access Modifier
class Student:
    def __init__(self):
        self.name = "pavan"
        self._age = 22
        self.__marks = 80
    def display(self):
        print("name",self.name)
        print("age",self._age)
        print("marks",self.__marks)
obj = Student()
obj.display()