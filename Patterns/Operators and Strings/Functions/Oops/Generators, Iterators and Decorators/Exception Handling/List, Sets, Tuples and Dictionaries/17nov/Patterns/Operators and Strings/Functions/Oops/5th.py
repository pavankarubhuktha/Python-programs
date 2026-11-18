#Program to Show Overloading of Methods in Class
class Pavan:
    def add(self,a,b=10):
        print("sum: ",a+b)
obj = Pavan()
obj.add(10)
obj.add(10,30)