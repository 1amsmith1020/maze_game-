import maze_game.my_maze_utils as utils

import random

import time

from colorama import Fore, Style


room5_inventory = {

}
is_open = True
# # # # # # # # #
#   Room 5
#       This room can only be gotten too from Room 4
#       You can only go to room 4
#       FLASHLIGHTS have an effect in this room
#       Player can get some health from the water here, nut only one time
#       There is a SHOWER to use here
def run_room(player_inventory, player_health):
    blind = True
    can_use_shower = False
    description = '''It's pitch black in here, you can't even tell what type of room this is.
    Using a FLASHLIGHT would be pretty useful right about now . . . 
    If you don't have a flashlight, you could always EXAMINE the room . . .'''

    print(description)

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
            if direction == 'east':
                next_room = 4
                done_with_room = True
                is_open = False
            else:
                # In this room, there is nowhere else to go.
                print('. . . ')
        elif the_command == 'use':
            use_what = response[1].title()
            if use_what == "Flashlight":
                if 'Flashlight' in player_inventory:
                    blind = False
                    can_use_shower = True
                    print('''You use your FLASHLIGHT. Upon shining it around the room, you quickly discern this room is a bathroom.
                    There are stalls and urinals on one side . . .
                     You shine your light to the other side of the room . . .
                     . . . The other side has a few showers. Using the SHOWER to get some water doesn't seem like such a bad idea . . .''')
                else:
                    print('You cannot use that here')
            if use_what == 'Shower' and can_use_shower:
                player_health = player_health + 20
                print('The water quenches your thirst and gives you extra strength. You now have', player_health, 'health. However, now the shower is out of water.')
                can_use_shower = False
            else:
                print('You cant use that here. . . ')
        elif the_command == 'take':
            take_what = response[1].title()
            utils.take_item(player_inventory, room5_inventory,
                            take_what)
        elif the_command == 'drop':
            drop_what = response[1].title()
            utils.drop_item(player_inventory, room5_inventory,
                            drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory, player_health)
            utils.room_status(room5_inventory)
        elif the_command == 'examine':
            injury_chance = random.randint(0, 4)
            if injury_chance == 1 or 2:
                print('''You slam your head into a nearby wall. You storm out of the room, slamming the door shut as you go.
                You quickly realize the door locked behind you.''')
                player_health = player_health - 5
                next_room = 4
                done_with_room = True
                is_open = False
            else:
                print('''You use your hands to guide you along the edge of the bathroom. You reach a corner and you feel a handle.
                Upon turning it you realize it is a SHOWER. You can now use the SHOWER.''')
                can_use_shower = True
    else:
        print('You cannot do that in this room')

    # end of main while loop
    return next_room