class Logger:
    def log(self,message):
        print(f"{message}")
        
    def log(self,message,error=""):
        print(f"{message},{error}")
        
l = Logger()
l.log("you")
l.log("hy","This is error")
l.log("hello","warning")