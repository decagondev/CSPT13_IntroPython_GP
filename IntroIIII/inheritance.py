class Entity:
    def __init__(self: id, x, y):
        self.id = id
        self.x = x
        self.y = y

        def __str__(self):
            return f"{self.id}: ({self.x}, {self.y})"

class Mob(Entity):
    def __init__(self, id, x, y):
        super().__init__(id, x, y)

    def move(self, direction):
        if direction == "n":
            self.y -= self.speed
        if direction == "s":
            self.y -= self.speed
        if direction == "e":
            self.x += self.speed
        if direction == "w":
            self.x -= self.speed



    def __str__(self):
        return f"{super().__str__()}, {self.speed}"

m = Mob(0, 12, 10, 1) # is_an Entity

p = Player
print(e)