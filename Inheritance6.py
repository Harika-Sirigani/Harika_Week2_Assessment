class Vehicle:
    def display(self):
        print('This is vehicle')
    
    
class Bike(Vehicle):
    def display(self):
        super().display()
        print("This is bike")
        
class Car(Vehicle):
    def display(self):
        print('This is car')
        
class ElectricCar(Car):
    def display(self):
        print("This is electricar")
        
obj1 = Car()
obj1.display()
obj2=Bike()
obj2.display()
obj3 = ElectricCar()
obj3.display()
