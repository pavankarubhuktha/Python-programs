#Program to Create an Interface
#duck typing
#overriding
class Father:
    def bike(self):
        print("hero honda")
class Son():
    def bike(self):
        print("KTM")

obj = Son()
obj.bike()

#abstract

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        print("mewon")
class Dog(Animal):
    def sound(self):
        print("bark")
ob1 = Dog()
ob2 = Cat()
ob1.sound()
ob2.sound()