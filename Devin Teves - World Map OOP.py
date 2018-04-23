import time
import random

import character
import items

# extra stuff
counter = 0  # for oof (??)
inventory = []
invCapacity = 8
health = 100


class Room(object):
    def __init__(self, name, description, north, south, east, west, up, down, character, items):
        self.NAME = name
        self.DESCRIPTION = description
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.up = up
        self.down = down
        self.character = character
        self.item = items
        self.looping_oof = ["oof"]
        self.ping_phrases = ['pls', 'pls stop', 'pls stop doing this', 'pls just continue the game',
                             'just play the game', 'y u do dis', 'stop', 'stop doing this']

    def print_descriptions(self):
        print(items.BLUE + self.NAME + items.END)
        print(self.DESCRIPTION)
        if current_node.item is not None and not current_node.item.isTaken:
            print("It seems you can take a..." + current_node.item.name.lower())
            # if isinstance(self.items, list):
            #     print("It seems you can take:")
            #     for items in inventory:

    def move(self, directions):
        global current_node
        current_node = globals()[getattr(self, directions)]

    def jump(self):
        if current_node == BEDROOM or current_node == LIVING_ROOM:
            time.sleep(.5)
            print(BOLD + "oh woop there's a ceiling fan there" + END)
            time.sleep(1)
            print(RED + "You hit the ceiling fan while it was on. Your head gets chopped off" + END)
            quit(0)
        else:
            print(REDBOLD + "ow" + END)
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
            print(REDBOLD + "You typed in ping too much that the game got tired of you and decided to quit")
            quit(0)

    def flush(self):
        if current_node == BATHROOM:
            print(BOLD + "..." + END)
            time.sleep(1)
            print(BOLD + RED + "a man rises from the toilet and kills you" + END)
            quit(0)
        else:
            print(REDBOLD + "There's no toilet here u stupid" + END)


# characters and items

Cookie = character.Character("Cookiezi", "This person seems to be sitting behind a desk with a computer mashing "
                                         "his keyboard\nslightly, but you could definitely hear it. On his monitor, "
                                         "he seems to be clicking circles...", None, None, None)
jeff = character.Character("jeff", 
                           "he's sitting on a chair playing a game on the left side of the room", "stop", None, 50)

cookie = items.Food("Cookie", "A chocolate chip cookie. Seems delicious.")
bed = items.Item("Bed", "Your average-looking bed.")
ball = items.Ball("Ball", "A regular, old tennis ball.")
techRoomKey = items.Item("Key", "The key has a message engraved that says 'Tech Room Key'...")
backwardsGun = items.BackwardsGun("Gun", "It's a gun, but its barrel is pointing the opposite way.")
water = items.Drink("Water Bottle", "A water bottle that has an off-center label that says 'Fiji'.")
cookieMask = items.Mask("Mask",
                        "A mask of a smiling man wearing glasses with slits in the eyes. Wonder what you'd use it for.")
shirt = items.Shirt("Shirt", "Just a plain white shirt.")
weirdBag = items.Container("Backpack", "Just a regular backpack.", 4)

# rooms

BEDROOM = Room("Bedroom", 
               "You are in a bedroom full of anime posters, figures, etc.\n"
               "You have a computer sitting on a desk to your north, and a door to the east.",
               "COMPUTER", None, "HALLWAY", None, None, None, None, bed)
COMPUTER = Room("Computer", "On the desk lies a computer with a crappy membrane keyboard and a mouse. "
                            "On the computer lies a weird game called 'osu!'...",
                None, "BEDROOM", "HALLWAY", None, None, None, None, weirdBag)
HALLWAY = Room("Hallway",
               "The hallway has a few paintings with a dull red carpet on the wooden floor."
               "\nThere are stairs leading down to the south, as well as another room across yours.",
               "DINING_ROOM", "EMPTY_ROOM", "BATHROOM", "BEDROOM", None, "DINING_ROOM", None, None)
EMPTY_ROOM = Room("Empty Room",
                  "You enter an empty room, but in the southern-most corner there's a table with what seems to be "
                  "a drawing tablet, as well as a keyboard.",
                  "HALLWAY", "TABLE", None, None, None, None, jeff, backwardsGun)
TABLE = Room("Table",
             "On the table there is a key and empty boxes with labels saying "
             "'HyperX Alloy FPS Mechanical Gaming Keyboard' as well as another\n"
             "box that says 'Huion Graphics Tablet'...",
             "EMPTY_ROOM", None, None, None, None, None, None, techRoomKey)
BATHROOM = Room("Bathroom",
                "The bathroom is set with two sinks, a bathtub and a toilet.\n"
                "There are also toiletries sitting on top of the sink counter.",
                None, None, None, "HALLWAY", None, None, None, None)
DINING_ROOM = Room("Dining Room",
                   "The dining room has a table with a fancy green cloth and a basket full of fake fruit."
                   "\nThe kitchen leads east, and the living room to the west.",
                   None, "HALLWAY", "KITCHEN1", "LIVING_ROOM", "HALLWAY", None, None, cookie)
KITCHEN1 = Room("Entrance to Kitchen",
                "In the kitchen there's a refrigerator and a pantry full of "
                "food,\nas well as a long counter to eat food on. There's more stuff farther south.",
                "DINING_ROOM", "KITCHEN2", None, None, None, None, None, None)
KITCHEN2 = Room("Farther Side of Kitchen",
                "This side of the Kitchen has a flat screen tv mounted to the wall\nwith a smaller table below "
                "it that holds the cable box, and an old,\nuseless game console. There's what seems to be a "
                "laundry room to the\nwest as well as a slide door leading outside east.",
                "KITCHEN1", None, "BACKYARD1", "LAUNDRY_ROOM", None, None, None, None)
LAUNDRY_ROOM = Room("Laundry Room",
                    "The Laundry Room has a washing and drying machine, as well as a cabinet.",
                    "CABINET", None, "KITCHEN2", None, None, None, None, water)
CABINET = Room("Inside of Cabinet",
               "Inside the cabinet contains jackets and sweaters. The shelf above it has a \n"
               "few boxes put for storage, but there's a paper mask of a man's face here...",
               # osu! joke, don't worry about it
               None, "LAUNDRY_ROOM", "KITCHEN2", None, None, None, None, cookieMask)
BACKYARD1 = Room("Backyard",
                 "The empty backyard had little to no grass, making it look like a desert.\nNot only that, there "
                 "are two dogs that seem to not care about it at all\nand just have fun with the tennis balls "
                 "around them.",
                 "BACKYARD2", None, None, "KITCHEN2", None, None, None, ball)
BACKYARD2 = Room("Farther side of the Backyard",
                 "This side of the backyard has an unused grill and a bench lying at the wall of the house. And "
                 "more tennis balls...", None, "BACKYARD1", None, None, None, None, None, ball)
LIVING_ROOM = Room("Living Room",
                   "The living room has couches set with a large TV.\nThe exit seems to go the south.",
                   None, "DOOR", "DINING_ROOM", None, None, None, None, None)
DOOR = Room("Door",
            "You stand at the exit of the house, where lies a bunch of shoes.\nThe door faces west, "
            "and there's another door to the south.",
            "LIVING_ROOM", "LOCKED_DOOR", None, 'PORCH', None, None, None, None)
LOCKED_DOOR = Room("Locked Door", "This room's door is locked.", "DOOR", None, None, None, None, None, None, None)
PORCH = Room("Porch",
             "You exit the house into the porch, where there are short, dull, plants.\nYou can go more to "
             "the west to exit the porch and into the driveway.",
             None, None, "DOOR", "DRIVEWAY", None, None, None, None)
DRIVEWAY = Room("Driveway",
                "The drive way has a basketball hoop, but to the west you see a store with a sign that says... "
                "Walm.\nYou can go back north into the porch.",
                "PORCH", None, None, "STORE", None, None, None, None)
STORE = Room("Walm", "Sorry to keep your hopes up, this store is closed.",
             None, None, "DRIVEWAY", None, None, None, None, None)

TECH_ROOM = Room("Tech Room",
                 "The door you open leads you into room filled with bright looking technology.\n"
                 "The whole room seems to be white-ish. The whole room seems to be some sort of 'man cave'.\n"
                 "You feel so intimidated that you shouldn't touch any of the equipment.",
                 "DOOR", None, None, None, None, None, Cookie, None)

dir1 = ['north', 'south', 'east', 'west', 'up', 'down']
dir2 = ['n', 's', 'e', 'w', 'u', 'd']

current_node = BEDROOM
current_node_hasChanged = True

while True:
    if health == 0:
        print(items.REDBOLD + "you died" + items.END)
        break
    print(items.REDBOLD + "Health: " + items.END + str(health))
    if current_node_hasChanged:
        current_node.print_descriptions()
        current_node_hasChanged = False
        if current_node.character is not None \
                and current_node.character.isAlive:
            current_node.character.print_descriptions()
    command = input('>').lower().strip()
    if command == 'quit':
        quit(0)
    elif command == 'look' or command == 'l':
        current_node.print_descriptions()
        if current_node.character is None or not current_node.character.isAlive:
            continue
        else:
            current_node.character.print_descriptions()
    elif command == "jump":
        current_node.jump()
    elif command == 'inv' or command == 'inventory':
        if not inventory:
            print(items.REDBOLD + "You don't have anything in your inventory." + items.END)
        else:
            print("Your inventory:")
            for item in inventory:
                if isinstance(item, Container):
                    if item.isOpen:
                        print(BOLD + item.name.lower() + " (Open)" + items.END)
                    else:
                        print(BOLD + item.name.lower() + " (Closed)" + items.END)
                else:
                    print(BOLD + item.name.lower() + items.END)
    elif command == 'armor':
        if items.head is None and items.chest is None and items.legs is None and items.feet is None:
            print(items.REDBOLD + "You're wearing nothing." + items.END)
        else:
            print("You are wearing:")
            if items.items.head is not None:
                print("Head: " + items.items.head.name)
            if items.chest is not None:
                print("Chest: " + items.chest.name)
            if items.legs is not None:
                print("Legs: " + items.legs.name)
            if items.feet is not None:
                print("Feet: " + items.feet.name)
    elif command == "oof":
        current_node.oof()
    elif command == "ping":
        current_node.ping()
        counter += 1
    elif command == 'flush':
        current_node.flush()
    elif command == 'beep':
        print('boop')
    elif command in dir2:
        pos = dir2.index(command)
        command = dir1[pos]
        try:
            current_node.move(command)
            current_node_hasChanged = True
        except KeyError:
            print(RED + "You can't go that way." + items.END)
            current_node_hasChanged = False
    elif command in dir1:
        try:
            current_node.move(command.lower())
            current_node_hasChanged = True
        except KeyError:
            print(RED + "You can't go that way." + items.END)
            current_node_hasChanged = False
    elif 'take off' in command or 'unequip' in command:
        if command == 'take off' or command == 'unequip':
            if items.head is None and items.chest is None and items.legs is None and items.feet is None:
                print(items.REDBOLD + "You aren't wearing anything." + items.END)
            else:
                unequip_command = input("What do you want to take off?\n>").lower()
                if items.head is not None:
                    if items.head == bed and unequip_command == 'bed':
                        items.head = None
                        inventory.append(bed)
                        print(items.BLUEBOLD + "You take off the bed." + items.END)
                    elif unequip_command == items.head.name.lower():
                        items.head.unequip()
                    else:
                        print(items.REDBOLD + "You aren't wearing that." + items.END)
                elif items.chest is not None:
                    if unequip_command == items.chest.name.lower():
                        items.chest.unequip()
                    else:
                        print(items.REDBOLD + "You aren't wearing that." + items.END)
                elif items.legs is not None:
                    if unequip_command == items.legs.name.lower():
                        items.legs.unequip()
                    else:
                        print(items.REDBOLD + "You aren't wearing that." + items.END)
                elif items.feet is not None:
                    if unequip_command == items.feet.name.lower():
                        items.feet.unequip()
                    else:
                        print(items.REDBOLD + "You aren't wearing that." + items.END)
                else:
                    print(items.REDBOLD + "You aren't wearing that.")
        else:
            if items.head is not None:
                if 'bed' in command:
                    items.head = None
                    inventory.append(bed)
                    print(items.BLUEBOLD + "You take off the bed." + items.END)
                elif items.head.name.lower() in command:
                    items.head.unequip()
            elif items.chest is not None:
                if items.chest.name.lower() in command:
                    items.chest.unequip()
            elif items.legs is not None:
                if items.legs.name.lower() in command:
                    items.legs.unequip()
            elif items.feet is not None:
                if items.feet.name.lower() in command:
                    items.feet.unequip()
            else:
                print(items.REDBOLD + "You aren't wearing anything.")
    elif 'take' in command or 'pickup' in command.strip():
        if command == 'take' or command.strip() == 'pickup':
            take_command = input("What do you want to take?\n>").lower().strip()
            if take_command == current_node.item.name.lower():
                if not current_node.item.isTaken:
                    current_node.item.take()
                else:
                    print(items.REDBOLD + "You already took that." + items.END)
            elif 'nothing' in take_command or 'nevermind' in take_command or 'nvm' in take_command:
                print("ok")
            else:
                print(items.REDBOLD + "That item isn't here." + items.END)
        elif current_node.item.name.lower() in command:
            current_node.item.take()
        else:
            print(items.REDBOLD + "That item isn't here." + items.END)
    elif 'drop' in command:
        if not inventory:
            print(items.REDBOLD + "You don't have anything in your inventory." + items.END)
        elif command == 'drop':
            drop_command = input("What do you want to drop?\n>").lower()
            for item in inventory:
                if item.name.lower() in drop_command:
                    item.drop()
                else:
                    print(items.REDBOLD + "You can't drop that." + items.END)
        else:
            for item in inventory:
                if item.name.lower() in command:
                    item.drop()
                else:
                    print(items.REDBOLD + "You don't have that in your inventory." + items.END)
                    break
    elif 'throw' in command:
        if not inventory:
            print(items.REDBOLD + "You don't have anything in your inventory." + items.END)
        elif command == 'throw':
            throw_command = input("What do you want to throw?\n>").lower()
            if throw_command == 'ball':
                ball.throw()
            elif 'nothing' in throw_command or 'nevermind' in throw_command or 'nvm' in throw_command:
                print("ok")
            else:
                for item in inventory:
                    if throw_command == item:
                        item.drop()
                        break
                    else:
                        print(items.REDBOLD + "That's not in your inventory." + items.END)
        else:
            for item in inventory:
                if item.name.lower() in command:
                    if item == ball:
                        ball.throw()
                        ball.isTaken = False
                        break
                    else:
                        item.drop()
                else:
                    print(items.REDBOLD + "You don't have that in your inventory." + items.END)
    elif 'talk' in command:
        if current_node.character is None:
            print(items.REDBOLD + "There is no one here." + items.END)
        elif command == 'talk':
            talk_command = input("Who do you want to talk to?\n>").lower().strip()
            if talk_command == current_node.character.name:
                if current_node.character.isAlive:
                    current_node.character.talk()
                else:
                    print(items.REDBOLD + "That person is dead." + items.END)
            elif 'noone' in talk_command or 'nevermind' in talk_command or 'nvm' in talk_command:
                print("ok")
            else:
                print(items.REDBOLD + "That person isn't here." + items.END)
        elif current_node.character.name.lower() in command:
            if current_node.character.isAlive:
                current_node.character.talk()
            elif not current_node.character.isAlive:
                print(items.REDBOLD + "That person is dead.")
            else:
                print(items.REDBOLD + "That person isn't here." + items.END)
        else:
            print(items.REDBOLD + "That person isn't here." + items.END)
    elif 'wear' in command:
        if not inventory:
            print(items.REDBOLD + "You don't have anything in your inventory." + items.END)
        else:
            for item in inventory:
                if command == 'wear':
                    wear_command = input("What do you want to wear?\n>").lower()
                    if wear_command == 'bed':
                        time.sleep(1)
                        print("ok")
                        time.sleep(.5)
                        items.head = bed
                        inventory.pop(inventory.index(bed))
                        print(items.BLUEBOLD + "You wear the bed." + items.END)
                        break
                    elif wear_command == item.name.lower():
                        item.equip()
                        break
                    else:
                        print(items.REDBOLD + "That item isn't in your inventory." + items.END)
                        break
                elif 'bed' in command:
                    time.sleep(1)
                    print("ok")
                    time.sleep(.5)
                    items.head = bed
                    inventory.pop(inventory.index(bed))
                    print(items.BLUEBOLD + "You wear the bed." + items.END)
                    break
                elif item.name.lower() in command:
                    item.equip()
                    break
                else:
                    print(items.REDBOLD + "You aren't wearing that.")
                    break
    elif 'open door' in command:
        if current_node == LOCKED_DOOR:
            if techRoomKey in inventory:
                current_node = TECH_ROOM
                print(items.BLUEBOLD + "You open the door.\n" + items.END)
                current_node_hasChanged = True
            else:
                print(items.REDBOLD + "You don't have a key." + items.END)
        else:
            print(items.REDBOLD + "There is no locked door to open.")
    elif 'shoot' in command:
        if not inventory:
            print(items.REDBOLD + "You don't have anything to shoot with." + items.END)
        else:
            if backwardsGun in inventory:
                if command == 'shoot':
                    backwardsGun_command = input("Who do you want to shoot?\n>").lower()
                    if backwardsGun_command == current_node.character.name.lower():
                        backwardsGun.shoot()
                    else:
                        print(items.REDBOLD + "That person isn't here." + items.END)
                elif current_node.character.name.lower() in command:
                    backwardsGun.shoot()
                else:
                    print(items.REDBOLD + "That person isn't here." + items.END)
            else:
                print(items.REDBOLD + "You don't have anything to shoot with." + items.END)
    elif 'check' in command or 'look at' in command:
        if not inventory:
            print(items.REDBOLD + "You don't have anything in your inventory." + items.END)
        else:
            for item in inventory:
                if command == 'check':
                    check_command = input("What do you want to check?\n>").lower()
                    if check_command == item.name.lower():
                        item.print_descriptions()
                        break
                    elif 'nothing' in check_command or 'nevermind' in check_command or 'nvm' in check_command:
                        print("ok")
                        break
                    else:
                        print(items.REDBOLD + "That isn't in your inventory." + items.END)
                        break
                else:
                    if item.name.lower() not in command:
                        continue
                    else:
                        item.print_descriptions()

    elif 'drink' in command:
        if not inventory:
            print(items.REDBOLD + "You don't have anything in your inventory." + items.END)
        else:
            for item in inventory:
                if command == 'drink':
                    drink_command = input("What do you want to drink?\n>").lower()
                    if drink_command == item.name.lower():
                        if isinstance(item, Drink):
                            water.drink()
                        elif item == bed:
                            time.sleep(1)
                            print("ok")
                            time.sleep(.5)
                            print(items.BLUEBOLD + "You drink the bed." + items.END)
                            inventory.pop(inventory.index(bed))
                    elif 'nothing' in drink_command or 'nevermind' in drink_command or 'nvm' in drink_command:
                        print("ok")
                        break
                    else:
                        print(items.REDBOLD + "You can't drink that." + items.END)
                        break
                elif item.name.lower() in command:
                    if command == item.name.lower():
                        if isinstance(item, Drink):
                            water.drink()
                        elif item == bed:
                            time.sleep(1)
                            print("ok")
                            time.sleep(.5)
                            print(items.BLUEBOLD + "You drink the bed." + items.END)
                            inventory.pop(inventory.index(bed))
                    else:
                        print(items.REDBOLD + "You can't drink that." + items.END)
                        break
                else:
                    print(items.REDBOLD + "That's not in your inventory." + items.END)
    elif 'play' in command:
        if 'computer' in command:
            if items.head == cookieMask:
                print(PURPLE + BOLD + "You're so good at this game that the computer exploded" + items.END)
                time.sleep(1)
                print(PURPLE + BOLD + "And it pops back..." + items.END)
            else:
                print(items.REDBOLD
                      + "You play the game and rage in frustration at why you're so bad at it."
                      + items.END)
        elif command == 'play':
            play_command = input("What do you want to play?\n>").lower().strip()
            if play_command == 'computer':
                if items.head == cookieMask:
                    print(PURPLE + BOLD + "You're so good at this game that the computer exploded" + items.END)
                    time.sleep(3)
                    print(PURPLE + BOLD + "And it pops back..." + items.END)
                else:
                    print(items.REDBOLD
                          + "You play the game and rage in frustration at why you're so bad at it..."
                          + items.END)
            elif 'nothing' in take_command or 'nevermind' in take_command or 'nvm' in take_command:
                print("ok")
            else:
                print(items.REDBOLD + "You can't play that." + items.END)
        else:
            print(items.REDBOLD + "You can't play that." + items.END)
    elif 'kill' in command:
        if command == 'kill':
            kill_command = input("Who do you want to kill?\n>").lower()
            if kill_command == 'me' or kill_command == 'self':
                time.sleep(2)
                print("ok")
                time.sleep(.5)
                while health != 0:
                    health -= 1
                    print(items.REDBOLD + "Health: " + items.END + str(health))
                    time.sleep(.01)
            elif kill_command == current_node.character.name.lower():
                if current_node.character.isAlive:
                    current_node.character.kill()
                else:
                    print(items.REDBOLD + "That person is dead." + items.END)
            else:
                print(items.REDBOLD + "That person isn't here." + items.END)
        elif current_node.character is None:
            print(items.REDBOLD + "There is no one here." + items.END)
        elif current_node.character.name.lower() in command:
            if current_node.character.isAlive:
                current_node.character.kill()
            else:
                print(items.REDBOLD + "That person is dead." + items.END)
        else:
            print(items.REDBOLD + "That person isn't here." + items.END)
    elif 'suicide' in command:
        time.sleep(2)
        print("ok")
        time.sleep(.5)
        while health != 0:
            health -= 1
            print(items.REDBOLD + "Health: " + items.END + str(health))
            time.sleep(.01)
            if health == 0:
                break
    elif 'open' in command:
        if not inventory:
            print(items.REDBOLD + "You don't have anything in your inventory to open." + items.END)
        else:
            for item in inventory:
                if command == 'open':
                    open_command = input("What do you want to open?\n>").lower()
                    if open_command == item.name.lower():
                        if isinstance(item, Container):
                            item.open()
                        else:
                            print(items.REDBOLD + "You can't open that." + items.END)
                    elif 'nothing' in open_command or 'nevermind' in open_command or 'nvm' in open_command:
                        print("ok")
                    else:
                        print(items.REDBOLD + "That isn't in your inventory." + items.END)
                        break
                elif item.name.lower() in command:
                    if isinstance(item, Container):
                        item.open()
                        break
                    else:
                        print(items.REDBOLD + "You can't open that." + items.END)
                # else:
                #     print(items.REDBOLD + "That is not in your inventory." + items.END)
    elif 'close' in command:
        if not inventory:
            print(items.REDBOLD + "You don't have anything in your inventory to close." + items.END)
        else:
            for item in inventory:
                if command == 'close':
                    close_command = input("What do you want to close?\n>").lower()
                    if close_command == item.name.lower():
                        if isinstance(item, Container):
                            item.close()
                        else:
                            print(items.REDBOLD + "You can't close that." + items.END)
                    elif 'nothing' in close_command or 'nevermind' in close_command or 'nvm' in close_command:
                        print("ok")
                    else:
                        print(items.REDBOLD + "That isn't in your inventory." + items.END)
                elif item.name.lower() in command:
                    if isinstance(item, Container):
                        item.close()
                    else:
                        print(items.REDBOLD + "You can't open that." + items.END)
                else:
                    print(items.REDBOLD + "That isn't in your inventory." + items.END)







    elif 'put' in command:
        if not inventory:
            print(items.REDBOLD + "You don't have anything in your inventory." + items.END)
        else:
            if command == 'put':
                put_command = input("What do you want to put?\n>").lower()
                for item in inventory:
                    if put_command == item.name.lower():
                        for item2 in inventory:
                            putIn_command = input("Where do you want to put that?\n").lower()
                            if putIn_command == item2.name.lower():
                                if isinstance(item2, Container):
                                    if item2.isOpen:
                                        item2.put_item_in(item)
                                    else:
                                        print(items.REDBOLD + "That item isn't open." + items.END)
                                else:
                                    print(items.REDBOLD + "You can't put that in there." + items.END)
                            elif putIn_command == put_command:
                                print(items.REDBOLD + "You can't put that in itself." + items.END)
                            else:
                                print(items.REDBOLD + "That is not in your inventory." + items.END)
                    else:
                        print(items.REDBOLD + "That isn't in your inventory." + items.END)



    else:
        print("Command not Recognized")
        current_node_hasChanged = False
