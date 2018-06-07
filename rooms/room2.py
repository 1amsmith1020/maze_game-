import maze_game.my_maze_utils as utils

import time

import os

from colorama import Fore, Style
# # # # # # # # #
#   Room 2
#       This room can only be gotten too from Room 1
#       You can only go to room 1
#       You can take a key
#       There is nothing to use in this room
room2_inventory = {
    'Green Backpack': 1,
    'Bump Key': 1,
    'Flashlight': 1
}


#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop
def run_room(player_inventory, player_health):
    description = '''
    . . . 
    You are in a brightly lit hallway with rooms identical to yours lining the walls and alarms blaring overhead. 
    Just as you walk in, all the doors begin to close automatically.
    All of a sudden, the lights cut out, as well as the alarms. 
    A few moments later, the lights come back on, but much dimmer, the alarms come back to life, more deafening than ever. At the end of the hall on the SOUTH side, one door is still open.
    To the WEST there is an open door 
    You see a GREEN BACKPACK in the far left corner and a BUMP KEY next to it.
    . . . 
    '''

    print(Fore.BLUE + Style.BRIGHT + description +
          Style.RESET_ALL)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = 1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0]

        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'north':
                next_room = 1
                done_with_room = True
            elif direction == 'south':
                next_room = 6
                done_with_room = True
            elif direction == 'east':
                next_room = 3
                done_with_room = True
            elif direction == 'west':
                next_room = 4
                done_with_room = True

            else:
                # In this room, there is nowhere else to go.
                print('. . . ')
        elif the_command == 'take':
            take_what = response[1].title()
            utils.take_item( player_inventory, room2_inventory,
                             take_what)
        elif the_command == 'drop':
            drop_what = response[1].title()
            utils.drop_item( player_inventory, room2_inventory,
                         drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory, player_health)
            utils.room_status(room2_inventory)
    else:
        print('You cannot', the_command, 'in this room')

    # end of main while loop
    return next_room

