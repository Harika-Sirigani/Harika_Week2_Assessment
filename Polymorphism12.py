class Payment:
    def process_payment(self):
        pass
    
class CreditCardPayment():
    def __init__(self,CreditCard_Holder,cre_amount):
        self.CreditCard_Holder=CreditCard_Holder
        self.cre_amount=cre_amount
        
    def process_payment(self):
        print(f"Credit card details: \n holder name is {self.CreditCard_Holder} \n credit balance is : {self.cre_amount}")
    
    
class PayPalPayment():
    def __init__(self,paypal_holder,pay_amount):
        self.paypal_holder=paypal_holder
        self.pay_amount=pay_amount
    def process_payment(self):
        print(f"Paypal details are : \n holder name : {self.paypal_holder}, paypal balance : {self.pay_amount}")    

class BitcoinPayment():
    def __init__(self,Bitcoin_holder,bit_amount):
        self.Bitcoin_holder=Bitcoin_holder
        self.bit_amount=bit_amount
        
    def process_payment(self):
        print(f"Bitcoin details are : \n holder name : {self.Bitcoin_holder} \n bit balance : {self.bit_amount}")
    
obj = BitcoinPayment("hari",20000)
obj.process_payment()

obj1 = PayPalPayment("Krish",10000)
obj1.process_payment()

obj2=CreditCardPayment("Ram",50000)
obj2.process_payment()