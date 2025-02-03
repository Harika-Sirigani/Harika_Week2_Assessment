class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price =price
        self.stock = stock
        
    def display(self):
        return f"Product details : \n {self.name} price is {self.price} and stock is {self.stock}" 
        
    def check_availability(self,quantity):
        quantity=self.stock
        if requested_quantity <= quantity:
            return f"Quantity is available"
        else:
            return f"requested quantity of {self.name} is not available"
    
p = Product("Salt",60,100)
print(p.display())

requested_quantity = int(input("Enter the quantity \n"))


print(p.check_availability(requested_quantity))


