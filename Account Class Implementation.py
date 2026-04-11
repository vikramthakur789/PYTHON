class account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self ,amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance =", self.get_balance())    

    
    def credit(self ,amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance =", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = account(100000000,16263) 
print(acc1.balance)
print(acc1.account_no)      
acc1.credit(61536636)
acc1.debit(60000)
acc1.credit(1000000000)        
