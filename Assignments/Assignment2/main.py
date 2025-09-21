import data
from Assignments.Assignment2 import sandwich_maker, cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()




def main():
    control = True
    while control:
        userinput = input("What will you order? (small/ medium/ large/ off/ ): ")
        match userinput:
            case "small" | "medium" | "large" :
                sandwich = recipes[userinput]
                if sandwich_maker_instance.check_resources(recipes[userinput]["ingredients"]):
                    print("We have the resources to make your sandwich.")
                    insertedCash = cashier_instance.process_coins()
                    if cashier_instance.transaction_result(insertedCash, recipes[userinput]["cost"]):
                        print("Transaction successful making your order now...")
                        sandwich_maker_instance.make_sandwich(userinput, recipes[userinput]["ingredients"])
                        print("Here is your sandwich!")
                    else:
                        return "insufficient funds"
            case "off":
                break


if __name__=="__main__":
    main()
