"""
Battleship game which in the future you can play with your friend through network...
...hopefully
"""

#TODO: Need to make some sense to all the classes and their functions
#TODO: Somekind of GameState class to instatiate and control the game
#TODO: "UI"-class to handle all the drawing - just for the learning purposes
#TODO: Make the game work through network - maybe through some simple UDP protocol
#TODO: Make simple AI to play against

__all__ = []
__version__ = "0.1"
__author__ = "Timo Mehto"


from classes import *
import os


def main():
    # Create players and their grids
    p1 = Player(name="Esko")
    p2 = Player(name="Matti")
    
    # Deploy Player 1's ships to the grid
    for ship in p1.ships:
        while True:
            print('---------- ---------- ---------- ---------- Player 1 ---------- ---------- ---------- ----------')
            print()
            print(p1.grid.draw_grids())
            print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
            print()
            print(f"{p1.name}, deploy your {ship.ship_class} [{ship.length}]")
            print("Enter the start and the end coordinates of the ship")
            start = input("Starting coordinate > ")
            end = input("Ending coordinate > ")

            if Grid.valid_coordinates(start, end, ship) and \
                Grid.can_be_deployed(start, end, ship, p1.ships):

                p1.grid.deploy_ship(ship)
                print(f'{ship.ship_class} successfully deployed to {ship.location}!')
                break
            else:
                print("~~~~~~~~~~ Invalid input! ~~~~~~~~~~")
        
    # Deploy Player 2's ships to the grid
    for ship in p2.ships:
        while True:
            print('---------- ---------- ---------- ---------- Player 2 ---------- ---------- ---------- ----------')
            print()
            print(p2.grid.draw_grids())
            print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
            print()
            print(f"{p2.name}, deploy your {ship.ship_class} [{ship.length}]")
            print("Enter the start and the end coordinates of the ship")
            start = input("Starting coordinate > ")
            end = input("Ending coordinate > ")

            if Grid.valid_coordinates(start, end, ship) and \
                Grid.can_be_deployed(start, end, ship, p2.ships):

                p2.grid.deploy_ship(ship)
                print(f'{ship.ship_class} successfully deployed to {ship.location}!')
                break
            else:
                print("~~~~~~~~~~ Invalid input! ~~~~~~~~~~")

    
    # Shoot for your lives
    while True:        
        # Player 1's turn
        while True:
            os.system('cls')

            print('---------- ---------- ---------- ---------- Player 1 ---------- ---------- ---------- ----------')
            print()
            print(p1.grid.draw_grids())
            print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
            print()
            
            print('---------- ---------- ---------- ---------- Player 2 ---------- ---------- ---------- ----------')
            print()
            print(p2.grid.draw_grids())
            print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
            print()

            # Player 1 shoots
            shot = input('Player 1 shoots > ')
            if Grid.validate_shot(shot):
                break
            else:
                input("~~~~~~~~~~ Invalid input! ~~~~~~~~~~")
        
        os.system('cls')

        Grid.shot(shot, p2.grid.primary, p1.grid.tracking)

        print('---------- ---------- ---------- ---------- Player 1 ---------- ---------- ---------- ----------')
        print()
        print(p1.grid.draw_grids())
        print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
        print()
        
        print('---------- ---------- ---------- ---------- Player 2 ---------- ---------- ---------- ----------')
        print()
        print(p2.grid.draw_grids())
        print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
        print()

        if p2.is_sunk():
            input(f"{p2.name}: You sunk my battleship!")
        
        if p2.has_lost():
            input(f'{p1.name} has won the game')
            break

        # Player 2's turn
        while True:
            os.system('cls')

            print('---------- ---------- ---------- ---------- Player 1 ---------- ---------- ---------- ----------')
            print()
            print(p1.grid.draw_grids())
            print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
            print()
            
            print('---------- ---------- ---------- ---------- Player 2 ---------- ---------- ---------- ----------')
            print()
            print(p2.grid.draw_grids())
            print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
            print()
            
            # Player 2 shoots
            shot = input('Player 2 shoots > ')
            if Grid.validate_shot(shot):
                break
            else:
                input("~~~~~~~~~~ Invalid input! ~~~~~~~~~~")
        
        os.system('cls')

        Grid.shot(shot, p1.grid.primary, p2.grid.tracking)

        print('---------- ---------- ---------- ---------- Player 1 ---------- ---------- ---------- ----------')
        print()
        print(p1.grid.draw_grids())
        print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
        print()
        
        print('---------- ---------- ---------- ---------- Player 2 ---------- ---------- ---------- ----------')
        print()
        print(p2.grid.draw_grids())
        print('---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------')
        print()

        if p1.is_sunk():
            input(f"{p1.name}: You sunk my battleship!")
        
        if p1.has_lost():
            input(f'{p2.name} has won the game')
            break

    input("Exit the game by pressing ENTER")

if __name__ == "__main__":
    main()