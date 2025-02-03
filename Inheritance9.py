class Car:
    def move(self):
        return "This is car"
    
class Airplane:
    def move(self):
        return "This is Airplane"
    
class FlyingCar(Car,Airplane):
    def move(self):
        return f"{Car.move(self)} \n {Airplane.move(self)}"
    
obj = FlyingCar()
print(obj.move())