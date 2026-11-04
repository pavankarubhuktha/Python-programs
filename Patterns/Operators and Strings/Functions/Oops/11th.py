#Write a Java program that creates a class hierarchy for employees of a company. The base class should be Employee, with subclasses Manager,Developer, and Programmer. Each subclass should have properties such as name, address, salary, and job title.Implement methods for calculating bonuses, generating performance reports, and managing projects.
class Employee:
    def __init__(self,name,address,salary,jobtitle):
        self.name = name
        self.address = address
        self.salary = salary
        self.jobtitle = jobtitle
    def calculatingbonuses(self):
        print("bonuses: ",self.salary*0.10)
    def generatingperformancereports(self):
        print(self.name , "is performing well")
    def managingprojects(self):
        print(self.name , "is managing well")
class Manager(Employee):
    def calculatingbonuses(self):
        print("bonuses: ",self.salary*0.10)
    def generatingperformancereports(self):
        print(self.name , "is performing well")
    def managingprojects(self):
        print(self.name , "is managing well")
class Developer(Employee):
    def calculatingbonuses(self):
        print("bonuses: ",self.salary*0.10)
    def generatingperformancereports(self):
        print(self.name , "is performing well")
    def managingprojects(self):
        print(self.name , "is managing well")
class programmer(Employee):
    def calculatingbonuses(self):
        print("bonuses: ",self.salary*0.10)
    def generatingperformancereports(self):
        print(self.name , "is performing well")
    def managingprojects(self):
        print(self.name , "is managing well")
m = Manager("ava","viza",50000,"manager")
d = Developer("pava","iza",50000,"developer")
p = programmer("kumarava","viz",50000,"programmer")

print("-----manager-------")
m.calculatingbonuses()
m.generatingperformancereports()
m.managingprojects()
print("\n------deloper-------")
d.calculatingbonuses()
d.generatingperformancereports()
d.managingprojects()


print("\n----- PROGRAMMER -----")
p.calculatingbonuses()
p.generatingperformancereports()
p.managingprojects()