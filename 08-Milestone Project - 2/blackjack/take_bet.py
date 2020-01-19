def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("How much would you like to bet? "))
        except:
            print("This is not a number, please try again")
            continue
        else:
            if chips.bet > chips.total:
                print(f"Sorry, you do not have enough chips! You have {chips.total} chips.")
            else:
                break