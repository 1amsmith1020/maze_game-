import maze_game.my_maze_utils as utils

import time

from colorama import Fore, Style


room3_inventory = {
    'Crowbar': 1
}
# # # # #
# ROOM 3
#
# Serves as a good template for blank rooms
item_description = 'There is a CROWBAR laying on the ground near the door. . . '
room3_description = '''
    . . .  3rd room ... 
    You are in a storage room that feels very familiar. There is a CROWBAR laying on the ground near the door. . . 
    There is nothing else of interest in this room'''


def run_room(player_inventory, player_health):
    # Let the user know what the room looks like

    if room3_inventory['Crowbar'] == 0:
        room3_description = '''
    . . .  3rd room ... 
    You are in a storage room that feels very familiar. There is nothing else of interest in this room.'''
        print(room3_description)
    else:
        room3_description = '''
        . . .  3rd room ... 
        You are in a storage room that feels very familiar. There is a CROWBAR laying on the ground near the door. . . 
        There is nothing else of interest in this room'''
        print(room3_description)
    # valid commands for this room
    commands = ["go", "take", "drop", "use", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number,
    # In the loop below the user should eventually ask to "go" somewhere.
    # If they give you a valid direction then set next_room to that value
    next_room = -1

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0]
        # now deal with the command
        if the_command == 'go':
            direction = response[1].lower()
            if direction == 'west':
                next_room = 2
                done_with_room = True

            else:
                print('. . . ')
        elif the_command == 'take':
            take_what = response[1].title()
            utils.take_item( player_inventory, room3_inventory,
                             take_what)
        elif the_command == 'drop':
            drop_what = response[1].title()
            utils.drop_item( player_inventory, room3_inventory,
                         drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory,player_health)
            utils.room_status(room3_inventory)
        else:
            print('The command', the_command, 'is invalid in ROOM3')

    return next_room

