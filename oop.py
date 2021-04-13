class Budget:
    def __init__(self):
        self.food_balance = 100
        self.clothing_balance = 100
        self.entertainment_balance = 100

    def depositFund(self, category, amount):
        if category == 'food':
            self.food_balance += int(amount)
            return "Deposited amount to food budget: " + str(amount) + ". Total balance: " + str(self.food_balance)
        elif category == 'clothing':
            self.clothing_balance += int(amount)
            return "Deposited amount to clothing budget: " + str(amount) + ". Total balance: " + str(self.clothing_balance)
        elif category == 'entertainment':
            self.entertainment_balance += int(amount)
            return "Deposited amount to entertainment budget: " + str(amount) + ". Total balance: " + str(self.entertainment_balance)
            
    def witdrawlFund(self, category, amount):
        if category == 'food':
            self.food_balance -= int(amount)
            return "Withdrawl amount to food budget: "  + str(amount) + ". Total balance: " + str(self.food_balance)
        elif category == 'clothing':
            self.clothing_balance -= int(amount)
            return "Withdrawl amount to clothing budget: " + str(amount) + ". Total balance: " + str(self.clothing_balance)
        elif category == 'entertainment':
            self.entertainment_balance -= int(amount)
            return "Withdrawl amount to entertainment budget: "+ str(amount) + ". Total balance: " + str(self.entertainment_balance)
        
        
food = Budget()

clothing = Budget()

entertainment = Budget()

print(food.depositFund('food', 10))
print(clothing.depositFund('clothing', 50))
print(entertainment.depositFund('entertainment', 80))

print(food.witdrawlFund('food', 10))
print(clothing.witdrawlFund('clothing', 50))
print(entertainment.witdrawlFund('entertainment', 80))
