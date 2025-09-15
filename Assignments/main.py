### Data ###
from operator import truediv
from random import choice

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print("Insufficient ingredients")
                return False
        return True


        """Returns True when order can be made, False if ingredients are insufficient."""
    def process_coins(self):
        print("Please enter you coins")
        dollarInput = int(input("Please enter dollar input: "))
        halfDollarInput = int(input("Please enter half dollar input: "))
        quarterInput = int(input("Please enter quarter input: "))
        nickleInput = int(input("Please enter nickle input: "))
        total_coins = dollarInput*1.0 + halfDollarInput * .5 + quarterInput*.25 + nickleInput*.05
        return total_coins

        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

    def transaction_result(self, coins, cost):
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

        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for items, amount in order_ingredients.items():
            self.machine_resources[items] -= amount    ##removing ingredients

    def report(self):
        print(f"Current resources: Bread: {self.machine_resources['bread']}, "
              f"Ham: {self.machine_resources['ham']}, "
              f"Cheese: {self.machine_resources['cheese']}")


### Make an instance of SandwichMachine class and write the rest of the codes ###
machineInstance = SandwichMachine(resources)
control = True
while control:
    userinput = input("What will you order? (small/ medium/ large/ off/ report/): ")
    match userinput:

        case "off":
            break
        case "report":
            machineInstance.report()
        case "small"| "medium" | "large":
            sandwich = recipes[userinput]
            if machineInstance.check_resources(sandwich["ingredients"]):
                coins_inserted = machineInstance.process_coins()
                if machineInstance.transaction_result(coins_inserted, sandwich["cost"]):
                    machineInstance.make_sandwich(userinput, sandwich["ingredients"])


