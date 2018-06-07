import maze_game.my_maze_utils as utils

import random

import time



from colorama import Fore, Style
# # # # # # # # #
#   Room 6
#       This room can only be gotten too from Room 1
#       You can go to room 2,
#       You can take a key
#       You can use your FLASHLIGHT, CROWBAR, and BUMP KEY in this room
room6_inventory = {
    'Butter Knife': 1,
    'Guard I.D.': 1,
    'Sub Machine Gun': 1,
    'Flashlight': 1
}
room_state = {
    'in_combat': True,
    'surprise': True,
    'enemy_health': 30,
    'door_locked': True,
    'continue_trying': True
}
def run_room(player_inventory, player_health):
    commands = ["go", "take", "drop", "use", "examine", "status", "help"]
    no_args = ["examine", "status", "help"]

    # nonsense room number, we need to figure out which room they want in the loop
    next_room = -1

    description = '''. . . 
Moonlight penetrates the large glass panes on the ceiling to reveal the room is much larger than you anticipated. . . 
It seems to be a large dining hall. . . 
It seems there was a conflict here not long ago, there is flecks of blood on the floor, and most of the tables have been overturned. . . 
There are doors each leading NORTH, SOUTH, and EAST, and you notice a lock holding the EASTERN door shut. . . 
The only thing that you see that could be actually useful to you is a BUTTER KNIFE laying close by. . .'''
    print(description)

    if 'Flashlight' in player_inventory:
        print('As always, you could always use your FLASHLIGHT to maybe reveal things that would otherwise be hidden. . . ')

    if 'Crowbar' or 'Bump Key' in player_inventory:
        print('You have some tools that could deal with that lock. . .')

    done_with_room = False
    while not done_with_room:
        # Examine the response and decide what to do
        response = utils.ask_command("What do you want to do?", commands, no_args)
        response = utils.scrub_response(response)
        the_command = response[0]

        if room_state['in_combat'] == True:
            if room_state['enemy_health'] == 30:
                room_state['surprise'] = False
                print(
                    'A strained scream pierces through the darkness as a shape rushes towards you knocking you backwards. . . '
                    'It slashes a cut in your arm dealing 10 damage'
                    'You realize as you get up that it is a mental patient just like you, only this one has lost its mind. . .'
                    'You are going to have to take care of it before you do anything else. . . .')

                player_health = player_health - 10

            if the_command == 'use':
                use_what = response[1].title()
                if use_what in player_inventory:
                    if player_inventory[use_what] > 0:
                        if use_what == 'Flashlight':
                            print('You blind the patient with your flashlight and hit him with the end of the flashlight dealing 15 damage')
                            room_state['enemy_health'] = room_state['enemy_health'] - 15
                        elif use_what == 'Butter Knife':
                            print('You actually manage to draw blood with the dull knife by hacking furiously, dealing 5 damage')
                            room_state['enemy_health'] = room_state['enemy_health'] - 5
                        elif use_what == "Sub Machine Gun":
                            print('You shoot him in the chest and he stumbles backward  dealing 30 damage')
                            room_state['enemy_health'] = room_state['enemy_health'] - 30
                        elif use_what == 'Glass Shard':
                            print('The glass shard rips trough his gown and opens a gash along his arm dealing 10 damage')
                            room_state['enemy_health'] = room_state['enemy_health'] - 10
            elif the_command == 'status':
                utils.player_status(player_inventory, player_health)
                utils.room_status(room6_inventory)
            else:
                print('While in combat you cannot use that command')

            if room_state['enemy_health'] <= 0:
                print('The crazed patient falls to the ground dead')
                room_state['in_combat'] = False
                room_state['surprise'] = False




        if room_state['in_combat'] == False:
            room_state['surprise'] = False
            if the_command == 'go':
                direction = response[1]
                if direction == 'north':
                    next_room = 2
                    done_with_room = True
                elif direction == 'east':

                    if room_state['door_locked'] == False:
                        next_room = 7
                        done_with_room = True
                    else:
                        print('The door is locked . . .')
                elif direction == 'south':
                    next_room = 8
                    done_with_room = True
                else:
                    print('You cannot go', direction, 'in this room. . . ')


            elif the_command == 'take':
                take_what = response[1].title()
                if take_what in room6_inventory:
                    utils.take_item(player_inventory, room6_inventory,
                                take_what)
                    if take_what == 'Sub Machine Gun' or 'Butter Knife':
                        room_state['surprise'] = True
                        room_state['in_combat'] = True
                else:
                    print('There is nothing like that in this room')
            elif the_command == 'drop':
                drop_what = response[1].title()
                utils.drop_item(player_inventory, room6_inventory,
                            drop_what)
            elif the_command == 'status':
                utils.player_status(player_inventory,player_health)
                print('In this room you can see. . .'
                  'a Butter Knife ')

            elif the_command == 'use' and room_state['in_combat']== False:
                use_what = response[1].title()
                if use_what in player_inventory:
                    if player_inventory[use_what] > 0:
                        if use_what == 'Flashlight':
                            print('. . .')
                            time.sleep(1.0)
                            print('''. . . You flip the switch on the flashlight and shine it around the room. . . 
                    In the farthest SOUTHERN corner, you see some thing reflect the flashlight beam back to you. . . 
                    After making your way towards the source, you realize it's a SUB MACHINE GUN and there is a GUARD I.D. next to it''')

                        elif use_what == 'Crowbar' or use_what == 'Bump Key':
                            if room_state['continue_trying'] == True:
                                open_chance = random.randint(0,4)

                                if open_chance == 1:

                                    if use_what == 'Crowbar':


                                        print('The crowbar snaps in half. . . ')
                                        room_state['door_locked'] = True
                                        room_state['continue_trying'] = False
                                        del player_inventory['Crowbar']

                                    elif use_what == 'Bump Key':
                                        print('It seems like you cant get any of the keys to work and the door stays locked. One of the keys is now pretty bent. . . '
                                    'You stop trying out of fear of breaking your tools. . . It does look like your BUMP KEYS are still usable though. . . .')
                                        room_state['door_locked'] = True
                                        room_state['continue_trying'] = False

                                elif open_chance == 2 or 3 or 4 or 5:
                                    room_state['door_locked'] = False
                                    print('. . . It worked! The door is now unlocked. . .')

                            else:
                                print('It isnt worth broken tools. . . you move on . . . ')
                else:
                        print('''You don't have a''', use_what)

    return next_room

