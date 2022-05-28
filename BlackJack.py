#In this project you will be creating
#a full blackjack cards games in python.
    #You need to create a blackjack game based on text.
    #The must have an automated dealer and a player.
    #The player can wait or ask more cards.
    #The player can choose his bet value.
    #You need to follow the players money.
    #You have to alert the player when he wins, loses, etc.

#Most important
    #You have to use POO and class in some part of your game
    #You can't use only functions in your game
    #Use you creativity

#Don't hexitate to expand the game! Maybe with more players.
#Use every resource you find usefull.

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
        print('%s created! \nMoney: $%.02f \n' %(self.name, self.money, self.points))

#Calculate money function - returns values and result of game
def Calculate_money(mp, md, mp_bet, winp):
    money_pd = []                                       #create list for money values
    if winp == 1:
        mp = mp + mp_bet*2
        md = md - mp_bet
    else:
        mp = mp - mp_bet
        md = md + mp_bet
    money_pd.append(mp)                                 #create list with money values
    money_pd.append(md)
    if md <= 0:
        money_pd.append(1)                              #indicates gameover
        if md < 0:
            negative_money = money_pd[1]
            money_pd[1] = 0
            money_pd[0] = money_pd[0] + negative_money  #Corrects player 1 money if gameover
    else:
        money_pd.append(0)
    return money_pd                                     #returns list with values of player money and Dealer money

#Prints info
def Print_game_info(list_mpd, pname, pcards, ppoints):
    mp = list_mpd[0]
    md = list_mpd[1]
    mpd = list_mpd[2]
    option_game

    if mpd == 1:
        print('\nGame over! The Dealer is out!\n')                  #prints game results when game over and player wins
        print(pname + "'s money: %r\n" mp)
        print("Dealer's money: %r\n" md)
        print(pname + "'s cards: %r\n" mp)
        option_game = 'n'
    elif mpd == 0:
        print('\nThe game continues!\n')                            #prints game results when game continues
        print("Dealer's money: %r\n" md)
        print(pname + "'s money: %r\n" mp)
        print(pname + "'s cards: " + pcards + '\n')
        option_game = input('Do you want 1 more card? (y/n)')
        while option_game != 'y' or option_game != 'Y':
            print("Type 'y' or 'Y' for yes and 'n' or 'N' for no.") 
            option_game = input('Do you want 1 more card? (s/n)')
    elif mpd == 3:
        print('\nGame over! You lose!\n')                           #prints game results when game over and player loses
        print(pname + "'s money: %r\n" mp)
        print("Dealer's money: %r\n" md)
        print(pname + "'s cards: %r\n" mp)
        print(pname + "'s points: %r\n" ppoints)
        option_game = 'n'
    return option_game

    
#insert cards points calculation


#Functions and classes tests
cards_p1 = []
cards_d = []
John_p1 = player('John', 100, 0, cards_p1)
Dealer_d1 = dealer(25, 0, cards_d)
lmoney = Calculate_money(John_p1.money, Dealer_d1.money, 30, 1)
print(lmoney)