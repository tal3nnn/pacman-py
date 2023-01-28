import pygame
from pygame.locals import *
import io
import json

from const import *

class Assets:
    def __init__(self):
        self.unextract('all')

    def extract(self, index):
        if index == 0:
            self.branding = pygame.image.load('assets/branding.png').convert_alpha()
            self.black_screen = pygame.Surface(WINDOW_SIZE)

        elif index == 1:
            with open('assets/pixelNes.otf', "rb") as raw: font_file = raw.read()
            self.font = pygame.font.Font(io.BytesIO(font_file), 20)

        elif index == 2:
            sheet = pygame.image.load('assets/pacman_sheet.png').convert_alpha()
            with open('assets/pacman_sheet.json', "rb") as raw: sheet_pos = json.loads(raw.read())

            default_sprite = pygame.Surface((TILE_SIZE, TILE_SIZE), SRCALPHA | RLEACCEL)
            for element in sheet_pos:
                sprite = default_sprite.copy()
                sprite.blit(sheet, tuple([-p * TILE_SIZE for p in sheet_pos[element]]))
                self.sprite[element] = sprite

            self.title = pygame.image.load('assets/title.png').convert_alpha()
            self.title = pygame.transform.scale(self.title, (self.title.get_width() * 2, self.title.get_height() * 2))

            with open('assets/pixelNes.otf', "rb") as raw: font_file = raw.read()
            self.font_mid = pygame.font.Font(io.BytesIO(font_file), 30)
            self.font_big = pygame.font.Font(io.BytesIO(font_file), 40)

    def unextract(self, index):
        if index in [0, 'all']:
            self.branding = None
            self.black_screen = None

        if index in [1, 'all']:
            self.font = None

        if index in [2, 'all']:
            self.sprite = dict()
            self.title = None
            self.font_mid = self.font_big = None