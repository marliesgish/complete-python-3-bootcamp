'''
The user enters a cost and then the amount of money given. The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.
'''

import math

class ChangeReturn():

    def __init__(self):
        self.cost, self.money_given = self.get_amount_change()
        self.change = self.money_given - self.cost
        self.change = float("{0:.2f}".format(self.change))
        self.list_change = self.get_list_change()
        self.dict_change = self.get_dict_change()
        self.get_printed_information()

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


    def get_list_change(self):

        change = self.change

        list_100 = []
        list_50 = []
        list_20 = []
        list_10 = []
        list_5 = []
        list_2 = []
        list_1 = []
        list_05 = []
        list_02 = []
        list_01 = []
        list_005 = []

        while True:
            if change >= 100:
                list_100.append(1)
                change -= 100
            elif change >= 50:
                list_50.append(1)
                change -= 50
            elif change >= 20:
                list_20.append(1)
                change -= 20
            elif change >= 10:
                list_10.append(1)
                change -= 10
            elif change >= 5:
                list_5.append(1)
                change -= 5
            elif change >= 2:
                list_2.append(1)
                change -= 2
            elif change >= 1:
                list_1.append(1)
                change -= 1
            elif change >= 0.5:
                list_05.append(1)
                change -= 0.5
            elif change >= 0.2:
                list_02.append(1)
                change -= 0.2
            elif change >= 0.1:
                list_01.append(1)
                change -= 0.1
            elif change >= 0.05:
                list_005.append(1)
                change -= 0.05
            else:
                return [sum(list_100), sum(list_50), sum(list_20), sum(list_10), sum(list_5), sum(list_2), sum(list_1), sum(list_05), sum(list_02), sum(list_01), sum(list_005)]


    def get_dict_change(self):
        dict_change = {
        "100 euro bill": self.list_change[0],
        "50 euro bill": self.list_change[1],
        "20 euro bill": self.list_change[2],
        "10 euro bill": self.list_change[3],
        "5 euro bill": self.list_change[4],
        "2 euro coin": self.list_change[5],
        "1 euro coin": self.list_change[6],
        "50 euro cent": self.list_change[7],
        "20 euro cent": self.list_change[8],
        "10 euro cent": self.list_change[9],
        "5 euro cent": self.list_change[10],
        }
        return dict_change

    def get_printed_information(self):
        change = ("{0:.2f}".format(self.change))

        dict_change = self.dict_change

        print(f"The total change is: {change}\n")
        print(f"You will get back:\n")
        for key, value in dict_change.items():
            if value > 0:

                print(f"{key}: {value}")



Person1 = ChangeReturn()