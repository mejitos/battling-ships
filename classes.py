class Grid:
    """ Class for the grids """
    
    # Grid x- and y-axis
    grid_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J']
    grid_y = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    # Icons for the primary and target grids
    empty = ' '
    ship = '#'
    hit = '@'
    trgt_hit = 'X'
    trgt_miss = 'O'


    def __init__(self):
        self.grid = [[], [], [], [], [], [], [], [], [], []]
    

    def create_grid(self, x, y):
        grid = [[], [], [], [], [], [], [], [], [], []]
        
        for j in range(len(y)):
            for i in range(len(x)):
                s = Square(x[i], y[j], ' ')
                grid[j].append(s)
        return grid


    def draw_grids(primary, target):
        """ Draws the primary grid and the target grid to the screen """

        grid = [[], [], [], [], [], [], [], [], [], [], []]

        for i in range(2):
            for col in range(len(grid)):
                for row in range(len(grid)):
                    # Add the empty corner
                    if col == 0 and row == 0:
                        grid[col].append(f'___|')
                    # Add the first column
                    if col == 0 and row <= len(Grid.grid_y) - 1:
                        if row + 1 == len(Grid.grid_y):
                            grid[row+1].append('10_|')
                        else:
                            grid[row + 1].append(f'_{Grid.grid_y[row]}_|')
                    # Add the top row
                    if row == 0 and col <= len(Grid.grid_x) - 1:
                        grid[row].append(f'_{Grid.grid_x[col]}_|')
                        # Tab for the next grid
                        if col == len(Grid.grid_x) - 1:
                            grid[row].append('\t\t')
                    # Add the rest of the grid with square state
                    if col >= 1 and row >= 1:
                        if i == 0:                        
                            grid[col].append(f'_{primary[col - 1][row - 1].state}_|')
                        else:
                            grid[col].append(f'_{target[col - 1][row - 1].state}_|')
                    # Tab for the next grid
                    if row == 10 and col >= 1 and col <= 10:    
                        grid[col].append('\t\t')

        print('\t\t Primary Grid \t\t\t\t\t\t Target Grid')
        print()
        for row in grid:
            print(''.join(row))

    
    def shot(shot, primary, target):
        for j in range(len(primary)):
            for i in range(len(primary[j])):
                if primary[j][i].x + primary[j][i].y == shot:
                    if primary[j][i].state == ' ':
                        primary[j][i].state = 'O'
                        target[j][i].state = 'O'
                    elif primary[j][i].state == '#':
                        primary[j][i].state = '@'
                        target[j][i].state = 'X'


    def deploy_ship(self):
        """ Places the ship to the grid if it can be placecd """
        pass


    def can_be_deployed(self):
        """ Checks if the ship can be placed to the spot players wants """
        pass


class Square:

    def __init__(self, x, y, state):
        self.x = x
        self.x_num = ord(self.x)
        self.y = y
        self.state = state
        #self.ship = ship


class Ship:
    """ Main class for all the ships """

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.location = []
    
    def is_sunk(self):
        """ Checks if ship is sunk and returns true or false """
        for x in self.location:
            if x.state == '#':
                return False
        #return True
        print("You sunk my battleship!")

    def is_hit(self, shot):
        """ Checks if players shot hit the ship and returns true or false """

        for loc in self.location:
            if shot == loc:
                #return True
                print("Hit") # remove from list? update to list as a '@'? return something?
            else:
                #return False
                print("Miss") # return something?


class Carrier(Ship):
    """ Ship with the size of 5 """
    def __init__(self):
        self.location = [Square, Square, Square, Square, Square] # laivojen pitäisi täyttyä koordinaateista


class Battleship(Ship):
    """ Ship with the size of 4 """
    def __init__(self):
        self.location = [Square, Square, Square, Square] 


class Cruiser(Ship):
    """ Ship with the size of 3 """
    def __init__(self):
        self.location = [Square, Square, Square] 


class Submarine(Ship):
    """ Ship with the size of 3 """
    def __init__(self):
        self.location = [Square, Square, Square] 


class Destroyer(Ship):
    """ Ship with the size of 2 """
    def __init__(self):
        self.location = [Square, Square] 


class Player:

    def __init__(self, name):
        self.name = name
        self.turn = False
        self.ships = [Carrier, Battleship, Cruiser, Submarine, Destroyer]
        self.shot = None

    def check_for_win(self):
        """ Checks if player has won after shot and returns true or false"""

        for ship in self.ships:
            for x in ship:
                if x == intact:
                    return
        print("LOSER")