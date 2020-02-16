'''
Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).
'''



class MortgageCalculator():

    def __init__(self):
        self.mortgage_amount()

    def mortgage_amount(self):
        while True:
            amount = input("What is the amount of mortgage in euros?")
            if amount.isnumeric():
                years = self.total_years()
                input_terms, terms = self.choose_terms(years)
                self.printed_information(amount, years, input_terms, terms)
                break
            else:
                print("Your input is not valid, please try again\n")
                continue
        

    def total_years(self):
        while True:
            years = input("In how many years would you like to pay your mortgage back?")
            if years.isnumeric():
                break
            else:
                print("Your input is not valid, please try again\n")
                continue
        return years


    def choose_terms(self, years):
        terms_values = {"yearly":1, "monthly":12, "weekly":52, "daily":365,}

        while True:
            input_terms = input("How often would you like to have your payments: 'yearly', 'monthly', 'weekly' or 'daily'?")
            input_terms = input_terms.lower()
            
            if input_terms == "yearly":
                terms = terms_values["yearly"]
                break
            elif input_terms == "monthly":
                terms = terms_values["monthly"]
                break
            elif input_terms == "weekly":
                terms = terms_values["weekly"]
                break
            elif input_terms == "daily":
                terms = terms_values["daily"]
                break
            else:
                print("Your input is not valid, please try again\n")
                continue
            
        terms = int(terms)*int(years)
            
        return input_terms, terms

    def get_label(self, input_terms, terms):
        terms_dict = {
            "yearly": {
                "singular": "year",
                "plural": "years"
            },
            "monthly": {
                "singular": "month",
                "plural": "months"
            },
            "weekly": {
                "singular": "week",
                "plural": "weeks"
            },
            "daily": {
                "singular": "day",
                "plural": "days"
            }
        }

        t = terms_dict[input_terms]
        return t["plural"] if int(terms) > 1 else t["singular"]


    def printed_information(self, amount, years, input_terms, terms):
        
        payment = int(amount) / int(terms)
        payment = int(payment)

        readable_term = self.get_label(input_terms, terms)
        readable_year = (self.get_label(input_terms, years)).capitalize()


        print(f"Mortgage: € {amount}")
        print(f"{readable_year}: {years}")
        print(f"Terms: {terms} {readable_term}")
        print(f"\nYou will have to pay € {payment} {input_terms} for {readable_term}.")
        

MortgageCalculator()