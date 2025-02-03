class Electronics:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
        
    def shows(self):
        print(f" {self.brand} price is {self.price}")
        
class MobileDevices(Electronics):
    def __init__(self,brand,price,battery):
        self.battery = battery
        self.brand = brand
        self.price = price
        
    def display(self):
        super().shows()
        print(f"Battery life is {self.battery}")
        
class SmartPhone(MobileDevices):
    def __init__(self,brand,price,battery,camera_quality):
        self.brand = brand
        self.price =price
        self.battery = battery
        self.camera_quality =camera_quality
        
    def show(self):
        print(f"The quality of camera is {self.camera_quality}")
        
        
smart = SmartPhone("OnePlus",35000,6,12)
smart.shows()
smart.display()
smart.show()

        
