import json #, sys

import pygame
from pygame.locals import *
import random

from const import *
from schedule import *

class Level:
    def __init__(self, player, ghost):
        self.id = 0
        self.score = 0
        self.player = player
        self.ghost = ghost
        self.void_tile = pygame.Surface((TILE_SIZE, TILE_SIZE))
        self.void_tile.fill('black')

    def set(self, type, mode):
        if type == 'new':
            self.id = 0
        elif type == 'retry':
            pass
        elif type == 'complete':
            self.id += 1
        if mode == 'arcade':
            with open('levels/built-in/lvl0.json', "rb") as raw: level_data = json.loads(raw.read())
        elif mode == 'adventure':
            with open('levels/built-in/lvl' + str(self.id) + '.json', "rb") as raw: level_data = json.loads(raw.read())
        elif mode == 'custom':
            with open('addgames/' + str(self.id) + '.json', "rb") as raw: level_data = json.loads(raw.read())

        self.map = level_data['MAP']
        self.map_width = len(self.map[0])
        self.map_height = len(self.map)

        self.player.map_pos = tuple(level_data['PLAYER_POS'])
        self.player.update_screen_pos()

        for ghost in self.ghost:
            ghost.map_pos = tuple(level_data['GHOST_POS'][self.ghost.index(ghost)])
            ghost.update_screen_pos()

    def map_void(self, map_pos):
        self.map[map_pos[1]][map_pos[0]] = 'VOID'
        self.map_surface.blit(self.void_tile, (TILE_SIZE * map_pos[0], TILE_SIZE * map_pos[1]))

    def map_complete(self):
        for row in self.map:
            if 'PACGUM' in row: 
                return False
        return True

    def map_draw(self, assets):
        self.map_surface = pygame.Surface((TILE_SIZE * self.map_width, TILE_SIZE * self.map_height), SRCALPHA | RLEACCEL)
        for row in range(self.map_width):
            for col in range(self.map_height):
                self.map_surface.blit(assets.sprite[self.map[col][row]], (TILE_SIZE * row, TILE_SIZE * col))

    def update(self):
        for ghost in self.ghost:
            if Rect(self.player.screen_pos[0] + 1, self.player.screen_pos[1] + 1, 14, 14).colliderect(Rect(ghost.screen_pos[0] + 1, ghost.screen_pos[1] + 1, 14, 14)):
                self.player.can_move = False
                self.player.death_index = 0

            if ghost.on_tile():
                if ghost.map_pos[0] < 0:
                    ghost.map_pos = (28, ghost.map_pos[1])
                    ghost.update_screen_pos()

                elif ghost.map_pos[0] > 27:
                    ghost.map_pos = (-1, ghost.map_pos[1])
                    ghost.update_screen_pos()

                elif ghost.map_pos[0] == 0:
                    pass

                elif ghost.map_pos[0] == 27:
                    pass

                else:
                    directions = DIRECTION.copy()
                    wall_types = WALLS if ghost.out else WALLS_NO_GHOST
                    while TILEID[self.map[ghost.map_pos[1] + ghost.direction[1]][ghost.map_pos[0] + ghost.direction[0]]] in wall_types:
                        random.shuffle(directions)
                        ghost.direction = directions.pop()

                    if TILEID[self.map[ghost.map_pos[1]][ghost.map_pos[0]]] == TILEID.WALL_GHOST:
                        ghost.direction = (0, -1)
                        ghost.out = True

                    for direction in DIRECTION:
                        if random.choice((True, False)) and random.choice((True, False)):
                            if TILEID[self.map[ghost.map_pos[1] + direction[1]][ghost.map_pos[0] + direction[0]]] not in wall_types:
                                if tuple(map(sum, zip(ghost.direction, direction))) != (0, 0):
                                    ghost.direction = direction

        # We test stuff relative to tiles every time the player is on a specific tile
        # While moving between 2 tiles the movement should be already allowed and the actions related to previous tile already done
        if self.player.on_tile():
            # Eating pac-gums
            if self.player.map_pos[0] < 0:
                self.player.next_direction = self.player.direction
                self.player.map_pos = (28, self.player.map_pos[1])
                self.player.update_screen_pos()
                return

            elif self.player.map_pos[0] > 27:
                self.player.next_direction = self.player.direction
                self.player.map_pos = (-1, self.player.map_pos[1])
                self.player.update_screen_pos()
                return

            if TILEID[self.map[self.player.map_pos[1]][self.player.map_pos[0]]] == TILEID.PACGUM:
                self.map_void(self.player.map_pos)
                self.score += 10
                if self.map_complete():
                    Schedule.level_type = 'complete'
                    Schedule.level_set_started = True
                    return

            elif TILEID[self.map[self.player.map_pos[1]][self.player.map_pos[0]]] == TILEID.POWER_PACGUM:
                self.map_void(self.player.map_pos)
                self.score += 80

            # Movement related to next tile
            # When player is stopped, we stop movement if the tile it's facing is a wall
            if self.player.direction == (0, 0):
                if TILEID[self.map[self.player.map_pos[1] + self.player.next_direction[1]][self.player.map_pos[0] + self.player.next_direction[0]]] in WALLS:
                    self.player.direction = self.player.next_direction = (0, 0)

            # When player is moving, we stop movement if we're facing a wall, and if there's a movement cache, we test if the cached movement is possible and we stop it otherwise
            # Movement cache starts when the player is at 1 tile worth or less pixels of the next tile
            else:
                if self.player.map_pos[0] == 0:
                    pass
                elif self.player.map_pos[0] == 27:
                    pass
                elif TILEID[self.map[self.player.map_pos[1] + self.player.direction[1]][self.player.map_pos[0] + self.player.direction[0]]] in WALLS:
                    if self.player.direction == self.player.next_direction:
                        self.player.next_direction = (0, 0)
                    else:
                        if TILEID[self.map[self.player.map_pos[1] + self.player.next_direction[1]][self.player.map_pos[0] + self.player.next_direction[0]]] in WALLS:
                            self.player.next_direction = (0, 0)
                elif TILEID[self.map[self.player.map_pos[1] + self.player.next_direction[1]][self.player.map_pos[0] + self.player.next_direction[0]]] in WALLS:
                    self.player.next_direction = self.player.direction

        else:
            if self.player.direction != (0, 0) and self.player.initial_pos:
                self.player.initial_pos = False
                if TILEID[self.map[int(self.player.map_pos[1] + self.player.direction[1])][int(self.player.map_pos[0] + self.player.direction[0])]] in WALLS:
                    self.player.direction = self.player.next_direction = (0, 0)
                    self.player.initial_pos = True