import random
suits =('Hearts','Clubs','Daimonds','Spades')
values ={'Two':2,
        'Three':3,
        'Four':4,
        'Five':5,
        'Six':6,
        'Seven':7,
        'Eight':8,
        'Nine':9,
        'Ten':10,
        'Jack':11,
        'Queen':12,
        'King':13,
        'Ace':14,}
        
ranks =('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack',
       'Queen','King','Ace')

class Card():
    def __init__(self,suits,rank):
        self.suits = suits
        self.ranks = rank
        self.value = values[self.ranks]
    
    def __str__(self):
        return(f"{self.ranks} of {self.suits}")
    


class Deck():
    def __init__(self):
        self.all_card =[]

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_card.append(created_card)

    
    def shuffle(self):
        random.shuffle(self.all_card)


    def deal_one(self):
        return self.all_card.pop()


class Player:

    def __init__(self,name):
        self.name = name
        self.all_card = []

    def adding_cards(self,new_cards):
        if(type(new_cards)== type([])):
            self.all_card.extend(new_cards)
        else:
            self.all_card.append(new_cards)

    def remove_card(self):
        return self.all_card.pop(0)
    
    def __str__(self):
        return(f"The name of the player is :{self.name} and has {len(self.all_card)} cards")








#GAME SETUP 
player_one = Player("One")
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

#DIVIDING THE CARDS AMONG THE PLAYERS 

for i in range(26):
    player_one.adding_cards(new_deck.deal_one())
    player_two.adding_cards(new_deck.deal_one())


game_on =True
round_no = 0
while game_on:
    round_no +=1
    print(f"Round number is:{round_no}")

    if len(player_one.all_card)== 0:
        print('Player one is out of cards..! Player Two wins')
        game_on= False
        break

    if len(player_two.all_card)== 0:
        print('Player Two is out of cards..! Player One wins')
        game_on= False
        break


    #START OF NEW ROUND
    player_one_card = []
    player_one_card.append(player_one.remove_card())
    player_two_card =[]
    player_two_card.append(player_two.remove_card())

    at_war = True

    while at_war:
        if player_one_card[-1].value > player_two_card[-1].value:
            player_one.adding_cards(player_one_card)
            player_one.adding_cards(player_two_card)

            at_war = False
        elif player_one_card[-1].value < player_two_card[-1].value:
            player_two.adding_cards(player_one_card)
            player_two.adding_cards(player_two_card)

            at_war = False
        else:
            print("WAR")

            if len(player_one.all_card) < 5:
                print('Player one unable to declare the war ')
                print('Player two wins the game')
                game_on = False
                break
            elif len(player_two.all_card) < 5:
                print('Player two unable to declare the war ')
                print('Player one wins the game')
                game_on = False
                break
            else:
                for num in range(5):
                    player_one_card.append(player_one.remove_card())
                    player_two_card.append(player_two.remove_card())
