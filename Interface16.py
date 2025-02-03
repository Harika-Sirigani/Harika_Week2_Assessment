from abc import ABC,abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth = breadth
        
    def calculate_area(self):
        return self.length*self.breadth
    
class Circle:
    def __init__(self,radius):
        self.radius=radius
        
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

r = Rectangle(5,10)
print(f"Area of rectangle : {r.calculate_area()}")
c=Circle(5)
print(f"Area of circle : {c.calculate_area()}")