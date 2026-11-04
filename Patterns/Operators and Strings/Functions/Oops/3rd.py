#Create a subclass called HRManager that overrides the work() method andadds a new method called addEmployee().
class Company:
    def work(self):
        print("employee of this company")
class HRManager(Company):
    def work(self):
        print("he has to compleate the given task")
    def addEmployee(self):
        print("he is new")
obj = HRManager()
obj.work()
obj.addEmployee()
