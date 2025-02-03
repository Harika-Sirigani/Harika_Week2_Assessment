from abc import ABC,abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    
class Car:
    def start_engine(self):
        print("Car is started")
    def stop_engine(self):
        print("Car is stopped")
        
class Bike:
    def start_engie(self):
        print("Bike is started")
    def stop_engine(self):
        print("Bike is stopped")
        
class Truck:
    def start_engine(self):
        print("Truck is started")
    def stop_engine(self):
        print("Truck is stopped")
        
b = Bike()
b.start_engie()
b.stop_engine()

c = Car()
c.start_engine()
c.stop_engine()

t = Truck()
t.start_engine()
t.stop_engine()