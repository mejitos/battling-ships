"""
Battleship game which you can play with your friend through network
"""


__all__ = []
__version__ = "0.1"
__author__ = "Timo Mehto"


from classes import *
import os


def main():
    # Create players grids. Each player needs primary grid and target grid
    p1_primary = Grid().create_grid(Grid.grid_x, Grid.grid_y)
    p1_target = Grid().create_grid(Grid.grid_x, Grid.grid_y)

    p2_primary = Grid().create_grid(Grid.grid_x, Grid.grid_y)
    p2_target = Grid().create_grid(Grid.grid_x, Grid.grid_y)
    
    # Print the initial grids to the screen
    print('---------- ---------- Player 1 ---------- ----------')
    print()
    Grid.draw_grids(p1_primary, p1_target)
    print('---------- ---------- ---------- ---------- ----------')
    print()

    print('---------- ---------- Player 2 ---------- ----------')
    print()
    Grid.draw_grids(p2_primary, p2_target)
    print('---------- ---------- ---------- ---------- ----------')
    print()

    run = True
    while run:
        # Player 1 shoots
        shot = input('Player 1 shoots > ')
        if shot == '':
            run = False
        
        os.system('cls')

        Grid.shot(shot, p2_primary, p1_target)

        print('---------- ---------- Player 1 ---------- ----------')
        print()
        Grid.draw_grids(p1_primary, p1_target)
        print('---------- ---------- ---------- ---------- ----------')
        print()
        
        print('---------- ---------- Player 2 ---------- ----------')
        print()
        Grid.draw_grids(p2_primary, p2_target)
        print('---------- ---------- ---------- ---------- ----------')
        print()

        # Player 2 shoots
        shot = input('Player 2 shoots > ')
        if shot == '':
            run = False
        
        os.system('cls')

        Grid.shot(shot, p1_primary, p2_target)

        print('---------- ---------- ---------- ---------- Player 1 ---------- ---------- ---------- ----------')
        print()
        Grid.draw_grids(p1_primary, p1_target)
        print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
        print()
        
        print('---------- ---------- ---------- ---------- Player 2 ---------- ---------- ---------- ----------')
        print()
        Grid.draw_grids(p2_primary, p2_target)
        print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
        print()


if __name__ == "__main__":
    main()