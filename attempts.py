#===========================================================
 # import random

# class Deck:
#     def _init_(self):
#         self.deck = {
#             'hearts': {'2H': 2, '3H': 3, '4H': 4, '5H': 5,  '6H': 6,'7H': 7,
#             '8H': 8, '9H': 9, '10H': 10, 'JH' : 10, 'QH': 10 , 'KH': 10, 'AH': [1, 11]},
            
#             'diamonds': {'2D': 2, '3D': 3, '4D': 4, '5D': 5,  '6D': 6,'7D': 7,
#             '8D': 8, '9D': 9, '10D': 10, 'JD' : 10, 'QD': 10 , 'KD': 10, 'AD': [1, 11]},
            
#             'clubs': {'2C': 2, '3C': 3, '4C': 4, '5C': 5,  '6C': 6,'7C': 7,
#             '8C': 8, '9C': 9, '10C': 10, 'JC' : 10, 'QC': 10 , 'KC': 10, 'AC': [1, 11]},
            
#             'spades': {'2S': 2, '3S': 3, '4S': 4, '5S': 5,  '6S': 6, '7S': 7,
#             '8S': 8, '9S': 9, '10S': 10, 'JS' : 10, 'QS': 10 , 'KS': 10, 'AS': [1, 11]}
#         }
        
#         self.player_hand = []
#         self.dealer_hand = []
        
    # def Draw(self):
    #     for _ in range(2):
    #         card, value = self.draw_card()
    #         self.player_hand.append((card, value))
    #     print(self.player_hand)
        
#     def Draw(self):
#         suit = random.choice(list(self.deck.keys()))
#         card, value = random.choice(list(self.deck[suit].items()))
#         del self.deck[suit][card]
#         if not self.deck[suit]:
#             del self.deck[suit]
#         return card, value
    
# deck_instance = Deck()
# deck_instance.Draw()


#================================================   
# import random 

# class BlackJack:



# def __init__(self, player, dealer):
#         self.player = player
#         self.dealer = dealer
#         self.deck = {
#         'hearts': ['2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH'],
#         'diamonds': ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD'],
#         'clubs': ['2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC'],
#         'spades': ['2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']
#         }
        
        
#     def Draw(self):
#          suit = random.choice(list(self.deck.keys()))
#          card = random.choice(self.deck[suit])
#          print(card)
         
        
#     def DealCards(self):
#          self.dealer = []
#          self.player = []
#          print(self.player)
#          for card in range(2):
#             new_player_card = game.Draw(self.deck)
#             new_dealer_card = game.Draw(self.deck)
#             self.player.append(new_player_card)
#             self.dealer.append(new_dealer_card)
            
#     def PlayerHit(self):
#         self.player.append(game.Draw)
        
#     def Stay(self):
#         print(f'The dealer has {self.dealer[0,1]}')
    
# def Driver():
#     # player_hand = game.DealCards
#     # print(player_hand)
#     # print(f'You have {player_hand[0][0]} and {player_hand[0][1]}. Dealer has a {player_hand[1][0]} showing')
#     while True:
#         reply = input('Do you want to exit, hit, or stay? ').lower
#         if reply == 'hit':
#             game.PlayerHit()
#             print('you hit')
#         elif reply == 'stay':
#             game.Stay()
#             print("Dealer's turn")
#         elif reply == 'exit':
#             break
#         # else:
#         #     print('please enter valid input')
            
               
# game = BlackJack([],[])  
# Driver()