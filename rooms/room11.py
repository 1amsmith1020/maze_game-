import maze_game.my_maze_utils as utils

import time

from colorama import Fore, Style


room11_inventory = {

}
room_state = {
    'in_combat': True,
    'surprise': True,
    'enemy_health': 20
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
 This must be teh room where they pat down the visitors before going into the visitors room. . .
 There is a door to the SOUTH and the WEST. . .
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
        if room_state['in_combat'] == True:
            if room_state['surprise'] == True:
                print('A security guard pistol whips you in the head dealing 15 damage. . . '
                      'He moves to block the door where you came. . . '
                      'You are going to have to take care of him before you can do anything else. . . ')
                room_state['surprise'] = False


            if the_command == 'use':
                use_what = response[1].title()
                if use_what in player_inventory:
                    if player_inventory[use_what] > 0:
                        if use_what == 'Flashlight':
                            print('You blind the guard with your flashlight and hit him with the end of the flashlight dealing 15 damage')
                            room_state['enemy_health'] = room_state['enemy_health'] - 15
                        elif use_what == 'Butter Knife':
                            print('You actually manage to draw blood with the dull knife by hacking furiously dealing 5 damage')
                            room_state['enemy_health'] = room_state['enemy_health'] - 5
                        elif use_what == "Sub Machine Gun":
                            print('You shoot him in the chest and he stumbles backward  dealing 30 damage')
                            room_state['enemy_health'] = room_state['enemy_health'] - 30
                        elif use_what == 'Glass Shard':
                            print('The glass shard rips trough his uniform and opens a gash along his arm dealing 10 damage')
                            room_state['enemy_health'] = room_state['enemy_health'] - 10
            elif the_command == 'status':
                utils.player_status(player_inventory, player_health)
                utils.room_status(room11_inventory)

            else:
                print('While in combat you cannot use that command')
            if room_state['enemy_health'] < 0:
                print('The guard falls to the ground dead')
                room_state['in_combat'] = False
        else:
            if the_command == 'go':
                direction = response[1]
            # Use your hand drawn map to help you think about what is valid
                if direction == 'west':
                    print('. . . ')
                    time.sleep(.75)
                    next_room = 12
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
                utils.room_status(room11_inventory)
            else:
                print('unkown command:', the_command)

    # end of while loop
    return next_room
