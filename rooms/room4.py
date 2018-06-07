import maze_game.my_maze_utils as utils

import maze_game.rooms.room5 as r5

import time

from colorama import Fore, Style
# This is the locker room
room4_inventory = {
'Flashlight': 1,
'Batteries': 3

}



# # # # # # # # #
#   Room 4
#       This room can only be gotten too from Room 3
#       You can go to room 5 and room 3
#       There is nothing to use in this room
#       You can take BATTERIES and a FLASHLIGHT
#   The player_inventory is expected to be a dictionary, and will be provided by the main game loop
def run_room(player_inventory, player_health):
    description = '''
    . . . 
    In the gloom, you can just make out the outline of rows of lockers lining the room, and one row in the middle. 
    Light reflects off a shiny handle of a FLASHLIGHT and some BATTERIES next to it.
    Behind the row of lockers, there is an open door leading to complete darkness'''

    print(description)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = 0

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        the_command = response[0]

        if the_command == 'go':
            direction = response[1]
            # Use your hand drawn map to help you think about what is valid
            if direction == 'west':
                if r5.is_open == False:
                    print('That room is locked now, you cant get in. . . ')
                else:
                    next_room = 5
                    done_with_room = True
            elif direction == 'east':
                next_room = 2
                done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print('. . . ')
        elif the_command == 'take':
            take_what = response[1].title()
            utils.take_item( player_inventory, room4_inventory,
                             take_what)
        elif the_command == 'drop':
            drop_what = response[1].lower()
            utils.drop_item( player_inventory, room4_inventory,
                         drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory, player_health)
            utils.room_status(room4_inventory)
        else:
            print("Command not implemented in ROOM 2,", the_command)

    # end of main while loop
    return next_room
