class GameState:
    """ Class which would work as a game engine for the game """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    
    

    
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
        self.primary = [
            [Square(Grid.GRID_X[i], Grid.GRID_Y[j], Grid.EMPTY) for i in range(len(Grid.GRID_X))] \
            for j in range(len(Grid.GRID_Y))]
        self.tracking = [
            [Grid.EMPTY for i in range(len(Grid.GRID_X))] \
            for j in range(len(Grid.GRID_Y))]

    
    def draw_grids(self):
        """ Returns a single string of the players primary and tracking grids """

        grid = ''
        row_tracking = ''
        
        for i in range(len(Grid.GRID_X) + 1):
            for j in range(len(Grid.GRID_Y) + 1):
                if i == 0:
                    if j == 0:
                        grid += '___|'
                        row_tracking += '___|'
                    if j >= 1:
                        grid += f'_{Grid.GRID_X[j - 1]}_|'
                        row_tracking += f'_{Grid.GRID_X[j - 1]}_|'
                if i > 0:
                    if j == 0:
                        if i < len(Grid.GRID_Y):
                            grid += f'_{Grid.GRID_Y[i - 1]}_|'
                            row_tracking += f'_{Grid.GRID_Y[i - 1]}_|'
                        if i == len(Grid.GRID_Y):
                            grid += f'{Grid.GRID_Y[i - 1]}_|'
                            row_tracking += f'{Grid.GRID_Y[i - 1]}_|'
                    if j >= 1:
                        grid += f'_{self.primary[i - 1][j - 1].state}_|'
                        row_tracking += f'_{Grid.EMPTY}_|'
                if j == len(Grid.GRID_X):
                    grid += '\t\t'
                    grid += row_tracking
                    grid += '\n'
                    row_tracking = ''

        return grid

    
    def shot(shot, primary, tracking):
        """ Changes the state of the shot square accordingly """

        for j in range(len(primary)):
            for i in range(len(primary[j])):
                if primary[j][i].x + primary[j][i].y == shot:
                    if primary[j][i].state == Grid.EMPTY:
                        primary[j][i].state = Grid.MISS
                        tracking[j][i] = Grid.MISS
                    elif primary[j][i].state == Grid.SHIP:
                        primary[j][i].state = Grid.SHIP_HIT
                        primary[j][i].ship.location.remove(shot)
                        primary[j][i].ship = None
                        tracking[j][i] = Grid.HIT

    
    def validate_shot(shot):
        """ Checks if the player input shot coordinates are valid"""

        if len(shot) == 2 or shot[1:] == '10':
            if shot[0] in Grid.GRID_X and shot[1:] in Grid.GRID_Y:
                return True
            else:
                return False
        else:
            return False


    def deploy_ship(self, ship):
        """ Places the ship to the players primary grid """

        for c in range(len(ship.location)):
            for i in range(len(self.primary)):
                for j in range(len(self.primary)):
                    if self.primary[i][j].x == ship.location[c][0] and self.primary[i][j].y == ship.location[c][1:]:
                        self.primary[i][j].state = Grid.SHIP
                        self.primary[i][j].ship = ship


    def can_be_deployed(start, end, ship, ships):
        """
        Checks whether the coordinates are already occupied and if not,
        adds the coordinates to the ship location
        """

        # Starting and ending coordinates of the ship
        start_x = start[0]
        start_y = start[1:]
        end_x = end[0]
        end_y = end[1:]

        """
        - Checks if the x- or y-coordinates are the same
        - Checks if the xy- or yx-coordinates are input the other way around
        - Checks if the input coordinate is already found on ships locations
        - If found, return False
        - If coordinate not on ships, add it to ships location
        """
        if start_x == end_x:
            if int(start_y) > int(end_y):
                for i in range(ship.length):
                    for s in ships:
                        if start_x + str(int(end_y) + i) in s.location:
                            ship.location = []
                            return False
                    ship.location.append(start_x + str(int(end_y) + i))
                return True
            else:
                for i in range(ship.length):
                    for s in ships:
                        if start_x + str(int(start_y) + i) in s.location:
                            ship.location = []
                            return False
                    ship.location.append(start_x + str(int(start_y) + i))
                return True
        elif start_y == end_y:
            if ord(start_x) > ord(end_x):
                for i in range(ship.length):
                    for s in ships:
                        if chr(ord(end_x) + i) + start_y in s.location:
                            ship.location = []
                            return False
                    ship.location.append(chr(ord(end_x) + i) + start_y)
                return True
            else:
                for i in range(ship.length):
                    for s in ships:
                        if chr(ord(start_x) + i) + start_y in s.location:
                            ship.location = []
                            return False
                    ship.location.append(chr(ord(start_x) + i) + start_y)
                return True


    def valid_coordinates(start, end, ship):
        """
        Checks if players input coordinates are valid or not by checking:
        - if the length of the inputs are correct or if the y is 10
        - if the starting coordinate is valid
        - if the ending coordinate is valid
        - if the x- or y-coordinates are the same
        - if the distance between x- or y-coordinates matches the ship length
        """

        if (len(start) == 2 and len(end) == 2) or (start[1:] == '10' or end[1:] == '10'):
            if start[0] in Grid.GRID_X and start[1:] in Grid.GRID_Y:
                if end[0] in Grid.GRID_X and end[1:] in Grid.GRID_Y:
                    if start[0] == end[0] or start[1:] == end[1:]:
                        if abs(ord(end[0]) - ord(start[0])) == ship.length - 1:
                            return True
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
    """ Class for the square of the grid """

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.ship = None


class Carrier():
    """ Ship with the size of 5 """

    def __init__(self):
        self.ship_class = 'Carrier'
        self.length = 5
        self.location = []


class Battleship():
    """ Ship with the size of 4 """

    def __init__(self):
        self.ship_class = 'Battleship'
        self.length = 4
        self.location = [] 


class Cruiser():
    """ Ship with the size of 3 """

    def __init__(self):
        self.ship_class = 'Cruiser'
        self.length = 3
        self.location = [] 


class Submarine():
    """ Ship with the size of 3 """

    def __init__(self):
        self.ship_class = 'Submarine'
        self.length = 3
        self.location = [] 


class Destroyer():
    """ Ship with the size of 2 """

    def __init__(self):
        self.ship_class = 'Destroyer'
        self.length = 2
        self.location = [] 


class Player:
    """ Class for the player information """

    def __init__(self, name):
        self.name = name
        self.turn = False
        self.ships = [Carrier(), Battleship(), Cruiser(), Submarine(), Destroyer()]
        self.grid = Grid()

    def has_lost(self):
        """ Checks if player has lost after opponents shot """

        if len(self.ships) == 0:
            return True

    def is_sunk(self):
        """ Checks whether a ship in players ships has sunk """

        for ship in self.ships:
            if len(ship.location) == 0:
                self.ships.remove(ship)
                return True