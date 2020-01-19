from deck import Deck
from chips import Chips
from hand import Hand
import hit_or_stand
import take_bet
import show
import bust_or_win

playing = True
new_game  = True

player_chips = Chips(100)


while new_game:
    # Print an opening statement
    print("Welcome to Black Jack!")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()    
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    # Set up the Player's chips
    
    # Prompt the Player for their bet
    take_bet.take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show.show_some(player_hand,dealer_hand)    

    while playing:  # recall this variable from our hit_or_stand function
       
        # Prompt for Player to Hit or Stand
        playing = hit_or_stand.hit_or_stand(deck,player_hand)

        # Show cards (but keep one dealer card hidden)
        show.show_some(player_hand,dealer_hand)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            bust_or_win.dealer_wins(player_hand,dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit_or_stand.hit(deck, dealer_hand)
    
        # Show all cards
        show.show_all(player_hand,dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            bust_or_win.dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            bust_or_win.dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            bust_or_win.player_wins(player_hand,dealer_hand,player_chips)
        else:
            bust_or_win.push(player_hand,dealer_hand)
        
    # Inform Player of their chips total 
    print(f"\n Your total chips: {player_chips.total}")
    
    # Ask to play again
    while True:
        play = input("Do you want to play again? y/n: ")
        if play == 'y':
            playing = True
            new_game = True
            break
        elif play == 'n':
            print("Thank you for playing!")
            new_game = False
            break
        else:
            print("I did not get that.")
            continue