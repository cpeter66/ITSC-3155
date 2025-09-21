class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please enter you coins")
        dollarInput = int(input("Please enter dollar input: "))
        halfDollarInput = int(input("Please enter half dollar input: "))
        quarterInput = int(input("Please enter quarter input: "))
        nickleInput = int(input("Please enter nickle input: "))
        total_coins = dollarInput*1.0 + halfDollarInput * .5 + quarterInput*.25 + nickleInput*.05
        return total_coins


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Insufficient funds")
            return False
        elif coins > cost:
            change = round(coins - cost, 2)
            print("Here is your change: $" + str(float(change)))
            return True
        else:
            print("Payment accepted ")
            return True

