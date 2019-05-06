"""
Battleship game which you can play with your friend through network
"""


__all__ = []
__version__ = "0.1"
__author__ = "Timo Mehto"


from classes import *
import os


def main():
    # Create players and their grids
    p1 = Player(name="Esko")
    p1.grid.create_grids()

    p2 = Player(name="Matti")
    p2.grid.create_grids()
    
    # Print the initial grids to the screen
    print('---------- ---------- Player 1 ---------- ----------')
    print()
    p1.grid.draw_grids()
    print('---------- ---------- ---------- ---------- ----------')
    print()

    print('---------- ---------- Player 2 ---------- ----------')
    print()
    p2.grid.draw_grids()
    print('---------- ---------- ---------- ---------- ----------')
    print()

    # Deploy Player 1's ships to the grid
    for ship in p1.ships:
        while True:
            print(f"{p1.name}}, deploy your {ship.ship_class} [{ship.length}]")
            print("Enter the start and the end coordinates of the ship")
            start = input("Starting coordinate > ")
            end = input("Ending coordinate > ")

            # Checks if the input is valid +++ and if the grid is free
            if Grid.valid_coordinates(start, end, ship):
                p1.grid.deploy_ship(start, end, ship)
                print(f'{ship.ship_class} successfully deployed to {ship.location}!')
                break
            else:
                print("~~~~~~~~~~ Invalid input! ~~~~~~~~~~")
        
    # Deploy Player 2's ships to the grid
    for ship in p2.ships:
        while True:
            print(f"{p2.name}}, deploy your {ship.ship_class} [{ship.length}]")
            print("Enter the start and the end coordinates of the ship")
            start = input("Starting coordinate > ")
            end = input("Ending coordinate > ")

            # Checks if the input is valid +++ and if the grid is free
            if Grid.valid_coordinates(start, end, ship):
                p1.grid.deploy_ship(start, end, ship)
                print(f'{ship.ship_class} successfully deployed to {ship.location}!')
                break
            else:
                print("~~~~~~~~~~ Invalid input! ~~~~~~~~~~")

    # Print the grids with the deployed boats
    print('---------- ---------- Player 1 ---------- ----------')
    print()
    p1.grid.draw_grids()
    print('---------- ---------- ---------- ---------- ----------')
    print()

    print('---------- ---------- Player 2 ---------- ----------')
    print()
    p2.grid.draw_grids()
    print('---------- ---------- ---------- ---------- ----------')
    print()
    
    # Shoot for your lives
    run = True
    while run:
        # Player 1 shoots
        shot = input('Player 1 shoots > ')
        if shot == '':
            run = False
        
        os.system('cls')

        Grid.shot(shot, p2.grid.primary, p1.grid.tracking)

        print('---------- ---------- ---------- ---------- Player 1 ---------- ---------- ---------- ----------')
        print()
        p1.grid.draw_grids()
        print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
        print()
        
        print('---------- ---------- ---------- ---------- Player 2 ---------- ---------- ---------- ----------')
        print()
        p2.grid.draw_grids()
        print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
        print()

        # Player 2 shoots
        shot = input('Player 2 shoots > ')
        if shot == '':
            run = False
        
        os.system('cls')

        Grid.shot(shot, p1.grid.primary, p2.grid.tracking)

        print('---------- ---------- ---------- ---------- Player 1 ---------- ---------- ---------- ----------')
        print()
        p1.grid.draw_grids()
        print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
        print()
        
        print('---------- ---------- ---------- ---------- Player 2 ---------- ---------- ---------- ----------')
        print()
        p2.grid.draw_grids()
        print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
        print()


if __name__ == "__main__":
    main()