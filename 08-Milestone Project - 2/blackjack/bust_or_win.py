def player_busts(player, dealer, chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("PLAYER WINS!")
    chips.win_bet()
    
def dealer_busts(player, dealer, chips):
    print("PLAYER WINS, DEALER BUSTED!")
    chips.win_bet()
    
def dealer_wins(player, dealer, chips):
    print("BUST PLAYER! DEALER WINS!")
    chips.lose_bet()
    
def push(player, dealer):
    print("Dealer and player tie, push!")