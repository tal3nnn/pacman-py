from const import *

class Ghost:
    def __init__(self):
        self.map_pos = (0, 0)
        self.screen_pos = (0, 0)
        self.direction = (0, -1)
        self.out = False

    def update_map_pos(self):
        self.map_pos = tuple([int(p / TILE_SIZE) for p in self.screen_pos])

    def update_screen_pos(self):
        self.screen_pos = tuple([p * TILE_SIZE for p in self.map_pos])

    def on_tile(self):
        return self.screen_pos[0] % TILE_SIZE == 0 and self.screen_pos[1] % TILE_SIZE == 0

    def update(self):
        self.screen_pos = tuple(map(sum, zip(self.screen_pos, self.direction)))
        self.update_map_pos()