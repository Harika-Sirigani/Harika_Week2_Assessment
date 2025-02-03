from abc import ABC,abstractmethod

class IDatabaseOPeration(ABC):
    
    def insert(self,name,age,id):
        pass
    
    def update(self,id):
        pass
    
    def delete(self,id):
        pass
    
class SQLDatabase:
    def insert(self,name,age,id):
        print(f"Inserting data : {name},{age},{id}")
    
    def update(self,id):
        print(f"Updating id : {id}")
    
    def delete(self,id):
        print(f"Deleting id : {id}")
    
class NoSQLDatabase:
    def insert(self,name,age,id):
        print(f"Inserting name, age and id into database : {name},{age},{id}")
    def update(self,id):
        print(f"After updating id is {id}")
    def delete(self,id):
        print(f"Deleting {id} id from databse")
    
print("NoSQLDatabase \n")
obj = NoSQLDatabase()
obj.insert("Krish",25,201)
obj.update(203)
obj.delete(203)

print("SQLDatabase")
obj = SQLDatabase()
obj.insert("Hari",20,101)
obj.update(102)
obj.delete(102)


        
