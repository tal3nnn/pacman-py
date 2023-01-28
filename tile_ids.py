from enum import Enum

TILE_SIZE = 16
WINDOW_SIZE = (42 * TILE_SIZE, 31 * TILE_SIZE)

TILEID = Enum('TileID', ['VOID', 'WALL'])