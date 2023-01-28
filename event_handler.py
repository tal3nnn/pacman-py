from pygame.locals import *

from schedule import *

class EventHandler:
    def __init__(self, app_handler, game_handler):
        self.app_handler = app_handler
        self.game_handler = game_handler

    def update_key(self, key):
        if self.app_handler.state == 'BRANDING':
            self.app_handler.set_state('LOADING')

        elif self.app_handler.state == 'LOADING':
            pass

        elif self.app_handler.state == 'MENU':
            if key == K_UP:
                self.app_handler.menu_choice -= 1
                if self.app_handler.menu_choice < 0:
                    self.app_handler.menu_choice = 4
            elif key == K_DOWN:
                self.app_handler.menu_choice += 1
                if self.app_handler.menu_choice > 4:
                    self.app_handler.menu_choice = 0
            elif key == K_RETURN:
                if self.app_handler.menu_choice == 0:
                    self.app_handler.set_state('INGAME')
                    Schedule.level_set_started = True
                elif self.app_handler.menu_choice == 1:
                    self.app_handler.set_state('EDITOR')
                elif self.app_handler.menu_choice == 2:
                    self.app_handler.set_state('SCORES')
                elif self.app_handler.menu_choice == 3:
                    self.app_handler.set_state('TUTORIAL')
                elif self.app_handler.menu_choice == 4:
                    self.app_handler.set_state('QUIT')

        elif self.app_handler.state == 'SCORES':
            self.app_handler.set_state('MENU')

        elif self.app_handler.state == 'TUTORIAL':
            self.app_handler.set_state('MENU')

        elif self.app_handler.state == 'PAUSE':
            self.app_handler.revert_state()

        elif self.app_handler.state == 'LOST':
            self.app_handler.set_state('SCORES')

        elif self.app_handler.state == 'INGAME':
            if key == K_UP:
                self.game_handler.player.next_direction = (0, -1)
            elif key == K_DOWN:
                self.game_handler.player.next_direction = (0, 1)
            elif key == K_LEFT:
                self.game_handler.player.next_direction = (-1, 0)
            elif key == K_RIGHT:
                self.game_handler.player.next_direction = (1, 0)
            elif key == K_ESCAPE:
                self.app_handler.set_state('MENU')
            elif key == K_RETURN:
                self.app_handler.set_state('PAUSE')

        elif self.app_handler.state == 'EDITOR':
            if key == K_ESCAPE:
                self.app_handler.set_state('MENU')