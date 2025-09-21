from BankAccount import BankAccount

class savings(BankAccount):
    interestRate = .03
    def __init__(self, customer_name, current_balance, minimum_balance):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interestRate = self.interestRate
    def showInterestRate(self):
        return self.interestRate

    def add_interest(self):
        interest = self.current_balance * self.interestRate
        self.current_balance += interest
        print(f"{self.customer_name}: Interest of {interest:.2f} added. New balance: {self.current_balance:.2f}")