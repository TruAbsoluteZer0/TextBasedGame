""" A text based game written so that a user can move from room to room
  and gather items to beat the game. A user has to input a valid Direction.
  A user moves throughout the rooms without a map and has to rely on memory when playing"""

# Constants
invalid_direction = "That is not a valid direction."
game_over = "Thanks for playing."

rooms = {
    'Library Entrance': {'East': 'Study Hall', 'West': 'Teen Room', 'North': 'Work Space',
                         'South': 'Collection Space'},
    'Teen Room': {'East': 'Library Entrance', 'Item': 'Bag'},
    'Collection Space': {'North': 'Library Entrance', 'East': 'Astrology Room', 'Item': 'Holy Water'},
    'Study Hall': {'North': 'Staff Break Room', 'West': 'Library Entrance', 'Item': 'Hall'},
    'Staff Break Room': {'South': 'Study Hall', 'Item': 'Rope'},
    'Work Space': {'East': 'Reader Seating Space', 'South': 'Library Entrance', 'Item': 'Med Kit'},
    'Reader Seating Space': {'West': 'Work Space', 'Item': 'Sword'},
    'Astrology Room': {'West': 'Collection Space'}
}

# Global Variables
inventory = []


# Navigation function
def get_new_state(direction_from_user, current_room):
    if direction_from_user != 'Item' and direction_from_user in rooms[current_room]:  # if input is in nested dict
        # 'current_room' it's valid
        current_room = rooms[current_room][direction_from_user]  # uses dictionary to set next room
    else:
        print(invalid_direction)

    return current_room


# Get current status (room and item/inventory)
def show_status(current_room, name):
    print('{} is currently in the {}'.format(name, current_room))
    if 'Item' in rooms[current_room]:
        print("{} is in this room.".format(rooms[current_room]['Item']))
    else:
        print('There are no items in this room!')

    # Checks if inventory is not empty (empty lists are False)
    if inventory:
        output = ""
        for item in inventory:
            output += item + " | "
        output = output[:-3]  # Remove last 3 items (trailing " | ")
        print("You are carrying: {}".format(output))


def main():  # creates a gameplay function to loop rooms/game

    name = input('Enter your name:')

    print('Welcome, ' + name + '!')

    print(
        'You are an adventurer in search of a legendary artifact known as the handyman, an esteemed collectible,\n '
        'that hasn’t been seen in the past 5000 years. You’ve heard it is in an ancient library in Delti where you\n '
        'head to collect the handyman. Legend speaks of an alluring demon that protects it. Your mission is to gather\n'
        'the supplies from the library. You’ll need holy water to fend off the demon, a helmet to protect you from\n '
        'the white poison the demon spews, a spell book to defend yourself against her dark arts, a rope for your\n '
        'escape, a bag to keep your supplies in, and a sword to deal damage, and finally a medkit to protect yourself\n'
        'with.\n')

    current_room = "Library Entrance"

    """a while loop to make sure  that a user enters the right direction to go , how to exit the game and a way to 
    prompt a user to  enter a correct input"""

    # Main Game Loop
    while True:  # infinite loop until hitting break
        show_status(current_room, name)

        user_direction = input(
            'Please enter the direction you would like to go: North, East, South, or West. Otherwise to leave the game '
            'type exit: ').strip().capitalize()

        # Check if user wants to exit game
        if user_direction == 'Exit':
            break

        # Call the navigation function
        current_room = get_new_state(user_direction, current_room)  # receives returned room from navigate function

        # Exit room checks
        if current_room == 'Astrology Room':  # checks if user is in astrology room and if they have all the items
            if len(inventory) == 6:
                print('Congratulations', name, 'you have acquired the Handyman and defeated the demon')
            else:
                print('You failed to collect all the items and the demon drained your energy and killed you.',
                      game_over)
            break

        if 'Item' in rooms[current_room]:  # coding used to allow user to grab items
            item = rooms[current_room]['Item']
            answer = input('Would you like to grab ' + item + '? Enter yes or no: ').strip().lower()

            if answer == 'yes':
                inventory.append(item)
                rooms[current_room].pop('Item')
                print('You have acquired ' + item + '!')

            elif answer == 'no':
                print('Are you sure? Alright, remember you can grab the item later.')


main()
