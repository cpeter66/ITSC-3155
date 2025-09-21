from BankAccount import BankAccount

class checkings(BankAccount):
    transferMax = 600
    def __init__(self, customer_name, current_balance, minimum_balance):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.transferMax = self.transferMax

    def showTransferMax(self):
        return self.transferMax
    def changeTransferMax(self, amount):
        amount = int(input("Please Enter new transfer amount as an integer"))
        self.transferMax = amount

    def transfer(self, amount, recipient):
        if amount > self.transferMax:
            print(f"{self.customer_name}: Transfer exceeds limit of {self.transferMax}")
        elif self.current_balance - amount < self.minimum_balance:
            print(f"{self.customer_name}: Insufficient funds for transfer")
        else:
            self.current_balance -= amount
            recipient.deposit(amount)
            print(f"{self.customer_name}: Transferred {amount} to {recipient.customer_name}")