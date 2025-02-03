from abc import ABC,abstractmethod

class Icalculator(ABC):
     @abstractmethod
     def add(self,a,b):
         pass
     @abstractmethod
     def subtract(self,a,b):
         pass
     @abstractmethod
     def mul(self,a,b):
         pass
     @abstractmethod
     def divide(self,a,b):
         pass
     
class BasicCalculator:
    def add(self,a,b):
        print("ADD:",a+b)
    def subtract(self,a,b):
        print("SUBTRACT:",a-b)
    def mul(self,a,b):
        print("MUL:",a*b)
    def divide(self,a,b):
        print("DIVIDE:",a/b)
    
calc = BasicCalculator()
calc.add(5,10)
calc.subtract(20,10)
calc.mul(10,20)
calc.divide(20,10)
