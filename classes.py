class Grid:
    """ Class for the grids """
    
    # Grid x- and y-axis
    GRID_X = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J']
    GRID_Y = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    # Icons for the primary and tracking grids
    EMPTY = ' '
    SHIP = '#'
    SHIP_HIT = '@'
    HIT = 'X'
    MISS = 'O'


    def __init__(self):
        self.primary = [[], [], [], [], [], [], [], [], [], []]
        self.tracking = [[], [], [], [], [], [], [], [], [], []]
    

    def create_grids(self):
        for j in range(len(Grid.GRID_Y)):
            for i in range(len(Grid.GRID_X)):
                sp = Square(Grid.GRID_X[i], Grid.GRID_Y[j], Grid.EMPTY)
                self.primary[j].append(sp)
                st = Square(Grid.GRID_X[i], Grid.GRID_Y[j], Grid.EMPTY)
                self.tracking[j].append(st)


    def draw_grids(self):
        """ Draws the primary grid and the tracking grid to the screen """

        grid = [[], [], [], [], [], [], [], [], [], [], []]

        for i in range(2):
            for col in range(len(grid)):
                for row in range(len(grid)):
                    # Add the empty corner
                    if col == 0 and row == 0:
                        grid[col].append(f'___|')
                    # Add the first column
                    if col == 0 and row <= len(Grid.GRID_Y) - 1:
                        if row + 1 == len(Grid.GRID_Y):
                            grid[row+1].append('10_|')
                        else:
                            grid[row + 1].append(f'_{Grid.GRID_Y[row]}_|')
                    # Add the top row
                    if row == 0 and col <= len(Grid.GRID_X) - 1:
                        grid[row].append(f'_{Grid.GRID_X[col]}_|')
                        # Tab for the next grid
                        if col == len(Grid.GRID_X) - 1:
                            grid[row].append('\t\t')
                    # Add the rest of the grid with square state
                    if col >= 1 and row >= 1:
                        if i == 0:                        
                            grid[col].append(f'_{self.primary[col - 1][row - 1].state}_|')
                        else:
                            grid[col].append(f'_{self.tracking[col - 1][row - 1].state}_|')
                    # Tab for the next grid
                    if row == 10 and col >= 1 and col <= 10:    
                        grid[col].append('\t\t')

        print('\t\t Primary Grid \t\t\t\t\t\t Target Grid')
        print()
        for row in grid:
            print(''.join(row))

    
    def shot(shot, primary, tracking):
        for j in range(len(primary)):
            for i in range(len(primary[j])):
                if primary[j][i].x + primary[j][i].y == shot:
                    if primary[j][i].state == Grid.EMPTY:
                        primary[j][i].state = Grid.MISS
                        tracking[j][i].state = Grid.MISS
                    elif primary[j][i].state == Grid.SHIP:
                        primary[j][i].state = Grid.SHIP_HIT
                        tracking[j][i].state = Grid.HIT
                        # update to ship state = hit location = remove or change to '@'

    
    def validate_shot(shot):
        pass


    def deploy_ship(self, start, end, ship):
        """ Places the ship to the grid """

        start_x = start[0]
        start_y = start[1:]
        end_x = end[0]
        end_y = end[1:]

        # if the X-coordinates are the same, then
        if start_x == end_x:
            # Check if the Y-coordinates are wrong way
            if int(start_y) > int(end_y):
                for i in range(ship.length):
                    ship.location.append(start_x + str(int(end_y) + i))
            else:
                for i in range(ship.length):
                    ship.location.append(start_x + str(int(start_y) + i))
        # if the Y-coordinates are the same, then
        elif start_y == end_y:
            # Check if the X-coordinates are wrong way
            if ord(start_x) > ord(end_x):
                for i in range(ship.length):
                    ship.location.append(chr(ord(end_x) + i) + start_y)
            else:
                for i in range(ship.length):
                    ship.location.append(chr(ord(start_x) + i) + start_y)
        
        # Deploys the ship to the players primary grid
        for c in range(len(ship.location)):
            for i in range(len(self.primary)):
                for j in range(len(self.primary)):
                    if self.primary[i][j].x == ship.location[c][0] and self.primary[i][j].y == ship.location[c][1:]:
                        self.primary[i][j].state = Grid.SHIP
                        self.primary[i][j].ship = ship


    # TODO: Grid check function - can_be_deployed()


    # better name would be somekind of input validating function
    def valid_coordinates(start, end, ship):
        """ Checks if the ship can be placed to the spot players wants """

        # Check if the length of the inputs are correct
        if (len(start) == 2 and len(end) == 2) or (start[1:] == '10' or end[1:] == '10'):
            # Checks if the starting coordinate is valid
            if start[0] in Grid.GRID_X and start[1:] in Grid.GRID_Y:
                # Checks if the ending coordinate is valid
                if end[0] in Grid.GRID_X and end[1:] in Grid.GRID_Y:
                    # Checks if the X-coordinates or the Y-coordinates are the same
                    if start[0] == end[0] or start[1:] == end[1:]:
                        # Checks if the distance between the X-coordinates matches the ship length
                        if abs(ord(end[0]) - ord(start[0])) == ship.length - 1:
                            return True
                        # Checks if the distance between the Y-coordinates matches the ship length
                        elif abs(int(end[1:]) - int(start[1:])) == ship.length - 1:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
        


class Square:

    def __init__(self, x, y, state):
        self.x = x
        self.x_num = ord(self.x)
        self.y = y
        self.state = state
        self.ship = None


class Ship:
    """ Main class for all the ships """


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
        self.ship_class = 'Carrier'
        self.length = 5
        self.location = []


class Battleship(Ship):
    """ Ship with the size of 4 """
    def __init__(self):
        self.ship_class = 'Battleship'
        self.length = 4
        self.location = [] 


class Cruiser(Ship):
    """ Ship with the size of 3 """
    def __init__(self):
        self.ship_class = 'Cruiser'
        self.length = 3
        self.location = [] 


class Submarine(Ship):
    """ Ship with the size of 3 """
    def __init__(self):
        self.ship_class = 'Submarine'
        self.length = 3
        self.location = [] 


class Destroyer(Ship):
    """ Ship with the size of 2 """
    def __init__(self):
        self.ship_class = 'Destroyer'
        self.length = 2
        self.location = [] 


class Player:

    def __init__(self, name):
        self.name = name
        self.turn = False
        self.ships = [Carrier(), Battleship(), Cruiser(), Submarine(), Destroyer()]
        self.grid = Grid()

    def check_for_win(self):
        """ Checks if player has won after shot and returns true or false"""
        pass