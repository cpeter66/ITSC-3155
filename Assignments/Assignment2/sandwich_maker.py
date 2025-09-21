
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item, amount in ingredients.items():
            if self.machine_resources[item] < amount:
                print("Insufficient ingredients")
                return False
        return True


    def make_sandwich(self, sandwich_size, order_ingredients):
        for items, amount in order_ingredients.items():
            self.machine_resources[items] -= amount