import maze_game.my_maze_utils as utils

import time

from colorama import Fore, Style


room8_inventory = {

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
   As you step inside, you realize the door used to be locked, but is now open with one hinge loose
   .... It looks like an armory. . . but there is nothing in it. . . . You can make out a door to the WEST
    . . . You have a feeling there is something more to the EAST than meets the eye. . . 
    '''
    print(Fore.BLUE + Style.BRIGHT + description +
          Style.RESET_ALL)
    if 'Flashlight' in player_inventory:
        print('As always, you could always use your FLASHLIGHT to maybe reveal things that would otherwise be hidden. . . ')

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
            if direction == 'north':
                print('. . . ')
                time.sleep(.75)
                next_room = 6
                done_with_room = True
            elif direction == 'east':
                if player_inventory['Flashlight'] > 0:
                    print(' . . . ')
                    time.sleep(.75)
                    next_room = 9
                    done_with_room = True
                else:
                    print('You stumble around the room and roll your ankle and you lose 5 health. . .'
                          'On the west end you feel the outline of a door and you head inside')
            elif direction == 'west':
                done_with_room = True
                next_room = 10
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
            utils.room_status(room8_inventory)
        elif the_command == 'use':
            use_what = response[1].title()
            if use_what in player_inventory:
                if player_inventory[use_what] > 0:
                    if use_what == 'Flashlight':
                        print('. . . '
                              'You switch the flashlight on and shine it around the room and realize there is a door to the EAST that says WARDEN on it. . . '
                              'You have a feeling what you need is in there. . . ')
        else:
            print('unkown command:', the_command)

    # end of while loop
    return next_room
