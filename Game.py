from header import *


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.__screen = pygame.display.set_mode(SCREEN)
        pygame.display.set_caption('Tank')

    def run(self) -> None:

        is_running = True
        while is_running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    is_running = False

            pygame.display.update()

        pygame.quit()
