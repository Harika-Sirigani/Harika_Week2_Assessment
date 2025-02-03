class BankAccount:
    def __init__(self,account_num,balance=0.0):
        self.account_num = account_num
        self.balance = balance
        
    def deposit(self,amount):
        if(amount>0):
            self.balance += amount
            print(f"Deposited {amount} in your bank \n The total balance is {self.balance} \n")
            
        else:
            print("Deposit number should be positive")
            
    def withdraw(self,amount):
        if(amount<0):
            print("Your account balance is 0 \n")
        elif amount>self.balance:
            print("Insufficient balance, Withdraw denied \n")
            
        else:
            self.balance -= amount
            print(f"Withdrawn : {amount} , Ramaining balance : {self.balance} \n")
            
    
    
    
    
account = BankAccount(15111078,1000)

num_transaction = int(input("enter the number of transactions: "))

for _ in range(num_transaction):
    action = input("Enter d for deposit and w for withdraw :")
    amount= int(input("Enter amount:"))
    
    if action == 'd':
        account.deposit(amount)
    elif action == 'w':
        account.deposit(amount)
    else:
        print("Invalid action . Please enter 'd' or 'w'")
        
#print(f"final Balance : {}")
        