class Person:
    def show(self):
        print("This is person class")
    
class Employee(Person):
    def show(self):
        super().show()
        print("This is employee class")
    
class Manager(Employee):
    def show(self):
        super().show()
        print("This is manager class")
        
    
    def approve_leave(self):
        return "This is approval for leave method"
    
obj = Manager()
obj.show()
print(obj.approve_leave())