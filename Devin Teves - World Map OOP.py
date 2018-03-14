import time
import random

# colored text
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'

counter = 0


class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down, character):
        self.NAME = name
        self.DESCRIPTION = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.up = up
        self.down = down
        self.character = character
        self.looping_oof = ["oof"]
        self.ping_phrases = ['pls', 'pls stop', 'pls stop doing this', 'pls just continue the game',
                             'just play the game', 'y u do dis', 'stop', 'stop doing this']

    def print_descriptions(self):
        print(BLUE + self.NAME + END)
        print(self.DESCRIPTION)

    def move(self, directions):
        global current_node
        current_node = globals()[getattr(self, directions)]

    def jump(self):
        if current_node == BEDROOM or current_node == LIVING_ROOM:
            print(BOLD + "oh woop there's a ceiling fan there" + END)
            time.sleep(1)
            print(RED + "You hit the ceiling fan while it was on. Your head gets chopped off" + END)
            quit(0)
        else:
            print(RED + BOLD + "ow" + END)
            time.sleep(.5)

    def oof(self):
        print(BOLD + "".join(self.looping_oof) + END)
        time.sleep(.5)
        self.looping_oof.append("oof")

    def ping(self):
        if counter <= 2:
            print(BOLD + UNDERLINE + "pong" + END)
        elif counter == 3:
            print(GREEN + BOLD + "don't waste your time doing this" + END)
        elif counter == 4:
            print(YELLOW + BOLD + "pls you have more important things other than this" + END)
        elif counter == 5:
            print(CYAN + BOLD + "pls" + END)
        elif counter <= 9:
            print(BOLD + PURPLE + random.choice(self.ping_phrases) + END)
        elif counter == 10:
            print(RED + BOLD + "You typed in ping too much that the game got tired of you and decided to quit")
            quit(0)

    def flush(self):
        if current_node == BATHROOM:
            print(BOLD + "..." + END)
            time.sleep(1)
            print(BOLD + RED + "a man rises from the toilet and kills you" + END)
            quit(0)
        else:
            print(RED + BOLD + "There's no toilet here u stupid" + END)


class Character(object):
    def __init__(self, name, description, dialogue, inv, effect):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.inventory = inv
        self.effect = effect
        self.isAlive = True
        self.hasTalked = False
        self.counter = 0

    def print_descriptions(self):
        print(GREEN + BOLD + self.name + END)
        print(self.description)

    def talk(self):
        print("He says...")
        time.sleep(1)
        print(self.dialogue)
        self.hasTalked = True

    def kill(self):
        print(BOLD + RED + "oh woops you killed " + self.name.lower() + END)
        self.isAlive = False
        # if None not in self.inventory:


jeff = Character("jeff", "he's sitting on a chair playing a game on the left side of the room", "stop",
                 ['pen'], 'burn')

BEDROOM = Room("Bedroom",
               "You are in a bedroom full of anime posters, figures, etc."
               "\nYou have a computer sitting on a desk to your north, and a door to the east.",
               "COMPUTER", None, "HALLWAY", None, None, None, None)
COMPUTER = Room("Computer",
                "On the desk lies a computer with a crappy membrane keyboard and a mouse. "
                "On the computer lies a weird game called 'osu!'...",
                None, "BEDROOM", "HALLWAY", None, None, None, None)
HALLWAY = Room("Hallway",
               "The hallway has a few paintings with a dull red carpet on the wooden floor."
               "\nThere are stairs leading down to the south, as well as another room across yours.",
               "DINING_ROOM", "EMPTY_ROOM", "BATHROOM", "BEDROOM", None, "DINING_ROOM", None)
EMPTY_ROOM = Room("Empty Room",
                  "You enter an empty room, but in the southern-most corner there's a table with what seems to be "
                  "a drawing tablet, as well as a keyboard.",
                  "HALLWAY", "TABLE", None, None, None, None, jeff)
TABLE = Room("Table",
             "On the table there's a long box with a label saying 'HyperX Alloy FPS Mechanical Gaming "
             "Keyboard' as well as another box that says 'Huion Graphics Tablet'...",
             "EMPTY_ROOM", None, None, None, None, None, None)
BATHROOM = Room("Bathroom",
                "The bathroom is set with two sinks, a bathtub and a toilet. "
                "There are also toiletries sitting on top of the sink counter.",
                None, None, None, "HALLWAY", None, None, None)
DINING_ROOM = Room("Dining Room",
                   "The dining room has a table with a fancy green cloth and a basket full of fake fruit."
                   "\nThe kitchen leads east, and the living room to the west.",
                   None, "HALLWAY", "KITCHEN1", "LIVING_ROOM", "HALLWAY", None, None)
KITCHEN1 = Room("Entrance to Kitchen",
                "In the kitchen there's a refrigerator and a pantry full of "
                "food, as well as a long counter to eat food on.\nThere's more stuff farther south.",
                "DINING_ROOM", "KITCHEN2", None, None, None, None, None)
KITCHEN2 = Room("Farther Side of Kitchen",
                "This side of the Kitchen has a flat screen tv mounted to the wall with a smaller table below "
                "it that holds the cable box, and an old, useless game console.\nThere's what seems to be a "
                "laundry room to the west as well as a slide door leading outside east.",
                "KITCHEN1", None, "BACKYARD", "LAUNDRY_ROOM", None, None, None)
LAUNDRY_ROOM = Room("Laundry Room",
                    "The Laundry Room has a washing and drying machine, as well as a cabinet.",
                    "CABINET", None, "KITCHEN2", None, None, None, None)
CABINET = Room("Inside of Cabinet",
               "Inside the cabinet contains jackets and sweaters. The shelf above it has a few boxes put for "
               "storage, but there's a paper mask of a man's face with glasses smiling and squinting his "
               "eyes...",  # osu! joke, don't worry about it
               None, "LAUNDRY_ROOM", "KITCHEN2", None, None, None, None)
BACKYARD1 = Room("Backyard",
                 "The empty backyard had little to no grass, making it look like a desert. Not only that, there "
                 "are two dogs that seem to not care about it at all and just have fun with the tennis balls "
                 "around them.",
                 "BACKYARD2", None, None, "KITCHEN2", None, None, None)
BACKYARD2 = Room("Farther side of the Backyard",
                 "This side of the backyard has an unused grill and a bench lying at the wall of the house. And "
                 "more tennis balls...",
                 None, "BACKYARD1", None, None, None, None, None)
LIVING_ROOM = Room("Living Room",
                   "The living room has couches set with a large TV.\nThe exit seems to go the south.",
                   None, "DOOR", "DINING_ROOM", None, None, None, None)
DOOR = Room("Door",
            "You stand at the exit of the house, where lies a bunch of shoes.\nThe door faces west, "
            "and there's another door to the south.",
            "LIVING_ROOM", "LOCKED_DOOR", None, 'PORCH', None, None, None)
LOCKED_DOOR = Room("Locked Door",
                   "This room's door is locked.",
                   "DOOR", None, None, None, None, None, None)
PORCH = Room("Porch",
             "You exit the house into the porch, where there are short, dull, plants.\nYou can go more to "
             "the west to exit the porch and into the driveway.",
             None, None, "DOOR", "DRIVEWAY", None, None, None)
DRIVEWAY = Room("Driveway",
                "The drive way has a basketball hoop, but to the west you see a store with a sign that says... "
                "Walm.\nYou can go back north into the porch.",
                "PORCH", None, None, "STORE", None, None, None)
STORE = Room("Walm",
             "Sorry to keep your hopes up, this store is closed.",
             None, None, "DRIVEWAY", None, None, None, None)

dir1 = ['north', 'south', 'east', 'west', 'up', 'down']
dir2 = ['n', 's', 'e', 'w', 'u', 'd']

health = 100

current_node = BEDROOM
current_node_hasChanged = True

while True:
    print(RED + BOLD + "Health: " + END + str(health))
    if current_node_hasChanged:
        current_node.print_descriptions()
        current_node_hasChanged = False
    if current_node.character is not None and current_node.character.isAlive and \
       current_node.character.hasTalked is False:
        current_node.character.print_descriptions()
    command = input('>').lower().strip()
    if command == 'quit':
        quit(0)
    elif health == 0:
        break
    elif current_node.character is not None:
        current_node.character.encounter += 1
    elif current_node.character.effect is not None:
        if current_node.character.effect == 'burn':
            if current_node.character.encounter == 1:
                health -= 10
                print(RED + BOLD + "woah you took damage from %s's %s\nYou have %d now"
                      % (current_node.character.name, current_node.character.effect, health))
            else:
                health -= 10
    elif current_node.character.effect is None:
        pass
    elif command == 'look' or command == 'l':
        current_node.print_descriptions()
        if current_node.character is None:
            continue
        else:
            current_node.character.print_descriptions()
    elif command == "jump":
        current_node.jump()
    elif command == "oof":
        current_node.oof()
    elif command == "ping":
        current_node.ping()
        counter += 1
    elif command == 'flush':
        current_node.flush()
    elif command == 'no u':
        print(BOLD + RED + 'no u' + END)
    elif command in dir2:
        pos = dir2.index(command)
        command = dir1[pos]
        try:
            current_node.move(command)
            current_node_hasChanged = True
        except KeyError:
            print(RED + "You can't go that way." + END)
            current_node_hasChanged = False
    elif command in dir1:
        try:
            current_node.move(command.upper())
            current_node_hasChanged = True
        except KeyError:
            print(RED + "You can't go that way." + END)
            current_node_hasChanged = False
    elif command == 'kill':
        kill_command = input("Who do you want to kill?" + "\n>")
        if kill_command == "myself" or kill_command == 'me' or kill_command == "self":
            time.sleep(1)
            print(RED + BOLD + "hey nice you killed yourself" + END)
            quit(0)
        elif current_node.character is None:
            print("There's no one here.")
        elif kill_command == current_node.character:
            current_node.character.kill()
    elif command == "talk":
        if current_node.character is None:
            print(BOLD + RED + "There's no one here" + END)
        else:
            talk_choice = input("Who do you want to talk to?\n>").lower()
            if talk_choice == current_node.character.name.lower():
                current_node.character.talk()
            else:
                print(RED + BOLD + "That person isn't here." + END)
    elif command == "talk to throckmorton":
        if current_node.character is None:
            print("He isn't here.")
        elif current_node.character != throckmorton:
            print("He isn't here.")
        elif current_node.character == throckmorton:
            current_node.character.talk()
    else:
        print("Command not Recognized")
        current_node_hasChanged = False
