

class Bank:
    def __init__(self,account_number,balance,ac_type,customer_name):
        self.account_number=account_number
        self.balance=balance
        self.ac_type=ac_type
        self.customer_name=customer_name
    def deposit(self,amount):
        self.balance+=amount
        print(f"your account{account_number}has been credited with amount{amount}available balance{balance}")
    def withdraw(self,amount):
        if self.balance>amount:
            self.balance-=balance
            print(f"your account{account_number}has been debited with amount{amount}available balance{balance}")
        else:
            print("insufficient bal")

        
    def bet_balance(self):
        print("your available balance",self.balance)
person=Bank(1000,2500,"savings","praveen")
person.withdraw(5000)

