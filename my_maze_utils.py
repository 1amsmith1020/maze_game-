# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# prompt_question:
#   Ask a question of your user. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("Would you like cheese on your pizza?", ['yes', 'no'])
def prompt_question(prompt, valid_options):
    response = input(prompt)
    while not response.lower() in valid_options:
        print("Sorry, I did not understand your choice.")
        response = input(prompt)
    return response.lower()


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ask_command:
#   Ask your user for a command. The user must provide a response that is in
#   you list of valid options
#
#   prompt : A string that will be used to ask the user a question
#
#   valid_options : A list of string values you expect your user to respond with.
#
#   example usage:
#       a_topping = prompt_question("What do you want to do?", ['go', 'take', 'drop'])
def ask_command(prompt, valid_commands, no_arguments):
    ask_again = True
    result = []
    while ask_again:
        # Get a response from the user and split the response into words
        response = input(prompt)
        words = response.split()

        # be safe against user accidents of just hitting the ENTER key
        if len(words) > 0:
            #check if the command is the list of valid commands
            if words[0].lower() not in valid_commands:
                print('\tSorry, I don\'t understand:"', response, '"')
                print('\t\t Your choices are:', valid_commands, "\n")
            else:
                #if the command is valid, but they forgot an argument, try again.
                if len(words) < 2:
                    # but check first if it was in the no argument list
                    if words[0].lower() in no_arguments:
                        result = words
                        ask_again = False
                    else:
                        print('\tThe command: "', words[0], '" requires an argument.\n')
                else:
                    # Otherwise we at least have two arguments! Now programmer gets to choose what to do.
                    ask_again = False
                    result = words
    # END WHILE LOOP / ASK COMMAND

    #Return the command back to the user as a list (command will be index 0)
    # If the command was required then it will be in position 1
    return result
#has_a will check if a a dictionary has a spacific item
def has_a(player_inventory, item):
    if item in player_inventory.keys():
        curr_count = player_inventory[item]
        if curr_count > 0:
            return True
        else:
            return False
    else:
        return False

def drop_item(player_inventory, room_inventory, item):
    if has_a(player_inventory, item):
        curr_count = player_inventory[item]
        player_inventory[item] = curr_count - 1
        if has_a(room_inventory, item):
            room_count = room_inventory[item]
            room_inventory[item] = room_count + 1
        else:
            room_inventory[item] = 1
            print('You dropped the', item)
    else: print('you cant drop something you dont possess')

def take_item(player_inventory, room_inventory, item):
    if has_a(room_inventory, item):
        room_count = room_inventory[item]
        room_inventory[item] = room_count - 1

        if has_a(player_inventory, item):
            player_count = player_inventory[item]
            player_inventory[item] = player_count + 1
        else:
            player_inventory[item] = 1
        print('You take the', item)
    else:
        print('There is nothing to take here')

def room_status(room_inventory):
    print('In this room you can see:')
    empty = True
    for key in room_inventory.keys():
        if room_inventory[key]>0:
            print('\t\ta', key)
            empty = False
    if empty == True:
        print('\t\t. . . Nothing, sadly it is empty')

def player_status(player_inventory, player_health):
    print('You are in possession of:')
    for key in player_inventory.keys():
        if player_inventory[key] > 0:
            print('\t\t', key, ' : ', player_inventory[key])
    print('You have', player_health, 'health')

def scrub_response( sus_response ):
    result = []
    result.append(sus_response[0])

    if len(sus_response) > 1:

        arg = sus_response[1].title()
        if arg == 'Green':
            result.append('Green Backpack')
        elif arg == 'Ice':
            result.append('Ice Pick')
        elif arg == 'Butter':
            result.append('Butter Knife')
        elif arg == 'Guard':
            result.append('Guard I.D.')
        elif arg == 'Sub':
            result.append('Sub Machine Gun')
        elif arg == 'Bump':
            result.append('Bump Key')
        elif arg == 'Butter':
            result.append('Butter Knife')
        elif arg == 'Warden':
            result.append('Warden Key')
        elif arg == 'Glass':
            result.append('Glass Shard')
        else:
            result.append(sus_response[1])
    return result

