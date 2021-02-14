from Image import *


class Frame(Image):
    frame: int

    def __init__(self, url: str, pos: tuple, size: int) -> None:
        super().__init__(url, pos, size)
        self.frame = 0
        self.__max_frames = MAX_FRAMES
    
    def nextFrame(self) -> None:
        self.frame += 1
        if self.frame >= self.__max_frames:
            self.frame = 0
