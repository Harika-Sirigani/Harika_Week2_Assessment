class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
        
    def display(self):
        return f"Student details are :\n Name : {self.name} \n RollNumber : {self.roll_number}"
    
stu = Student("Krish",32)
print(stu.display())