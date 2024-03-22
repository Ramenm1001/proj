class NPC:
    pass


class Player(NPC):
    pass


class Level:
    pass


class Sprite:
    pass


class Decorations:
    def __init__(self):
        self.decorations = [Sprite(), Sprite(), Sprite()]


class Game:
    def __init__(self):
        self.p = Player()
        self.background = Sprite()
        self.decor = Decorations()
        
