class BankAccount:
    def __init__(self, customer_name, mpin, account_type, balance):
        self.customer_name = customer_name
        self.__mpin = mpin
        self.account_type = account_type
        self.__balance = balance

    def get_balance(self):
        print(self.__balance)

    def __str__(self):
        return self.customer_name

BankAccount_instance = BankAccount("rahul unnikannan", 2211, "savings", 12000)

print(BankAccount_instance)  # This will print the customer name
BankAccount_instance.get_balance()  # This will print the balance
