import maze_game.my_maze_utils as utils

import time

from colorama import Fore, Style


room7_inventory = {
'Janitor I.D': 1,
'MOP': 1
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
   . . . The room is less like a room and more like a utility closet. . . 
   There is a MOP and a JANITOR I.D. on a hook. . . 
   It looks like there is nothing else of intrest . . . But there is no harm is using your FLASHLIGHT if you have one, right?
   

    '''
    print(Fore.BLUE + Style.BRIGHT + description +
          Style.RESET_ALL)

    # valid commands for this room
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
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
            if direction == 'west':
                print('. . . ')
                time.sleep(.75)
                next_room = 6
                done_with_room = True
            else:
                # In this room, there is nowhere else to go.
                print("There is no way to go,", direction)

        elif the_command == 'take':
            take_what = response[1].title()
            if take_what in room7_inventory:
                utils.take_item(player_inventory, room7_inventory,
                                take_what)
            else:
                print('There is nothing like that in this room')
        elif the_command == 'use':
            use_what = response[1].title()
            if use_what in player_inventory:
                if player_inventory[use_what] > 0:

                    if use_what == 'Flashlight':
                        print('. . .')
                        time.sleep(1.0)
                        print('''The flashlight lights up the room for a few moments, then begins to get very hot. . . 
                    You drop it. . . The FLASHLIGHT singes your hand. . . 
                    Upon impact it explodes. . . 
                    There are pieces of shrapnel in your legs . . . ''')
                        player_health = player_health -25
                        del player_inventory['Flashlight']
                    else:
                        print('That cant be used here')
                else:
                    print('You dont have that . . . ')
            else:
                print('You dont got that')
        elif the_command == 'drop':
            drop_what = response[1]
            utils.scrub_response(drop_what)
            if drop_what in player_inventory.keys():
                del player_inventory[drop_what]
                print("You no longer possess,", drop_what)
        elif the_command == 'status':
            utils.player_status(player_inventory, player_health)
            utils.room_status(room7_inventory)
        else:
            print('unkown command:', the_command)

    # end of while loop
    return next_room
