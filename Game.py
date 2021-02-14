from header import *
from Timer import *
from Tank import *


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN)
        pygame.display.set_caption('Tank')

        self.is_running = True
        self.tank = Tank('red', (16, 16))
        self.timer = Timer()

    def processInput(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.is_running = False

    def update(self):
        self.tank.update()

    def render(self):
        self.screen.fill(BLACK)
        self.tank.draw(self.screen)
        pygame.display.update()

    def run(self) -> None:
        ms_per_frame = 1000 / FPS
        while self.is_running:
            self.timer.start()

            self.processInput()
            self.update()
            self.render()
            
            current_time = self.timer.ticks
            if current_time < ms_per_frame:
                delay_time = ms_per_frame - current_time
                pygame.time.delay(int(delay_time))

        pygame.quit()
