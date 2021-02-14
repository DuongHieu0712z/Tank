from header import *


class Image:
    img: pygame.Surface
    pos: Vector2
    rect: Rect
    size: int

    def __init__(self, url: str, pos: tuple, size: int) -> None:
        self.img = pygame.image.load(url)
        self.pos = Vector2(pos)
        self.__rect = Rect(0, 0, size, size)

    @property
    def rect(self) -> Rect:
        return self.__rect

    @rect.setter
    def rect(self, rect: tuple) -> None:
        self.__rect.x = rect[0]
        self.__rect.y = rect[1]

    @property
    def size(self) -> int:
        return self.__rect.w

    @size.setter
    def size(self, size: int) -> None:
        self.rect.w = self.rect.h = size

    def load(self, url: str) -> None:
        self.img = pygame.image.load(url)

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.img, self.pos, self.rect)
