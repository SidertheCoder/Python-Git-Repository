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

class Player:

    def __init__(self):
        #Ask each player for their name
        player1 = input('Input name for player 1.\n')
        player2 = input('Input name for player 2.\n')
        self.player1 = player1
        self.player2 = player2

    def player_order(self,player1,player2):
        print('Whoever rolls the highest gets to play first and pick X or O')
        print('')
        roll1 = input(player1 + ' enter r to roll: ')
        if roll1 == 'r':
            player1_roll = random.randint(1,6)
            print(player1 + ' got a ' + str(player1_roll))

        roll2 = input(player2 + ' enter r to roll: ')

        if roll2 == 'r':
            player2_roll = random.randint(1,6)
            print(player2 + ' got a ' + str(player2_roll))

        print('')

        if player1_roll > player2_roll:
            print(player1 + ' is going first')
            #choice = input("Do you want X or O(In caps please): ")
            #if choice == 'X':
                #self.player1 = x
                #choice_list.remove(X)
        else:
            print(player2 + ' is going first')
    



#Call function player_order from class player
player = Player()
player1 = player.player1
player2 = player.player2
player.player_order(player1,player2)
