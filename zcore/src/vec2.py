class Vec2:
    x: float
    y: float
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


    def copy(self) -> 'Vec2':
        return Vec2(self.x, self.y)

