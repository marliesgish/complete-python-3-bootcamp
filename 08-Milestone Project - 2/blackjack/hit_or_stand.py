def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
        
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above
            return True

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            return False
        else:
            print("Sorry, please try again.")
            continue
        break