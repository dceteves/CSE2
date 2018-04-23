# armor
head = None
chest = None
legs = None
feet = None

# colored text
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

REDBOLD = RED + BOLD
BLUEBOLD = BLUE + BOLD

class Item(object):
    def __init__(self, name, desc):
        self.name = name
        self.description = desc
        self.isTaken = False

    def print_descriptions(self):
        print(PURPLE + BOLD + self.name + END)
        print(self.description)

    def take(self):
        if len(inventory) == invCapacity:
            print(REDBOLD + "Your inventory is full." + END)
        else:
            inventory.append(self)
            print(CYAN + BOLD + "You take the " + self.name.lower() + "." + END)
            self.isTaken = True

    def drop(self):
        inventory.pop(inventory.index(self))
        print(CYAN + BOLD + "You drop the " + self.name.lower() + '.' + END)
        current_node.item = self
        self.isTaken = False


class Weapon(Item):
    def __init__(self, name, desc, damage):
        super(Weapon, self).__init__(name, desc)
        self.damage = damage

    def hit(self): current_node.character.health -= self.damage

    def check_stats(self): print(BOLD + BLUE + "Damage: " + END + str(self.damage))


class Sword(Weapon):
    def __init__(self, name, desc, damage):
        super(Sword, self).__init__(name, desc, damage)

    def hit(self):
        random_number = random.randint(0, 10)
        if random_number % 2 == 0:  # crit
            current_node.character.health -= damage * 2
        else:
            current_Node.character.health -= damage


class BackwardsGun(Weapon):
    def __init__(self, name, desc):
        super(BackwardsGun, self).__init__(name, desc, 100)

    def shoot(self):
        print(REDBOLD + "you shot yourself and died" + END)
        quit(0)


class Hammer(Weapon):
    def __init__(self, name):
        super(Hammer, self).__init__(name, desc, 1)

    def break_door(self):
        print(BOLD + "..." + END)
        time.sleep(1)
        print(BOLD + BLUE + "Why is this hammer made of rubber?" + END)


class Consumable(Item):
    def __init__(self, name, desc):
        super(Consumable, self).__init__(name, desc)

    def use(self):
        inventory.pop(inventory.index(self))


class Food(Consumable):
    def __init__(self, name, desc):
        super(Food, self).__init__(name, desc)

    def eat(self):
        inventory.pop(inventory.index(self))
        print(PURPLE + BOLD + "yummy" + END)


class Drink(Consumable):
    def __init__(self, name, desc):
        super(Drink, self).__init__(name, desc)

    def drink(self):
        inventory.pop(inventory.index(self))
        print(BLUEBOLD + "You drink the %s and its bottle disappears..." + END % self.name.lower())


class Container(Item):
    def __init__(self, name, desc, capacity):
        super(Container, self).__init__(name, desc)
        self.capacity = capacity
        self.inventory = []
        self.isOpen = False
        self.isEmpty = False

    def put_item_in(self, item_name):
        if self.inventory.len() == capacity:
            print(REDBOLD + "Your inventory is full." + END)
        else:
            self.inventory.append(item_name)
            print(CYAN + BOLD + "You put the %s in the %s." + END % (item_name.lower(), self.name.lower()))

    def take_out(self, item_name):
        self.inventory.pop(self.inventory.index(item_name))
        inventory.append(item_name)
        print(CYAN + BOLD + "You take the %s out of the %s." + END % (item_name.lower(), self.name.lower()))

    def open(self):
        if not self.isOpen:
            self.isOpen = True
            print(BLUEBOLD + "You open the " + self.name.lower() + "." + END)
        else:
            print(REDBOLD + "That is already open." + END)

    def close(self):
        if self.isOpen:
            self.isOpen = False
            print(BLUEBOLD + "You close the " + self.name.lower() + "." + END)
        else:
            print(REDBOLD + "That is already closed." + END)

    def drop_all(self):
        for items in self.inventory:
            current_node.item = items
            self.inventory.pop(self.inventory.index(items))



class Box(Container):
    def __init__(self, name, desc):
        super(Box, self).__init__(name, desc, 4)

    def put_item_in(self, item_name):
        if self.inventory.len() == capacity:
            print(REDBOLD + "Your inventory is full." + END)
        else:
            self.inventory.append(item_name)
            print(CYAN + BOLD + "You put the %s in the box" + END % item_name.lower())

    def wear(self):
        global head
        head = self


class Ball(Item):
    def __init__(self, name, desc):
        super(Ball, self).__init__(name, desc)

    def throw(self):
        inventory.pop(inventory.index(ball))
        print("You throw the ball and in a blink of "
                  "an eye, one of the dogs zoom in a blink "
                  "of an eye and catch the ball.")
        time.sleep(4)
        print(YELLOW + BOLD + "The dog then hovers and starts floating to orbit.")
        time.sleep(3)
        print(YELLOW + BOLD + "The dog comes back with a bucket with even more balls.")
        time.sleep(1)

class Wearable(Item):
    def __init__(self, name, desc, body):
        super(Wearable, self).__init__(name, desc)
        self.body = body

    def equip(self):
        if self.body is not None:
            print(REDBOLD + "You're already wearing something." + END)
        else:
            self.body = self
            inventory.pop(inventory.index(self))
            print(BLUEBOLD + "You wear the " + self.name + END)

    def un_equip(self):
        self.body = None
        print(BLUEBOLD + "You take off the " + self.name + END)
        inventory.append(self)


class Mask(Wearable):
    def __init__(self, name, desc):
        super(Mask, self).__init__(name, desc, head)

    def equip(self):
        global head
        if head is not None:
            print(REDBOLD + "You're already wearing something." + END)
        else:
            head = self
            inventory.pop(inventory.index(self))
            print(BLUEBOLD + "You wear the " + self.name + END)

    def un_equip(self):
        global head
        head = None
        inventory.append(self)


class Shirt(Wearable):
    def __init__(self, name, desc):
        super(Shirt, self).__init__(name, desc, chest)

    def equip(self):
        global chest
        if chest is None:
            print(REDBOLD + "You're already wearing something." + END)
        else:
            chest = self
            inventory.pop(inventory.index(self))
            print(BLUEBOLD + "You wear the %s." + END + self.name.lower())

    def un_equip(self):
        global chest
        print(BLUEBOLD + "You take off the %s." + END + self.name.lower())
        chest = None
        inventory.append(self)


class Book(Item):
    def __init__(self, name, desc, read_text):
        super(Book, self).__init__(name, desc)
        self.readText = read_text

    def read(self):
        print(self.read_text)
