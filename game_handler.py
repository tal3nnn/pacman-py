from ghost import *
from level import *
from player import *
from schedule import *

class GameHandler:
    def __init__(self):
        self.mode = 'arcade'
        self.player = Player()
        self.ghost = [Ghost(), Ghost(), Ghost(), Ghost()]
        self.level = Level(self.player, self.ghost)
        self.lives = 3

    def update(self):
        if Schedule.level_set_started:
            for ghost in self.ghost:
                ghost.out = False
                ghost.direction = (0, -1)
            self.player.initial_pos = True
            self.player.display_direction = (1, 0)
            self.player.direction = self.player.next_direction = (0, 0)
            self.level.set(Schedule.level_type, self.mode)
            Schedule.level_set_started = False
            Schedule.level_set_finished = True

        elif self.player.death_index == 11:
            self.lives -= 1
            if self.lives == 0:
                Schedule.lost = str(self.level.score)
                self.level.score = 0
                return
            for ghost in self.ghost:
                ghost.out = False
                ghost.direction = (0, -1)
            self.player.initial_pos = True
            self.player.display_direction = (1, 0)
            self.player.direction = self.player.next_direction = (0, 0)
            self.player.can_move = True
            self.player.death_index = 0
            self.level.set('retry', self.mode)
            Schedule.level_set_finished = True

        else:
            self.level.update()
            for ghost in self.ghost:
                ghost.update()
            self.player.update()
            if self.player.death_index > 11:
                pass