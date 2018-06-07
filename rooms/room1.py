import maze_game.my_maze_utils as utils

import time

import os

from colorama import Fore, Style



room1_inventory = {

}
room_state = {
    'door_locked': True
}
#HOW TO USE TIME
##### time.sleep(1.5)
# # # # # # # # # # # # # # #
#  This is the main room you will start in.
#
#  GO: From this room you can get to Room 2 (SOUTH) and Room 1 (East)
#  Take: There is nothing to take in this room
#  Use: There is nothing to use in this room
#
def run_room(player_inventory, player_health):
    description = '''
    . . . Main Room . . .
    You open your eyes. The padded room you see is unfamiliar. Red light coming from flashes on and off, you hear alarms blaring and shouting in the distance.
    You see the heavy metal door in your room has been opened to the outside. You see a brightly lit doorway to the SOUTH. 

    '''
    print(Fore.BLUE + Style.BRIGHT + description +
          Style.RESET_ALL)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help", "die"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0]
        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'south':
                print('. . . ')
                time.sleep(.75)
                next_room = 2
                done_with_room = True

            else:
                print('You cannot go that way')
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)
        elif the_command == 'take':
            print("There is nothing to take here.")
        elif the_command == 'drop':
            drop_what = response[1]
            utils.scrub_response(drop_what)
            if drop_what in player_inventory.keys():
                del player_inventory[drop_what]
                print("You no longer possess,", drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory, player_health)
            utils.room_status(room1_inventory)
        else:
            print('unkown command:', the_command)

    # end of while loop
    return next_room
