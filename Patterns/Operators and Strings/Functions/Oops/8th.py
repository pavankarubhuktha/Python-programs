#Create a subclass called Employee that adds a new method named getEmployeeId() and overrides the getLastName() method to include the employee's job title.
class Person:
    def getLastName(self):
        print("pavan")
class Employee(Person):
    def getEmployeeId(self):
        print("2200032954")
    def getLastName(self):
        print("pavan - software developer")
obj = Employee()
obj.getLastName()
obj.getEmployeeId()