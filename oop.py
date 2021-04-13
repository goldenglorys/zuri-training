class Budget:
    """
        Budget App
        Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects should allow for
            1.  Depositing funds to each of the categories
            2.  Withdrawing funds from each category
            3.  Computing category balances
            4.  Transferring balance amounts between categories
    """
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
        
    def getBalance(self, category):
        if category == 'food':
            return "Total balance for food category: " + str(self.food_balance)
        elif category == 'clothing':
            return "Total balance for clothing category: " + str(self.clothing_balance)
        elif category == 'entertainment':
            return "Total balance for entertainment category: " + str(self.entertainment_balance)
            
    # def transferBalance(self, from_cat, to_cat, amount):
        
        
food = Budget()

clothing = Budget()

entertainment = Budget()

print(food.depositFund('food', 10))
print(clothing.depositFund('clothing', 50))
print(entertainment.depositFund('entertainment', 80))

print(food.witdrawlFund('food', 10))
print(clothing.witdrawlFund('clothing', 50))
print(entertainment.witdrawlFund('entertainment', 80))

print(food.getBalance('food'))
print(food.getBalance('clothing'))
print(food.getBalance('entertainment'))
