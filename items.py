inventory = []


class Items(object):
    def __init__(self):
        self.onGround = True

    def take(self):
        inventory.append(self)
        self.onGround = False