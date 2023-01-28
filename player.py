from const import *

class Player:
    def __init__(self):
        self.map_pos = (0, 0)
        self.screen_pos = (0, 0)
        self.initial_pos = True
        self.direction = (0, 0)
        self.next_direction = (0, 0)
        self.display_direction = (1, 0)
        self.can_move = True
        self.death_index = 0

    def update_map_pos(self):
        if self.initial_pos:
            self.map_pos = tuple([p / TILE_SIZE for p in self.screen_pos])
        else:
            self.map_pos = tuple([int(p / TILE_SIZE) for p in self.screen_pos])

    def update_screen_pos(self):
        self.screen_pos = tuple([p * TILE_SIZE for p in self.map_pos])

    def on_tile(self):
        return self.screen_pos[0] % TILE_SIZE == 0 and self.screen_pos[1] % TILE_SIZE == 0

    def update(self):
        if self.on_tile() or self.initial_pos:
            self.direction = self.next_direction
        if self.can_move:
            self.screen_pos = tuple(map(sum, zip(self.screen_pos, self.direction)))
            self.update_map_pos()
        else:
            self.death_index += 1