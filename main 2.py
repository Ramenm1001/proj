class Player:
    def __init__(self):
        self.hp = 100


player = Player()
player.hp -= 5


class Player:
    def __init__(self):
        self.hp = 100

    def take_damage(self, dmg):
        self.hp -= dmg

    def feature(self):
        print(123)


player = Player()
player.take_damage(5)
