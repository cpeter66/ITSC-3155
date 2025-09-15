class BankAccount:
    bankName = "Wells Fargo of America"

    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance


    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance-amount < self.minimum_balance:
            print("Insufficient balance")
        else:
            self.current_balance -= amount
    def print_customer_information(self):
        print("Bank Name:" + self.bankName + " , Current Balance:" + str(self.current_balance) + " , Minimum Balance:" + str(self.minimum_balance))


Steven = BankAccount("Steven", 200, 100)
Steven.print_customer_information() #200, min bal 100
Steven.deposit(100)
Steven.print_customer_information() #300
Steven.withdraw(200) #100
Steven.print_customer_information()
Steven.withdraw(200)   #Should give insufficent

James = BankAccount("James", 4400, 300)