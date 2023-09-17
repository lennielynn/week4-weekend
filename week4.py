"""
52 cards / 4 suits(clubs, dimonds, hearts, spades) num 1-13 Ace-King
no wild cards

Gameplay:
Dealer shuffles deck

Both the dealer and the player get 2 cards each(only one of the dealers cards ar visible)

The player can either choose to Hit or Stand. if they choose hit they recieve another card. 
If their total card value is greater then 21 they Bust and are out of the game

If on the FIRST deal the players card value equals 21 it is condidered blackJack and that player 
gets 2 times their bet. or wins depending on the number of players 

If the player chooses to Stand that means they no longer want any cards an their turn is over. once
all players have had their turn it is the dealers turn

The dealer reveales their second card. If the dealers card sum is less than 16 they must draw again.
but can bust if they go over 21. If the dealer gets black jack he wins and takes all bets placed.

If a players card sum is less than the dealer they loose. If the Players card sum is 
higher then the dealer they win their bet, and if the players card sum is equal to the dealer its a 
draw. 


all numbers represent themelves
jack-king = 10
Ace = 11 or 1

"""



import random 


class FreePlayCards:
    
    
    def __init__(self):
        self.player_hand = {
            'cards': [],
            'values': 0
        }
        self.dealer_hand = {
            'cards': [],
            'values': 0
        }            
        self.key = {
            'H': {'2H': 2, '3H': 3, '4H': 4, '5H': 5,  '6H': 6,'7H': 7,
            '8H': 8, '9H': 9, '10H': 10, 'JH' : 10, 'QH': 10 , 'KH': 10, 'AH': [1, 11]},
            
            'D': {'2D': 2, '3D': 3, '4D': 4, '5D': 5,  '6D': 6,'7D': 7,
            '8D': 8, '9D': 9, '10D': 10, 'JD' : 10, 'QD': 10 , 'KD': 10, 'AD': [1, 11]},
            
            'C': {'2C': 2, '3C': 3, '4C': 4, '5C': 5,  '6C': 6,'7C': 7,
            '8C': 8, '9C': 9, '10C': 10, 'JC' : 10, 'QC': 10 , 'KC': 10, 'AC': [1, 11]},
            
            'S': {'2S': 2, '3S': 3, '4S': 4, '5S': 5,  '6S': 6, '7S': 7,
            '8S': 8, '9S': 9, '10S': 10, 'JS' : 10, 'QS': 10 , 'KS': 10, 'AS': [1, 11]}
        }
    
        self.deck = ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
        '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
         '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
        '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']
        
    def score(self, s_list):
        total = 0
        for s in s_list:
            if s[0].isnumeric():
                if s[0] == '1':
                    total += 10
                else:
                    total += int(s[0])
            elif s[0] != 'A':
                total += 10   
            else:
                if total < 11:
                    total += 11
                else:
                    total += 1
        return total
            
    def FreeDrawP(self):     
        self.player_hand['cards'].append(self.deck.pop())
        
    def FreeDrawD(self):
        self.dealer_hand['cards'].append(self.deck.pop())
        if self.dealer_card['values'] > 16:
            self.dealer_hand['cards'].append(self.deck.pop())
           
    
    def Deal(self):
        for i in range(2):
            self.player_hand['cards'].append(self.deck.pop())
            self.dealer_hand['cards'].append(self.deck.pop())
            self.player_hand['values'] += self.score(self.player_hand['cards'])
            # self.player_card = [random.choice(self.deck.values())]
            # self.player_hand.append(self.player_card)          
            # self.dealer_card = [random.choice(self.deck.values())]
            # self.dealer_hand.append(self.dealer_card)
            
    
class BlackJack:
    
    def __init__(self):
        pass
    
    
    #The player can either choose to Hit or Stand. if they choose hit they recieve another card. If their total card value is greater then 21 they Bust and are out of the game
    def PlayerTurn(self):
        print(f"Your hand is:  {cards.player_hand.keys()} \n The Dealers hand is {cards.dealer_hand.keys([0])} ")        
        if sum(cards.player_hand.values()) == 21:
            game.PlayerWin()
        else:
            while True:
                responce = input('Would you like to [h]it, or [s]tand? ').lower
                if responce == 'h':
                    cards.FreeDrawP()
                    print(f'your new hand is {cards.player_hand.keys()}')
                    if sum(cards.player_hand.values()) > 21:
                        print('You Bust, Dealer Wins!')
                        break
                elif responce == 's':
                    game.DealerTurn()
                
    #The dealer reveales their second card. If the dealers card sum is less than 16 they must draw again, but can bust if they go over 21. If the dealer gets black jack he wins and takes all bets placed.
    def DealerTurn():
        print(f'The dealers hand is {cards.dealer_hand.keys()}')
        if sum(cards.dealer_hand) < 16:
            cards.FreeDrawD()
            if sum(cards.dealer_hand) > 21:
                game.PlayerWin()
    
    def PlayerWin(self):
        print('You won!')
        
        
def Driver():
    while True:
        cards.Deal
        print(cards.player_hand)
        break
    #    beg_in = input('Welcome To Black Jack! Would you like to [b]et or [f]reeplay? ').lower
    #    if beg_in == 'f':
    #          print('dealer is shuffling...\n\n The cards are being dealt. Good luck! ' )  
    #          cards.Deal()
    #          game.PlayerTurn()
    #    elif beg_in == 'b':
    #        pass
       
         
                 
 
cards = FreePlayCards()
game = BlackJack()
Driver()
 
