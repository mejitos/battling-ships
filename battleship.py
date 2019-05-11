"""
Battleship game which in the future you can play with your friend through network...
...hopefully
"""

#TODO: Game UI with curses-library
#   maybe "UI-class" to handle all the drawing - just for the learning purposes
#TODO: Make the game work through network - maybe through some simple UDP protocol
#TODO: Make simple AI to play against

__all__ = []
__version__ = "0.1"
__author__ = "Timo Mehto"


from classes import *


def main():
    # Create players and their grids
    players = []
    p1 = Player(input('Player one, please enter your name > '))
    players.append(p1)
    p2 = Player(input('Player two, please enter your name > '))
    players.append(p2)

    # Start the game by initializing it
    bs = Game(players)
    
    # Deploy Players ships to the grid
    # TODO: At the end let player make sure ships are where they want them to be
    #   and give an option to reset them if they want to
    for player in bs.players:
        for ship in player.ships:            
            Game.draw_grids(player)
            print(f"{player.name}, deploy your {ship.ship_class} [{ship.length}]")

            while True:
                print("Enter the start and the end coordinates of the ship")
                start = input("Starting coordinate > ").strip().upper()
                end = input("Ending coordinate > ").strip().upper()

                if Game.valid_deployment(start, end, ship, player.ships):
                    player.grid.deploy_ship(ship)
                    print(f'{ship.ship_class} successfully deployed to {ship.location}!')
                    input('Press ENTER to continue!')
                    break
                else:
                    print('~~~~~~~~~~ Invalid coordinates! ~~~~~~~~~~')
                    input('Press ENTER to continue!')

    # Draw starter here to set up player turns
    bs.draw_first_blood()
    for player in bs.players:
        if player.turn:
            print()
            print(f'{player.name} won the coin toss!')
            input('Press ENTER to start the battle!')

    # Battle time
    while True:        
        for player in bs.players:
            if player.turn:
                Game.draw_grids(player)

                # Player shoots
                while True:
                    shot_coordinate = input(f'{player.name} shoots > ').strip().upper()
                    if Game.valid_coordinate(shot_coordinate):
                        break
                    else:
                        input("~~~~~~~~~~ Invalid coordinate! ~~~~~~~~~~")
                print(f'{player.name} shot to ' + shot_coordinate)

                # Shot hits the opponents grid
                for plr in bs.players:
                    if not plr.turn:
                        print(shot_coordinate)
                        hit = bs.shot_result(shot_coordinate)
                        print(hit)
                        if hit in plr.ships:
                            hit.make_damage(shot_coordinate)
                            print(f'{plr.name}: Hit!')
                            if hit.sunk():
                                plr.ships.remove(hit)
                                print(f'{plr.name}: You sunk my battlehsip!')
                        else:
                            print(f'{plr.name}: Miss!')
        
        input('Press ENTER to advance')

        # Check for game over, if not, change player turns
        if bs.game_over():
            break
        else:
            bs.change_turns()
        
    # Declare winner
    for player in bs.players:
        if player.winner:
            print()
            print('~~~~~~~~~~ GAME OVER! ~~~~~~~~~~')
            print(f'{player.name} has won the game!')

    # Exit the game
    input("Exit the game by pressing ENTER")

if __name__ == "__main__":
    main()