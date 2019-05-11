import os
import random

class Game:
    """ Class which would work as a game engine for the game """

    def __init__(self, players):
        self.players = players
    
    
    def valid_deployment(start, end, ship, ships):
        """
        Checks whether the coordinates are already occupied and if not,
        adds the coordinates to the ship location
        
        - Checks if the coordinates itself are valid or not
        - Checks if the distance between coordinates is right
        - Checks if the x- or y-coordinates are the same
        - Checks if the xy- or yx-coordinates are input the other way around
        - Checks if the input coordinate is already found on ships locations
        - If found, return False and reset ships location, else add it to ships location
        """
        # TODO: Is there easier way to check for occupied squares?

        if Game.valid_coordinate(start) and Game.valid_coordinate(end):
            if abs(ord(end[0]) - ord(start[0])) == ship.length - 1 or \
                abs(int(end[1:]) - int(start[1:])) == ship.length - 1:
                if start[0] == end[0]:
                    if int(start[1:]) > int(end[1:]):
                        for i in range(ship.length):
                            for s in ships:
                                if start[0] + str(int(end[1:]) + i) in s.location:
                                    ship.location = []
                                    return False
                            ship.location.append(start[0] + str(int(end[1:]) + i))
                        return True
                    else:
                        for i in range(ship.length):
                            for s in ships:
                                if start[0] + str(int(start[1:]) + i) in s.location:
                                    ship.location = []
                                    return False
                            ship.location.append(start[0] + str(int(start[1:]) + i))
                        return True
                elif start[1:] == end[1:]:
                    if ord(start[0]) > ord(end[0]):
                        for i in range(ship.length):
                            for s in ships:
                                if chr(ord(end[0]) + i) + start[1:] in s.location:
                                    ship.location = []
                                    return False
                            ship.location.append(chr(ord(end[0]) + i) + start[1:])
                        return True
                    else:
                        for i in range(ship.length):
                            for s in ships:
                                if chr(ord(start[0]) + i) + start[1:] in s.location:
                                    ship.location = []
                                    return False
                            ship.location.append(chr(ord(start[0]) + i) + start[1:])
                        return True

    
    def valid_coordinate(coordinate):
        """ Checks if the players input coordinate is valid or not """

        if len(coordinate) < 2:
            return False
        if coordinate[0] in Grid.GRID_X and coordinate[1:] in Grid.GRID_Y:
            return True


    def draw_first_blood(self):
        """ Does a coin toss which defines the player who starts the game """

        flip = random.randint(0, 1)
        if flip == 1:
            self.players[0].turn = True
        else:
            self.players[1].turn = True

    
    def shot_result(self, shot):
        """ Makes the changes to the grid according to the shot result """

        if self.players[0].turn:
            for j in range(len(Grid.GRID_X)):
                for i in range(len(Grid.GRID_Y)):
                    if self.players[1].grid.primary[j][i].x + \
                        self.players[1].grid.primary[j][i].y == shot:
                        if self.players[1].grid.primary[j][i].state == Grid.EMPTY:
                            self.players[1].grid.primary[j][i].state = Grid.MISS
                            self.players[0].grid.tracking[j][i].state = Grid.MISS
                            return None
                        elif self.players[1].grid.primary[j][i].state == Grid.SHIP:
                            ship = self.players[1].grid.primary[j][i].ship
                            self.players[1].grid.primary[j][i].state = Grid.SHIP_HIT
                            self.players[1].grid.primary[j][i].ship = None
                            self.players[0].grid.tracking[j][i].state = Grid.HIT
                            return ship
        else:
            for j in range(len(Grid.GRID_X)):
                for i in range(len(Grid.GRID_Y)):
                    if self.players[0].grid.primary[j][i].x + \
                        self.players[0].grid.primary[j][i].y == shot:
                        if self.players[0].grid.primary[j][i].state == Grid.EMPTY:
                            self.players[0].grid.primary[j][i].state = Grid.MISS
                            self.players[1].grid.tracking[j][i].state = Grid.MISS
                            return None
                        elif self.players[0].grid.primary[j][i].state == Grid.SHIP:
                            ship = self.players[0].grid.primary[j][i].ship
                            self.players[0].grid.primary[j][i].state = Grid.SHIP_HIT
                            self.players[0].grid.primary[j][i].ship = None
                            self.players[1].grid.tracking[j][i].state = Grid.HIT
                            return ship
    
    
    def change_turns(self):
        """ Changes the player turn """

        if self.players[0].turn == True:
            self.players[0].turn = False
            self.players[1].turn = True
        else:
            self.players[0].turn = True
            self.players[1].turn = False
    
    
    def game_over(self):
        """ Checks if player has lost after opponents shot thus ending the game """

        for player in self.players:
            if len(player.ships) == 0:
                player.winner = False
                return True


    def draw_grids(player):
        """ Draws the players grids to the screen """

        os.system('cls')
        print(f'---------- ---------- ---------- ---------- {player.name} ---------- ---------- ---------- ----------')
        print('\t\t Primary Grid \t\t\t\t\t\t Tracking Grid')
        print()
        print(Game.build_grids(player.grid))
        print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
        print()
    

    def build_grids(player_grid):
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
                        grid += f'_{player_grid.primary[i - 1][j - 1].state}_|'
                        row_tracking += f'_{player_grid.tracking[i - 1][j - 1].state}_|'
                if j == len(Grid.GRID_X):
                    grid += '\t\t'
                    grid += row_tracking
                    grid += '\n'
                    row_tracking = ''

        return grid

    
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
            [Square(Grid.GRID_X[i], Grid.GRID_Y[j], Grid.EMPTY) \
                for i in range(len(Grid.GRID_X))] \
                    for j in range(len(Grid.GRID_Y))
                    ]
        self.tracking = [
            [Square(Grid.GRID_X[i], Grid.GRID_Y[j], Grid.EMPTY) \
                for i in range(len(Grid.GRID_X))] \
                    for j in range(len(Grid.GRID_Y))
                    ]


    def deploy_ship(self, ship):
        """ Places the ship to the players primary grid """

        for c in range(len(ship.location)):
            for i in range(len(self.primary)):
                for j in range(len(self.primary)):
                    if self.primary[i][j].x == ship.location[c][0] and \
                        self.primary[i][j].y == ship.location[c][1:]:
                        self.primary[i][j].state = Grid.SHIP
                        self.primary[i][j].ship = ship
        

class Square:
    """ Class for the square of the grid """

    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state
        self.ship = None


class Ship:
    """ Main class for ship functions """

    def sunk(self):
        if len(self.location) == 0:
            return True
    
    def make_damage(self, shot):
        self.location.remove(shot)


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
    """ Class for the player information """

    def __init__(self, name):
        self.name = name
        self.ships = [Carrier(), Battleship(), Cruiser(), Submarine(), Destroyer()]
        self.grid = Grid()
        self.turn = False
        self.winner = True