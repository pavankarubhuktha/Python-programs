#Single Inheritance
class Pavan:
    def bike(self):
        print("hero honda")
class Phani(Pavan):
    def car(self):
        print("varna")
obj = Phani()
obj.car()
obj.bike()
#Multiple Inheritance
class Tenth:
    def tp(self):
        print("10th pass")
class Inter:
    def ip(self):
        print("inter pass")
class Btech(Tenth,Inter):
    def bp(self):
        print("Btech pass")
obj = Btech()
obj.tp()
obj.ip()
obj.bp()
#Multilevel Inheritance
class Grandfather:
    def house(self):
        print("grandfather has house")
class Father(Grandfather):
    def shop(self):
        print("Father has shop")
class Son(Father):
    def flat(self):
        print("son has flat")

obj= Son()

obj.house()
obj.shop()
obj.flat()

#Hierarchical Inheritance
class Tesla:
    def funds(self):
        print("got funds")
class Teslacar(Tesla):
    def Newcar(self):
        print("working new model")
class Spacex(Tesla):
    def prj(self):
        print("working on new project")
obj1= Teslacar()
obj2= Spacex()

obj1.funds()
obj1.Newcar()
obj2.funds()
obj2.prj()

#Hybrid Inheritance
class Grandfather:
    def house(self):
        print("grandfather has house")
class Father():
    def shop(self):
        print("Father has shop")
    def Car(self):
        print("father")
class Son(Father,Grandfather):
    def flat(self):
        print("son has flat")
class Son2(Father,Grandfather):
    def flat(self):
        print("son has flat")

obj=Son()
obj2= Son2()

obj.house()
obj.shop()
obj.flat()
obj2.Car()
obj2.house()
obj2.flat()