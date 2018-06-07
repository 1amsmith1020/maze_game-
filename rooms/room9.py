import maze_game.my_maze_utils as utils

import random

import time

import os

from colorama import Fore, Style


room9_inventory = {
'Warden Key': 1,
}
room_state = {
    'enemy_health': 70
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
    You step inside the Warden's office filled with apprehension and fear. . .
    You only get a brief glimpse of the moonlit room before something shoves you towards the center of the room. . . 
    . . . You hear the door slam and hear a voice . . . 
    "So you think you're gonna escape this asylum?! Well lemme tell you right, I'm going to kill you just like the others!"
    The source of the voice reveals itself as the WARDEN as he steps into the moonlight eminating from the window behind the desk. . . 
    He is fat and bald but is fully covered head to toe in riot armor. . .
    . . . He pulls out a .44 revolver. . . 
    This is going to be a hard fight. . . '''
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
        warden_health = 100
        if room_state['enemy_health'] <= 0:
            print('The warden is dead. . . You grab his WARDEN KEY and his FLASHLIGHT and get out of that room. . . ')
            take_what = 'Warden Key'
            utils.take_item(player_inventory, room9_inventory,
                                take_what)
            time.sleep(1.5)
            done_with_room = True
            next_room = 8



        if the_command == 'go':
            direction = response[1]
            print('The WARDEN has locked the door and there is no getting around him')
                # In this room, there is nowhere else to go.
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
            utils.room_status(room9_inventory)
        elif the_command == 'use':
            use_what = response[1].title()
            warden_attack = random.randint(0, 4)
            if warden_attack == 1:
                print('The warden swings his baton but misses dealing no damage. . .')
            elif warden_attack == 2:
                print('The warden swings his baton and knocks you in the side of the head, dealing 20 damage')
                player_health = player_health - 15
            elif warden_attack == 3:
                print('The warden fires a shot from his revolver, hitting you in the arm dealing 15 damage')
                player_health = player_health - 15
            elif warden_attack == 4:
                print('He bodyslams you into the wall, but it does not hurt too bad. . . It deals 10 damage')
                player_health = player_health - 10
            else:
                print('...')
            if use_what in player_inventory:
                if player_inventory[use_what] > 0:
                    if use_what == 'Butter Knife:':
                        print("You swing the butter knife at the warden. . . It bounces off his armor, and he laughs as it falls to the floor")
                        del player_inventory['Butter Knife']
                    elif use_what == 'Flashlight':
                        print('You blind the warden with the beam of the flashlight and then hit him in the head twice dealing 25 damage before he pushes you into a wall, hurting your back')
                        player_health = player_health - 10
                        room_state['enemy_health'] = room_state['enemy_health'] - 25
                    elif use_what == 'Sub Machine Gun':
                        print('You manage to fire off quite a few shots into his armor dealing 30 damage before he knocks the gun away')
                        room_state['enemy_health'] = room_state['enemy_health'] - 30
                    elif use_what == 'Crowbar':
                        print('The Crowbar digs deep into his left arm as you bring it down, dealing 15 damage')
                        room_state['enemy_health'] = room_state['enemy_health'] - 15
                    elif use_what == 'Mop':
                        print('You swing the wet mop and it strikes the side of his neck between his helmet and his armor dealing 15 damage')
                        room_state['enemy_health'] = room_state['enemy_health'] - 15
                    else:
                        print('you cant use that')

        else:
            print('unkown command:', the_command)

    # end of while loop
    return next_room
