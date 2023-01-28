import pygame
# import threading

from const import *
from schedule import *

class DisplayHandler:
    def __init__(self, app_handler, game_handler):
        self.app_handler = app_handler
        self.game_handler = game_handler
        # self.game_handler.level.map_draw(self.app_handler.assets)

    def update(self, screen):
        if self.app_handler.state == 'BRANDING':
            screen.fill('black')

            self.app_handler.assets.black_screen.set_alpha(255 - self.app_handler.branding_index)

            screen.blit(self.app_handler.assets.branding, (int(WINDOW_SIZE[0] - self.app_handler.assets.branding.get_width()) / 2, int(WINDOW_SIZE[1] - self.app_handler.assets.branding.get_height()) / 2))
            screen.blit(self.app_handler.assets.black_screen, (0, 0))

        elif self.app_handler.state == 'LOADING':
            screen.fill('black')

            bar_posx, bar_posy = int(WINDOW_SIZE[0] - LOADING_BAR_SIZE[0]) / 2, int(WINDOW_SIZE[1] - LOADING_BAR_SIZE[1]) / 2

            pygame.draw.rect(screen, (33, 33, 255), (bar_posx - 4, bar_posy - 4) + (LOADING_BAR_SIZE[0] + 8, LOADING_BAR_SIZE[1] + 8), width = 2)
            pygame.draw.rect(screen, (33, 33, 255), (bar_posx, bar_posy) + (LOADING_BAR_SIZE[0] * (self.app_handler.loading_index / 100), LOADING_BAR_SIZE[1]))

            text_loading = self.app_handler.assets.font.render('LOADING...', True, (33, 33, 255))
            text_completion = self.app_handler.assets.font.render(str(self.app_handler.loading_index) + '%', True, 'white')

            screen.blit(text_loading, (bar_posx + int(LOADING_BAR_SIZE[0] - text_loading.get_width()) / 2, bar_posy - LOADING_BAR_SIZE[1] - 4))
            screen.blit(text_completion, (bar_posx + int(LOADING_BAR_SIZE[0] - text_completion.get_width()) / 2, bar_posy))

        elif self.app_handler.state == 'SCORES':
            screen.fill('black')
            screen.blit(self.app_handler.assets.title, (int(WINDOW_SIZE[0] - self.app_handler.assets.title.get_width()) / 2, 60))
            screen.blit(self.app_handler.assets.font.render('HIGH SCORES', True, (33, 33, 255)), (20, 270))

        elif self.app_handler.state == 'TUTORIAL':
            screen.fill('black')
            screen.blit(self.app_handler.assets.font_mid.render('HOW TO PLAY', True, (192, 192, 0)), (20, 20))
            screen.blit(self.app_handler.assets.font.render('USE THE ARROW KEYS TO MOVE.', True, 'white'), (20, 50))
            screen.blit(self.app_handler.assets.font.render('EAT ALL PAC-GUMS TO FINISH A LEVEL.', True, 'white'), (20, 70))
            screen.blit(self.app_handler.assets.font.render('GHOSTS WILL KILL YOU ASIDE IF YOU EAT', True, 'white'), (20, 90))
            screen.blit(self.app_handler.assets.font.render('A POWER PAC-GUM.', True, 'white'), (20, 110))
            screen.blit(self.app_handler.assets.font.render('IN ARCADE AND RANDOM MODE YOU HAVE TO', True, 'white'), (20, 130))
            screen.blit(self.app_handler.assets.font.render('COMPLETE AS MUCH LEVELS AS POSSIBLE.', True, 'white'), (20, 150))
            screen.blit(self.app_handler.assets.font.render('IN ADVENTURE MODE, YOU HAVE TO COMPLETE.', True, 'white'), (20, 170))
            screen.blit(self.app_handler.assets.font.render('ALL THE LEVELS, JUST LIKE IN CUSTOM MODE,', True, 'white'), (20, 190))
            screen.blit(self.app_handler.assets.font.render('WHERE YOU CAN PLAY LEVELS MADE IN EDITOR.', True, 'white'), (20, 210))
            screen.blit(self.app_handler.assets.font_mid.render('LEVEL EDITOR', True, (192, 192, 0)), (20, 240))
            screen.blit(self.app_handler.assets.font.render('THE EDITOR CAN BE USED TO EDIT UP TO', True, 'white'), (20, 270))
            screen.blit(self.app_handler.assets.font.render('99 CUSTOM LEVELS, THAT WILL BE SAVED IN', True, 'white'), (20, 290))
            screen.blit(self.app_handler.assets.font.render('YOUR PC, IN A FOLDER CALLED ADDGAMES.', True, 'white'), (20, 310))
            screen.blit(self.app_handler.assets.font.render('YOU CAN COPY-PASTE THE CONTENT OF THIS', True, 'white'), (20, 330))
            screen.blit(self.app_handler.assets.font.render('FOLDER TO SHARE YOUR LEVELS.', True, 'white'), (20, 350))

        elif self.app_handler.state == 'MENU':
            screen.fill('black')
            screen.blit(self.app_handler.assets.title, (int(WINDOW_SIZE[0] - self.app_handler.assets.title.get_width()) / 2, 60))
            screen.blit(self.app_handler.assets.font.render('PLAY', True, 'white' if self.app_handler.menu_choice == 0 and int(self.app_handler.animation_index) % 3 else (33, 33, 255)), (235, 230))
            screen.blit(self.app_handler.assets.font.render('LEVEL EDITOR', True, 'white' if self.app_handler.menu_choice == 1 and int(self.app_handler.animation_index) % 3 else (33, 33, 255)), (235, 260))
            screen.blit(self.app_handler.assets.font.render('HIGH SCORES', True, 'white' if self.app_handler.menu_choice == 2 and int(self.app_handler.animation_index) % 3 else (33, 33, 255)), (235, 290))
            screen.blit(self.app_handler.assets.font.render('TUTORIAL', True, 'white' if self.app_handler.menu_choice == 3 and int(self.app_handler.animation_index) % 3 else (33, 33, 255)), (235, 320))
            screen.blit(self.app_handler.assets.font.render('EXIT', True, 'white' if self.app_handler.menu_choice == 4 and int(self.app_handler.animation_index) % 3 else (33, 33, 255)), (235, 350))

        elif self.app_handler.state == 'PAUSE':
            text_pause_shadow = self.app_handler.assets.font_big.render('PAUSED', True, (0, 0, 64))
            text_pause = self.app_handler.assets.font_big.render('PAUSED', True, 'white' if int(self.app_handler.animation_index) % 3 else (192, 192, 0))
            screen.blit(text_pause_shadow, (int(WINDOW_SIZE[0] - text_pause.get_width()) / 2 - 8, int(WINDOW_SIZE[1] - text_pause.get_height()) / 2 - 8))
            screen.blit(text_pause, (int(WINDOW_SIZE[0] - text_pause.get_width()) / 2, int(WINDOW_SIZE[1] - text_pause.get_height()) / 2))

        elif self.app_handler.state == 'LOST':
            text_lost_shadow = self.app_handler.assets.font_big.render('YOU LOST', True, (0, 0, 64))
            text_lost = self.app_handler.assets.font_big.render('GAME OVER', True, (192, 192, 0))
            text_score_shadow = self.app_handler.assets.font_big.render('SCORE : ' + self.app_handler.lost_score, True, (0, 0, 64))
            text_score = self.app_handler.assets.font_big.render('SCORE : ' + self.app_handler.lost_score, True, 'white' if int(self.app_handler.animation_index) % 3 else (192, 192, 0))
            screen.blit(text_lost_shadow, (int(WINDOW_SIZE[0] - text_lost.get_width()) / 2 - 8, int(WINDOW_SIZE[1] - text_lost.get_height()) / 2 - 8 - 50))
            screen.blit(text_lost, (int(WINDOW_SIZE[0] - text_lost.get_width()) / 2, int(WINDOW_SIZE[1] - text_lost.get_height()) / 2 - 50))
            screen.blit(text_score_shadow, (int(WINDOW_SIZE[0] - text_score.get_width()) / 2 - 8, int(WINDOW_SIZE[1] - text_score.get_height()) / 2 - 8 + 50))
            screen.blit(text_score, (int(WINDOW_SIZE[0] - text_score.get_width()) / 2, int(WINDOW_SIZE[1] - text_score.get_height()) / 2 + 50))

        elif self.app_handler.state == 'INGAME':
            if Schedule.level_set_finished:
                self.game_handler.level.map_draw(self.app_handler.assets)
                Schedule.level_set_finished = False

            screen.fill('black')
            screen.blit(self.game_handler.level.map_surface, (0, 0))

            if self.game_handler.player.direction != (0, 0):
                self.game_handler.player.display_direction = self.game_handler.player.direction
            if self.game_handler.player.can_move:
                pacman_id = 'PACMAN_' + DIR_NAMES[self.game_handler.player.display_direction] + '_' + str(int(self.app_handler.animation_index % 2))
            else:
                pacman_id = 'PACMAN_DEAD_' + str(self.game_handler.player.death_index)

            screen.blit(self.app_handler.assets.sprite[pacman_id], self.game_handler.player.screen_pos)
            for ghost in self.game_handler.ghost:
                ghost_id = 'GHOST_' + str(self.game_handler.ghost.index(ghost)) + '_' + DIR_NAMES[ghost.direction] + '_' + str(int(self.app_handler.animation_index % 2))
                screen.blit(self.app_handler.assets.sprite[ghost_id], ghost.screen_pos)

            pygame.draw.rect(screen, (33, 33, 255), (28 * TILE_SIZE + 5, 0, WINDOW_SIZE[0] - 28 * TILE_SIZE - 5, WINDOW_SIZE[1]), width = 5)
            screen.blit(self.app_handler.assets.font_mid.render('LEVEL', True, (192, 192, 0)), (513, 20))
            screen.blit(self.app_handler.assets.font_mid.render('SCORE', True, (192, 192, 0)), (506, 80))
            screen.blit(self.app_handler.assets.font.render(str(self.game_handler.level.id + 1), True, 'white'), (513, 50))
            screen.blit(self.app_handler.assets.font.render(str(self.game_handler.level.score), True, 'white'), (513, 110))
            for life in range(self.game_handler.lives):
                screen.blit(self.app_handler.assets.sprite['PACMAN_LEFT_0'], (530 + life * 20, 460))

        elif self.app_handler.state == 'LOST':
            text_lost_shadow = self.app_handler.assets.font_big.render('GAME OVER', True, (0, 0, 64))
            text_lost = self.app_handler.assets.font_big.render('GAME OVER', True, (192, 192, 0))
            text_score_shadow = self.app_handler.assets.font_big.render('SCORE : ' + self.app_handler.lost_score, True, (0, 0, 64))
            text_score = self.app_handler.assets.font_big.render('SCORE : ' + self.app_handler.lost_score, True, 'white' if int(self.app_handler.animation_index) % 3 else (192, 192, 0))
            screen.blit(text_lost_shadow, (int(WINDOW_SIZE[0] - text_lost.get_width()) / 2 - 8, int(WINDOW_SIZE[1] - text_lost.get_height()) / 2 - 8 - 50))
            screen.blit(text_lost, (int(WINDOW_SIZE[0] - text_lost.get_width()) / 2, int(WINDOW_SIZE[1] - text_lost.get_height()) / 2 - 50))
            screen.blit(text_score_shadow, (int(WINDOW_SIZE[0] - text_score.get_width()) / 2 - 8, int(WINDOW_SIZE[1] - text_score.get_height()) / 2 - 8 + 50))
            screen.blit(text_score, (int(WINDOW_SIZE[0] - text_score.get_width()) / 2, int(WINDOW_SIZE[1] - text_score.get_height()) / 2 + 50))

        elif self.app_handler.state == 'EDITOR':
            if Schedule.level_set_finished:
                self.game_handler.level.map_draw(self.app_handler.assets)
                Schedule.level_set_finished = False

            screen.fill('black')
            screen.blit(self.game_handler.level.map_surface, (0, 0))
            screen.blit(self.app_handler.assets.sprite['PACMAN_RIGHT_1'], self.game_handler.player.screen_pos)

            pygame.draw.rect(screen, (33, 33, 255), (28 * TILE_SIZE + 5, 0, WINDOW_SIZE[0] - 28 * TILE_SIZE - 5, WINDOW_SIZE[1]), width = 5)
            screen.blit(self.app_handler.assets.font_mid.render('LEVEL', True, (192, 192, 0)), (513, 20))
            screen.blit(self.app_handler.assets.font.render(str(self.game_handler.level.id + 1), True, 'white'), (513, 50))