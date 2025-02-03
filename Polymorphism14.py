class Notification:
    def send(self):
        pass
    
class EmailNotification():
    def __init__(self,email):
        self.email=email
        
    def send(self,message):
        print(f"The mail is {self.email} : {message}")
        
class SMSNotification():
    def __init__(self,sms):
        self.sms=sms
        
    def send(self,message):
        print(f"sms Notification {self.sms} : {message}")
        
obj = SMSNotification("from hari")
obj.send("HY")

obj1= EmailNotification("abc@gmail.com")
obj1.send("Hello")