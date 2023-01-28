import pygame, sys
from pygame.locals import *

from app_handler import *
from const import *
from display_handler import *
from event_handler import *
from game_handler import *

class Pacman:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()

        pygame.display.set_caption('PACMAN')
        pygame.display.set_icon(pygame.image.load('assets/icon.png'))
        self.screen = pygame.display.set_mode(WINDOW_SIZE, SCALED | DOUBLEBUF)

        self.app_handler = AppHandler()
        self.game_handler = GameHandler()
        self.display_handler = DisplayHandler(self.app_handler, self.game_handler)
        self.event_handler = EventHandler(self.app_handler, self.game_handler)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.app_handler.set_state('QUIT')
                elif event.type == pygame.KEYDOWN:
                    self.event_handler.update_key(event.key)

            self.app_handler.update()
            if self.app_handler.state == 'INGAME':
                self.game_handler.update()
            self.display_handler.update(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    pacman = Pacman()
    pacman.run()