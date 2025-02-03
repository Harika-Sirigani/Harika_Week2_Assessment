from abc import ABC,abstractmethod

class UserAuthentication(ABC):
    @abstractmethod
    def login(self,username,password):
        pass
    def logout(self):
        pass
    
class GoogleAuth:
    def login(self,username,password):
        print("Google account is successfully logged in \n")
    def logout(self):
        print("Google account is successfully logged out \n")
        
class FacebookAuth:
    def login(self,username,password):
        print("Facebook account is successfully logged in \n")
    def logout(self):
        print("Facebook account is successfully logged out \n")
        
g = GoogleAuth()
g.login("Hari",123456789)
g.logout()

f = FacebookAuth()
f.login("Hari",123456789)
f.logout()