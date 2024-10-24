#TicTacToe

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

