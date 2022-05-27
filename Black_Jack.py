#scratch code
#- Create text-based game.
#- Game needs to have an automated Dealer.
#- The player can wait or ask for more cards.
#- The player must be able to choose his bet amount.
#- You need to keep track of players' total money.
#- You need to alert the player of wins, losses, etc.
#- You must use OOP and classes. It is not allowed to use only functions.
#- Do not hesitate to expand the game.

#The project will consist in:
    #1 class for the player
    #1 class for the dealer
    #1 function to calculate money, game score, etc
    #1 function to print everything, including results and info
    #1 main function that call's all the other function and uses it classes

#Player class - a player has a name, money, points and cards.
class player(object):
    def __init__(self, name, money, points, cards):
        self.name = name
        self.money = money
        self.points = points
        self.cards = cards
        print('\nPlayer %s created! \nMoney: $%.02f \nPoints: %r\n' %(self.name, self.money, self.points))

#Dealer class - a dealer has points and cards.
class dealer(object):
    def __init__(self, money, points, cards):
        self.name = 'Dealer'
        self.money = money
        self.points = points
        self.cards = cards
        print('%s created! \nMoney: $%.02f \nPoints: %r\n' %(self.name, self.money, self.points))

#Functions and classes tests
cards_p1 = []
cards_d = []
John_p1 = player('John', 100, 0, cards_p1)
Dealer_d1 = dealer(100, 0, cards_d)
