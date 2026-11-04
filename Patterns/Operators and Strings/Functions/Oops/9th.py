#Program to Show Abstraction in Class
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