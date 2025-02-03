class Employee:
    def __init__(self,name,id,dept):
        self.name = name
        self.id = id
        self.dept=dept
        
    def display(self):
        print(f"\n Employee details are : \n\n Name : {self.name} \n Id : {self.id} \n Deartment : {self.dept} \n")
        
name = input("Enter the name \n")
id = int(input("Enter the id \n "))
dept = input("Enter the department \n")

emp = Employee(name,id,dept)
emp.display()