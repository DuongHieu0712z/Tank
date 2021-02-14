import pygame


class Timer:
    def __init__(self) -> None:
        self.__start_tick = 0
        self.__pause_tick = 0
        self.is_started = False
        self.is_paused = False

    def start(self) -> None:
        self.__is_started = True
        self.__is_paused = False
        self.__start_tick = pygame.time.get_ticks()

    def stop(self) -> None:
        self.__is_started = False
        self.__is_paused = False

    def pause(self) -> None:
        if self.__is_started and not self.__is_paused:
            self.__is_paused = True
            self.__pause_tick = pygame.time.get_ticks() - self.__is_started

    def unpause(self) -> None:
        if self.__is_paused:
            self.__is_paused = False
            self.__pause_tick = 0
            self.__start_tick = pygame.time.get_ticks() - self.__pause_tick

    @property
    def ticks(self) -> int:
        if self.__is_started:
            if self.__is_paused:
                return self.__pause_tick
            return pygame.time.get_ticks() - self.__start_tick
        return 0
