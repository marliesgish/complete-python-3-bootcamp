'''
The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
'''

import math


class ChangeReturn():


    def __init__(self):
        self.cost, self.money_given = self.get_amount_change()
        self.change_money()


    def get_amount_change(self):
        while True:
            try:
                cost = float(input("Please enter the total cost of your purchase"))
            except ValueError:
                print("Your input is not valid, please try again")
            else:
                break

        while True:
            try:
                money_given = float(input("Please enter the amount of cash that you give"))
            except ValueError:
                print("Your input is not valid, please try again")
                continue
            else:
                if money_given < cost:
                    print("The given money is not enough")
                    continue
                else:
                    break

        return float(cost), float(money_given)


    def change_money(self):
        remaining_money = round(self.money_given - self.cost, 2)

        money = [
            {
                "amount": 50,
                "money_type": 'bill'
            },
            {
                "amount": 20,
                "money_type": 'bill'
            },
            {
                "amount": 10,
                "money_type": 'bill'
            },
            {
                "amount": 5,
                "money_type": 'bill'
            },
            {
                "amount": 2,
                "money_type": 'coin'
            },
            {
                "amount": 1,
                "money_type": 'coin'
            },
            {
                "amount": .5,
                "money_type": 'cent'
            },
            {
                "amount": .2,
                "money_type": 'cent'
            },
            {
                "amount": .1,
                "money_type": 'cent'
            },
            {
                "amount": .05,
                "money_type": 'cent'
            },
        ]
    
        print(f"The total change is {remaining_money} euro")

        for m in money:
            amount = m["amount"]
            money_type = m["money_type"]
            if remaining_money / amount >= 1:
                amount_value = math.floor(remaining_money / amount)
                remaining_money = remaining_money%amount
                
                amount = ("{0:.2f}".format(amount))
                
                print(f"{amount_value} times {amount} euro {money_type}")


Person1 = ChangeReturn()