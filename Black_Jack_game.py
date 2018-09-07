
# coding: utf-8

# In[ ]:


import random
suits=('diamonds','spades','clubs','hearts')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing=True
#Creating a Card Class that will give a card with suit-rank pair
class Card():
    '''
    DOCSTRING: This class returns the cards
    INPUT: Suit and Rank
    RETURN: string of card with suit and rank pair
    '''
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank+" of "+self.suit
#Creating a Deck class that will give the deck of cards,print the cards,shuffle and make a deal
class Deck():
    '''
    DOCSTRING: This class adds the cards produced to deck
    Methods
    __str__:print string of cards in deck
    shuffle: shuffles the deck
    deal: pops the dealer card and returns it
    INPUT: no input
    OUTPUT: returns the dealer card
    '''
    def __init__(self):
        self.deck=[]
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp=''
        for card in self.deck:
            deck_comp+='\n'+card.__str__()
        return deck_comp
    def shuffle(self):
        random.shuffle(self.deck)
    def deal(self):
        return self.deck.pop()
#Creating a Hand Class that can add card values to a player hand
class Hand():
    '''
    DOCSTRING: This class adds cards to hands of player
    Methods:
    add_card: adds rank on card to value
    INPUT: card popped from deal
    RETURN: None
    adjust_ace:Chnages ace value from 11 to 1 after value>21
    
    '''
    def __init__(self):
        # initialising all the cards,value and no.of aces to empty
        self.value=0
        self.aces=0
        self.cards=[]
    def add_card(self,card):
        #adding each card popped out in the deal to the list of cards
        self.cards.append(card)
        #incrementing the total value based on rank of each card popped
        self.value+=values[card.rank]
        #tracking the number of aces
        if card.rank=='Ace':
            self.aces+=1
    def adjust_ace(self):
        #If value > 21 and player still has ace then change ace to '1' instead of '11'
        while self.value>21 and self.aces>0:
            self.value-=10
            self.aces-=1
# Creating Chip class to track chips and bet
class Chips():
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def loose_bet(self):
        self.total-=self.bet
def take_bet(chips):
    while True:
        try:
            chips.bet=int(input("Please enter your bet:"))
        except:
            print("Please enter a valid number")
        else:
            if chips.bet>chips.total:
                print("Sorry you don't have enough chips..\n You currently have {} chips".format(chips.total))
            else:
                break
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_ace()
def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input("Hit or stand? \n Enter 'h' for hit and 's' for stand")
        if x.lower()=='h':
            hit(deck,hand)
        elif x.lower()=='s':
            print("Player stands.Dealer's turn")
            playing= False
        else:
            print("please enter a valid 'h' or 's'")
            continue
def show_some(player,dealer):
    print('DEALERS HAND:')
    print('One card hidden!')
    print(dealer.cards[1])
    print('\n')
    print('Players HAND:')
    for card in player.cards:
        print(card)
def show_all(player,dealer):
    print('DEALERS HAND:')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('Payers HAND:')
    for card in player.cards:
        print(card)
def player_busts(player,dealer,chips):
    print("BUST player!")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print('Player WINS!')
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print("Dealer BUSTED!")
    chips.lose_bet()
def dealer_wins(player,dealer,chips):
    print("Dealer WINS!")
    chips.win_bet()
def push(player,dealer):
    print("Dealer and Player tie")
    
while True:
    print("Welcome to BLACK JACK")
    deck=Deck()
    deck.shuffle()
    
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    player_chips=Chips()
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value>21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value<=21:
        while dealer_hand.value<player_hand.value:
            hit(deck,dealer_hand)
            
        show_all(player_hand,dealer_hand)
        if dealer_hand.value>211:
            dealer_hand(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value>player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value<player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
    print('\n Player total chips are: {}'.format(player_chips))
    #Ask to play again
    new_game=input("Would like to play the game again? Press 'y or 'n'..")
    if new_game.lower=='y':
        playing=True
        continue
    else:
        print('Thank you for playing!Hope you enjoyed..')
        break
    


# In[ ]:




