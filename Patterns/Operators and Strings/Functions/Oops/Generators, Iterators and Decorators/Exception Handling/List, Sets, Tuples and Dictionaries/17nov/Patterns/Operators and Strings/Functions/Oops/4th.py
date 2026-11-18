#Program to Show Polymorphism in Class
class Tenth:
    def pas(self):
        print("he has pass 10th class")
class Inter:
    def pas(self):
        print("he has pass inter")
class Btech:
    def pas(self):
        print("he has pass Btech")
ob1 = Btech()
ob2 = Tenth()
ob3 = Inter()
ob2.pas()
ob3.pas()
ob1.pas()