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


class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down):
        self.NAME = name
        self.DESCRIPTION = description
        self.NORTH = north
        self.SOUTH = south
        self.WEST = west
        self.EAST = east
        self.UP = up
        self.DOWN = down
        self.looping_oof = ["oof"]
        self.counter = 0
        self.ping_phrases = ['pls', 'pls stop', 'pls stop doing this', 'pls just continue the game',
                             'just play the game', 'y u do dys', 'stop', 'stop doing this']

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
        if self.counter <= 2:
            print(BOLD + UNDERLINE + "pong" + END)
            self.counter += 1
        elif self.counter == 3:
            print(GREEN + BOLD + "don't waste your time doing this" + END)
            self.counter += 1
        elif self.counter == 4:
            print(YELLOW + BOLD + "pls you have more important things other than this" + END)
            self.counter += 1
        elif self.counter == 5:
            print(CYAN + BOLD + "pls" + END)
            self.counter += 1
        elif self.counter <= 9:
            print(BOLD + PURPLE + random.choice(self.ping_phrases) + END)
            self.counter += 1
        elif self.counter == 10:
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
    def __init__(self, name, description, dialogue, health, location):
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.health = health
        self.location = location

    def print_descriptions(self):
        print(GREEN + BOLD + self.name + END)
        print(self.description)

    def talk(self):
        print(self.dialogue)


BEDROOM = Room("Bedroom",
               "You are in a bedroom full of anime posters, figures, etc."
               "\nYou have a computer sitting on a desk to your north, and a door to the east.",
               "COMPUTER", None, "HALLWAY", None, None, None)
COMPUTER = Room("Computer",
                "On the desk lies a computer with a crappy membrane keyboard and a mouse. "
                "On the computer lies a weird game called 'osu!'...",
                None, "BEDROOM", "HALLWAY", None, None, None)
HALLWAY = Room("Hallway",
               "The hallway has a few paintings with a dull red carpet on the wooden floor."
               "\nThere are stairs leading down to the south, as well as another room across yours.",
               "DINING_ROOM", "EMPTY_ROOM", "BATHROOM", "BEDROOM", None, "DINING_ROOM")
EMPTY_ROOM = Room("Empty Room",
                  "You enter an empty room, but in the southern-most corner there's a table with what seems to be "
                  "a drawing tablet, as well as a keyboard.",
                  "HALLWAY", "TABLE", None, None, None, None)
TABLE = Room("Table",
             "On the table there's a long box with a label saying 'HyperX Alloy FPS Mechanical Gaming "
             "Keyboard' as well as another box that says 'Huion Graphics Tablet'...",
             "EMPTY_ROOM", None, None, None, None, None)
BATHROOM = Room("Bathroom",
                "The bathroom is set with two sinks, a bathtub and a toilet. "
                "There are also toiletries sitting on top of the sink counter.",
                None, None, None, "HALLWAY", None, None)
DINING_ROOM = Room("Dining Room",
                   "The dining room has a table with a fancy green cloth and a basket full of fake fruit."
                   "\nThe kitchen leads east, and the living room to the west.",
                   None, "HALLWAY", "KITCHEN1", "LIVING_ROOM", "HALLWAY", None)
KITCHEN1 = Room("Entrance to Kitchen",
                "In the kitchen there's a refrigerator and a pantry full of "
                "food, as well as a long counter to eat food on.\nThere's more stuff farther south.",
                "DINING_ROOM", "KITCHEN2", None, None, None, None)
KITCHEN2 = Room("Farther Side of Kitchen",
                "This side of the Kitchen has a flat screen tv mounted to the wall with a smaller table below "
                "it that holds the cable box, and an old, useless game console.\nThere's what seems to be a "
                "laundry room to the west as well as a slide door leading outside east.",
                "KITCHEN1", None, "BACKYARD", "LAUNDRY_ROOM", None, None)
LAUNDRY_ROOM = Room("Laundry Room",
                    "The Laundry Room has a washing and drying machine, as well as a cabinet.",
                    "CABINET", None, "KITCHEN2", None, None, None)
CABINET = Room("Inside of Cabinet",
               "Inside the cabinet contains jackets and sweaters. The shelf above it has a few boxes put for "
               "storage, but there's a paper mask of a man's face with glasses smiling and squinting his "
               "eyes...",  # osu! joke, don't worry about it
               None, "LAUNDRY_ROOM", "KITCHEN2", None, None, None)
BACKYARD1 = Room("Backyard",
                 "The empty backyard had little to no grass, making it look like a desert. Not only that, there "
                 "are two dogs that seem to not care about it at all and just have fun with the tennis balls "
                 "around them.",
                 "BACKYARD2", None, None, "KITCHEN2", None, None)
BACKYARD2 = Room("Farther side of the Backyard",
                 "This side of the backyard has an unused grill and a bench lying at the wall of the house. And "
                 "more tennis balls...",
                 None, "BACKYARD1", None, None, None, None)
LIVING_ROOM = Room("Living Room",
                   "The living room has couches set with a large TV.\nThe exit seems to go the south.",
                   None, "DOOR", "DINING_ROOM", None, None, None)
DOOR = Room("Door",
            "You stand at the exit of the house, where lies a bunch of shoes.\nThe door faces west, "
            "and there's another door to the south.",
            "LIVING_ROOM", "LOCKED_DOOR", None, 'PORCH', None, None)
LOCKED_DOOR = Room("Locked Door",
                   "This room's door is locked.",
                   "DOOR", None, None, None, None, None)
PORCH = Room("Porch",
             "You exit the house into the porch, where there are short, dull, plants.\nYou can go more to "
             "the west to exit the porch and into the driveway.",
             None, None, "DOOR", "DRIVEWAY", None, None)
DRIVEWAY = Room("Driveway",
                "The drive way has a basketball hoop, but to the west you see a store with a sign that says... "
                "Walm.\nYou can go back north into the porch.",
                "PORCH", None, None, "STORE", None, None)
STORE = Room("Walm",
             "Sorry to keep your hopes up, this store is closed.",
             None, None, "DRIVEWAY", None, None, None)

dir1 = ['north', 'south', 'east', 'west', 'up', 'down']
dir2 = ['n', 's', 'e', 'w', 'u', 'd']

current_node = BEDROOM
current_node_hasChanged = True
while True:
    if current_node_hasChanged:
        current_node.print_descriptions()
        current_node_hasChanged = False
    command = input('>').lower().strip()
    if command == 'quit':
        quit(0)
    elif command == 'look' or command == 'l':
        current_node.print_descriptions()
    elif command == "jump":
        current_node.jump()
    elif command == "oof":
        current_node.oof()
    elif command == "ping":
        current_node.ping()
    elif command == 'flush':
        current_node.flush()
    elif command in dir2:
        pos = dir2.index(command)
        command = dir1[pos]
        try:
            current_node.move(command.upper())
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
    else:
        print("Command not Recognized")
        current_node_hasChanged = False