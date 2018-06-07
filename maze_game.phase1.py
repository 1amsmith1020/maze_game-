# fix to run progream fromm out directory
import sys
import os
cwd = os.getcwd()
sys.path.append(cwd+"/./../")
# room imports
import maze_game.rooms.room1 as r1
import maze_game.rooms.room2 as r2
import maze_game.rooms.room3 as r3
import maze_game.rooms.room4 as r4
import maze_game.rooms.room5 as r5
import maze_game.rooms.room6 as r6
import maze_game.rooms.room7 as r7
import maze_game.rooms.room8 as r8
import maze_game.rooms.room9 as r9
import maze_game.rooms.room10 as r10
import maze_game.rooms.room11 as r11
import maze_game.rooms.room12 as r12
#to use colorgram
from colorama import init
init()
import maze_game.my_maze_utils as utils
# Default the player to the first room
room_number = 1

# Player Inventory/Stats
player_inventory = {
    'Patient I.D': 1,
    'Janitor I.D': 0,
    'Guard I.D': 0,
    'Warden Key': 0,
    'Sewer Key': 0,
    'Tower Key': 0,
    'Bump Key': 0,
    'Crowbar': 0,
    'Green backpack': 0,
    'Key': 0,
    'Batteries': 0,
    'Flashlight:': 0,
    'Butter Knife': 0,
    'Sub Machine Gun': 0,
    'Glass Shard': 0,
    'Mop': 0,
}
player_health = 60
carry_weight = 10
print("Welcome to the maze game...\n")

should_continue = True

while should_continue:
    if room_number == 1:
        room_number = r1.run_room(player_inventory, player_health)
    elif room_number == 2:
        room_number = r2.run_room(player_inventory, player_health)
    elif room_number == 3:
        room_number = r3.run_room(player_inventory, player_health)
    elif room_number == 4:
        room_number = r4.run_room(player_inventory, player_health)
    elif room_number == 5:
        room_number = r5.run_room(player_inventory, player_health)
    elif room_number == 6:
        room_number = r6.run_room(player_inventory, player_health)
    elif room_number == 7:
        room_number = r7.run_room(player_inventory, player_health)
    elif room_number == 8:
        room_number = r8.run_room(player_inventory, player_health)
    elif room_number == 9:
        room_number = r9.run_room(player_inventory, player_health)
    elif room_number == 10:
        room_number = r10.run_room(player_inventory, player_health)
    elif room_number == 11:
        room_number = r11.run_room(player_inventory, player_health)
    elif room_number == 12:
        room_number = r12.run_room(player_inventory, player_health)
    elif room_number == -5:
        should_continue = False
    else:
        break


#

print('The game is over. . .')
print('''Lead Game Designer: Liam Smith
Lead Writer: Liam Smith
Lead Coder: Liam Smith
You get the point.......
''')
