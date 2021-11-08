#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Milestone project 2 


# In[2]:


#Card class

#suit,rank,value
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}


# In[3]:


class Card():
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit


# In[4]:


three_of_clubs = Card("Clubs","Three")


# In[5]:


three_of_clubs


# In[6]:


print(three_of_clubs)


# In[7]:


three_of_clubs.suit


# In[8]:


three_of_clubs.rank


# In[9]:


three_of_clubs.value


# In[10]:


two_diamonds = Card("Diamonds","Two")


# In[11]:


print(two_diamonds)


# In[12]:


two_diamonds


# In[13]:


two_diamonds.suit


# In[14]:


two_diamonds.rank


# In[15]:


two_diamonds.value


# In[16]:


#comparing card value between players
two_diamonds.value < three_of_clubs.value


# In[17]:


#comparing card value between players.. if equaly, then players WAR!!!


two_diamonds.value == three_of_clubs.value


# In[18]:


#Deck Class


# In[19]:


class Deck():
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                # creat the card objects
                created_card = Card(suit,rank)
                
                self.all_cards.append(created_card)
                
                
    
    def shuffle(self):
        
        #shuffle the deck
        random.shuffle(self.all_cards)
        print("Deck Shuffled and ready!!!")
        
    def deal_one(self):
        
        return self.all_cards.pop()


# In[20]:


new_deck = Deck()


# In[21]:


new_deck.shuffle()


# In[22]:


mycard = new_deck.deal_one()


# In[23]:


mycard


# In[24]:


print(mycard)


# In[25]:


len(new_deck.all_cards)


# In[26]:


print(new_deck)


# In[27]:


new_deck.all_cards[0]


# In[28]:


#print first card from the new deck
first_card = new_deck.all_cards[0]


# In[29]:


print(first_card)


# In[30]:


#print last card from the new deck

bottom_card = new_deck.all_cards[-1]


# In[31]:


print(bottom_card)


# In[32]:


#loop through call cards in the new deck and print out the cards in the list (without shuffle method)
for card_objects in new_deck.all_cards:
    print(card_objects)


# In[33]:


#shuffle deck
new_deck.shuffle()


# In[34]:


#loop through call cards in the new deck and print out the cards in the list (with shuffle method)
print(new_deck.all_cards[-1])


# In[35]:


for card_objects in new_deck.all_cards:
    print(card_objects)


# In[ ]:





# In[36]:


#Player Class


# In[37]:


class Player:
    
    def __init__(self,name):
        self.name = name
        # A new player has no cards
        self.all_cards = [] 
        
    def remove_one(self):
        return self.all_cards.pop(0)    
    
    def add_cards(self,new_cards):
        #if the 'type' of new_cards is the 'type' of an empty list
        if type(new_cards) == type([]):   
            #list of multiple cards objects .. use the extend method
            self.all_cards.extend(new_cards)
        else:
            #list of Single cards objects .. use the append method
            self.all_cards.append(new_cards) 
        
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    


# In[38]:


new_player = Player('Jose')


# In[39]:


print(new_player)


# In[40]:


new_player.add_cards(mycard)


# In[41]:


print(mycard)


# In[42]:


print(new_player)


# In[43]:


print(new_player.all_cards[0])


# In[44]:


new_player.add_cards([mycard,mycard,mycard])


# In[45]:


print(new_player)


# In[46]:


new_player.remove_one()


# In[47]:


print(new_player)


# In[ ]:





# In[48]:


#Game Logic 


# In[49]:


# game setup - creating players
player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()


#deal each player their cards (26 cards each)
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# In[50]:


len(player_one.all_cards)


# In[51]:


game_on = True


# In[52]:


# While game_on

round_num = 0

while game_on:
    
    round_num += 1
    print(f"Round {round_num}")
    
    if len(player_one.all_cards) == 0:
        print("Player One, out of cards! Player Two wins")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player Two, out of cards! Player One wins")
        game_on = False
        break
    
    #start a new round
    player_one_cards = []
    
    player_one_cards.append(player_one.remove_one())
    
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    #While at_war

    at_war = True
        
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value: 
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value: 
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            at_war = False

        else:
            print('WAR!!!!')
            #player_one_cards[-1].value == player_two_cards[-1].value:
            if len(player_one.all_cards) < 5:
                print('Player One cannot declare war')
                print('Player Two wins')
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print('Player Two cannot declare war')
                print('Player One wins')
                game_on = False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                


# In[ ]:





# In[53]:


#Milestone Project (2)


# In[65]:


#In this milestone project you will be creating a Complete BlackJack Card Game in Python.

#Here are the requirements:

#    You need to create a simple text-based BlackJack game
#    The game needs to have one player versus an automated dealer.
#    The player can stand or hit.
#    The player must be able to pick their betting amount.
#    You need to keep track of the player's total money.
#    You need to alert the player of wins, losses, or busts, etc...

#And most importantly:

#    You must use OOP and classes in some portion of your game. You can not just use functions in your game. 
#Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!

#Feel free to expand this game. Try including multiple players. Try adding in Double-Down and card splits! 
#Remember to you are free to use any resources you want and as always:


# In[82]:


#Step 1: Import the random module. This will be used to shuffle the deck prior to dealing. Then, declare variables to store suits,
#ranks and values. You can develop your own system, or copy ours below. Finally, declare a Boolean value to be used to control while loops. 
#This is a common practice used to control the flow of the game.


import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


playing = True


# In[83]:


#Class Definitions

#Consider making a Card class where each Card object has a suit and a rank, then a Deck class to hold all 52 Card objects, and can be shuffled,
#and finally a Hand class that holds those Cards that have been dealt to each player from the Deck.

#Step 2: Create a Card Class
#A Card object really only needs two attributes: suit and rank. You might add an attribute for "value" - we chose to handle value later when developing our Hand class.
#In addition to the Card's __init__ method, consider adding a __str__ method that, when asked to print a Card, returns a string in the form "Two of Hearts"


class Card():
    
    def __init__(self,suit,rank):
        
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit


# In[84]:


three_of_clubs = Card("Clubs","Three")


# In[85]:


print(three_of_clubs)


# In[86]:


#Step 3: Create a Deck Class
#Here we might store 52 card objects in a list that can later be shuffled. First, though, we need to instantiate all 52 unique card objects and 
#add them to our list. So long as the Card class definition appears in our code, we can build Card objects inside our Deck __init__ method. Consider iterating 
#over sequences of suits and ranks to build out each card. This might appear inside a Deck class __init__ method:

#for suit in suits:
#    for rank in ranks:

#In addition to an __init__ method we'll want to add methods to shuffle our deck, and to deal out cards during gameplay.

#OPTIONAL: We may never need to print the contents of the deck during gameplay, but having the ability to see the cards inside it may help troubleshoot 
#    any problems that occur during development. With this in mind, consider adding a __str__ method to the class definition.


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                
                self.deck.append(created_card)
    
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return "The deck has : "+deck_comp
        
    def shuffle(self):
        #shuffle the deck
        random.shuffle(self.deck)
        print("Deck shuffled and ready!!!")
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card


# In[71]:


#

test_deck = Deck()
test_deck.shuffle()
print(test_deck)


# In[97]:


#Step 4: Create a Hand Class
#In addition to holding Card objects dealt from the Deck, the Hand class may be used to calculate the value of those cards 
#using the values dictionary defined above. It may also need to adjust for the value of Aces when appropriate.

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        # Card passed in from Deck.deal() --> single Card(suit,rank)
        self.cards.append(card)
        
        #adjusting amount by taking the cards rank and looking in the values dictionary
        self.value += values[card.rank]
        
        
        #track aces
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        
        
        # if total value > 21 and I still have an Ace
        # then change my ace to be a 1 instead of an 11
        while self.aces > 21 and self.aces:   

        #can also be written like the below
        #while self.aces > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1
    
    
    


# In[98]:


test_deck = Deck()
test_deck.shuffle()

#player
test_player = Hand()

#deal 1 card from the deck CARD(suit,rank)
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)


# In[ ]:





# In[95]:


test_player.add_card(test_deck.deal())


# In[96]:


test_player.value


# In[100]:


#Step 5: Create a Chips Class
#In addition to decks of cards and hands, we need to keep track of a Player's starting chips, bets, and ongoing winnings. 
#This could be done using global variables, but in the spirit of object oriented programming, let's make a Chips class instead!

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet



# In[ ]:





# In[103]:


#Step 6: Write a function for taking bets
#Since we're asking the user for an integer value, this would be a good place to use try/except. 
#Remember to check that a Player's bet can be covered by their available chips.


def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break


# In[ ]:





# In[104]:


#Step 7: Write a function for taking hits
#Either player can take hits until they bust. This function will be called during gameplay anytime a Player 
#requests a hit, or a Dealer's hand is less than 17. It should take in Deck and Hand objects as arguments, and
#deal one card off the deck and add it to the Hand. You may want it to check for aces in the event that a player's hand exceeds 21.

def hit(deck,hand):
    
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
    


# In[ ]:





# In[112]:


#Step 8: Write a function prompting the Player to Hit or Stand
#This function should accept the deck and the player's hand as arguments, and assign playing as a global variable.
#If the Player Hits, employ the hit() function above. If the Player Stands, set the playing variable to False - this
#will control the behavior of a while loop later on in our code.



def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break


# In[120]:


#Step 9: Write functions to display cards
#When the game starts, and after each time Player takes a card, the dealer's first card is hidden and all
#of Player's cards are visible. At the end of the hand all cards are shown, and you may want to show each 
#hand's total value. Write a function for each of these scenarios.


def show_some(player,dealer):
    # Show only one of the dealers cards
    print("\n Dealer's Hand: ")
    print("First card hidden!!!")
    print(dealer.cards[1])
    
    
    # show all (2 cards) of the players hand/cards
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
    
    
    
def show_all(player,dealer):
    
    # Show all the dealers cards
    print("\n Dealer's hand: ")
    for card in dealer.cards:
        print(card)
    
    
    #Alernative method instead of the for loop:
    #print("\n Dealer's hand: ",*dealer.cards,sep='\n')
    
    #calculate and display value (eg j+k == 20)
    print(f"Value of Dealers hand is : {dealer.value}")
    
    #show all the players cards
    print("\n Player's hand: ")
    for card in player.cards:
        print(card)
    
    print(f"Value of Player's hand is : {player.value}")



# In[121]:


#Step 10: Write functions to handle end of game scenarios
#Remember to pass player's hand, dealer's hand and chips as needed.




def player_busts(player,dealer,chips):
    print("Bust Player!!!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player Wins!!!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Player Wins!!! Dealer Buster")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer Wins!!!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player Tie!! Push")


# In[ ]:





# In[122]:


while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
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
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break


# In[ ]:





# In[ ]:





# In[ ]:




