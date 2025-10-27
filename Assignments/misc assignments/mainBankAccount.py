from savings import savings
from checkings import checkings
from BankAccount import BankAccount

def main():
    alice_savings = savings("Alice", 1000, 100)
    bob_savings = savings("Bob", 500, 50)

    alice_savings.add_interest()
    bob_savings.add_interest()

    # Create Checking accounts
    charlie_checking = checkings("Charlie", 1200, 100)
    diana_checking = checkings("Diana", 800, 50)

    charlie_checking.transfer(400, diana_checking)  # valid
    charlie_checking.transfer(700, diana_checking)  # exceeds limit

    alice_savings.print_customer_information()
    bob_savings.print_customer_information()
    charlie_checking.print_customer_information()
    diana_checking.print_customer_information()

if __name__ == "__main__":
    main()
