class Animal:
    def speak(self):
        print("This is animal class")
        
class Dog(Animal):
    def speak(self):
        print("This is dog class")
        
class Cat(Animal):
    def speak(self):
        print("This is cat class")
        
obj = Cat()
obj.speak()
        