#TicTacToe


import random

#create empty grid for game
def create_grid():
    translation = {39: None}
    grid_a1 = [' ']
    grid_a2 = [' ']
    grid_a3 = [' ']
    grid_b1 = [' ']
    grid_b2 = [' ']
    grid_b3 = [' ']
    grid_c1 = [' ']
    grid_c2 = [' ']
    grid_c3 = [' ']
    print(str(grid_a1).translate(translation) + ' ' + str(grid_a2).translate(translation) + ' ' + str(grid_a3).translate(translation))
    print(str(grid_b1).translate(translation) + ' ' + str(grid_b2).translate(translation) + ' ' + str(grid_b3).translate(translation))
    print(str(grid_c1).translate(translation) + ' ' + str(grid_c2).translate(translation) + ' ' + str(grid_c3).translate(translation))

create_grid()
#Create holding list for X and O choices
choice_list = ['X','O']
#List to hold r key for rolling
roll_list = ['r']

class Player:

    def __init__(self):
        #Ask each player for their name
        player1 = input('Input name for player 1.\n')
        player2 = input('Input name for player 2.\n')
        self.player1 = player1
        self.player2 = player2

    def player_order(self,player1,player2):
        def reroll():
            print('Both players rolled the same number so roll again!')
            roll1 = input(player1 + ' enter r to roll: ')
            if roll1 == 'r':
                player1_roll = random.randint(1,6)
                print(player1 + ' got a ' + str(player1_roll))

            roll2 = input(player2 + ' enter r to roll: ')

            if roll2 == 'r':
                player2_roll = random.randint(1,6)
                print(player2 + ' got a ' + str(player2_roll))

        print('Whoever rolls the highest gets to play first and pick X or O')

        roll1 = input(player1 + ' enter r to roll: ')
        while roll1 not in roll_list:
            roll1 = input(player2 + ' enter r to roll: ')

        if roll1 == 'r':
            player1_roll = random.randint(1,6)
            print(player1 + ' got a ' + str(player1_roll))

        roll2 = input(player2 + ' enter r to roll: ')
        while roll2 not in roll_list:
            roll2 = input(player2 + ' enter r to roll: ')

        if roll2 == 'r':
            player2_roll = random.randint(1,6)
            print(player2 + ' got a ' + str(player2_roll))
        

        print('')

        def roll_win(player1_roll,player2_roll):
            if player1_roll > player2_roll:
                print(player1 + ' is going first')
                choice = input("Do you want X or O(In caps please): ")
                while choice not in choice_list:
                    choice = input("Do you want X or O(In caps please): ")
                if choice == 'X':
                    self.crosses = 1
                    self.noughts = 2
                elif choice == 'O':
                    self.crosses = 2
                    self.noughts = 1
            elif player1_roll < player2_roll:
                print(player2 + ' is going first')
                choice = input("Do you want X or O(In caps please): ")
                while choice not in choice_list:
                    choice = input("Do you want X or O(In caps please): ")
                if choice == 'X':
                    self.crosses = 1
                    self.noughts = 2
                elif choice == 'O':
                    self.crosses = 2
                    self.noughts = 1
            elif player1_roll == player2_roll:
                reroll()
                roll_win(player1_roll,player2_roll)

        roll_win(player1_roll,player2_roll)
    



#Call function player_order from class player
player = Player()
player1 = player.player1
player2 = player.player2
player.player_order(player1,player2)
if player.crosses == 1:
    first = player.crosses
    second = player.noughts
elif player.noughts == 1:
    first = player.noughts
    second = player.crosses
#print(player.noughts)
#print(player.crosses)