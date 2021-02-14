from header import *
from Frame import *


class Tank(Frame):
    def __init__(self, color: str, pos: tuple, size: int = SIZE_IMG) -> None:
        url = f'{color}_tank.png'
        super().__init__(url, pos, size)
        self.direction = Direction.UP
        self.val = Vector2(0, 0)
            
    def move(self) -> None:
        self.pos.x += self.val.x
        self.pos.y += self.val.y

    def handleDirection(self):
        if self.direction == Direction.UP:
            self.rect = (self.size * self.frame, 0)
            self.val.x = 0
            self.val.y = -SPEED_TANK

    def update(self):
        self.nextFrame()
        self.handleDirection()
        self.move()
