class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        res = []
        i = 0
        for i in range(len(self.ingredients)):
            for j in range(len(self.toppings)):
                lst = [self.ingredients[i], self.toppings[j]]
                res.append(lst)
        return res


if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce", "black sauce", "tomato sauce"])
    print(machine.scoops())  # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]
