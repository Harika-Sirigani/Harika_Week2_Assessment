class Shape:
    def area(self):
        pass

class Square():
    
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side * self.side
        
class Triangle():
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return  0.5*self.base*self.height
 
 
obj = Triangle(10,20)
print("Area of triangle :",obj.area()) 

obj=Square(10)
print("Area of square :",obj.area()) 
    