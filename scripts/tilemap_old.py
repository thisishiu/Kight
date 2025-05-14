# from scripts.settings import *

# NEIGHTBOR_OFFSETS = [(-1, 1), (-1, 0), (1, 1), (-1, 0), (0, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

# class Tilemap:
#     def __init__(self, game, tile_size = TILE_SIZE):
#         self.game = game
#         self.tile_size = tile_size
#         self.tilemap = {}
#         self.offgrid_tiles = []
        
#         # test
#         # for i in range(2,4):
#         #     for j in range(1,4):
#         #         self.tilemap[str(i) + ';' + str(j)] = {'type' : 'stone_bottom', 'varian' : 5, 'pos' : (i, j)}
#         # self.tilemap['2;1'] = {'type' : 'stone_bottom', 'varian' : 15, 'pos' : (2, 1)}
        
        
#     def tile_around(self, pos):
#         tile = []
#         tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size)) 
#         for offset in NEIGHTBOR_OFFSETS:
#             check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
#             if check_loc in self.tilemap:
#                 tile.append(self.tilemap[check_loc])
#         return tile
        
#     def render(self, surf):
#         for tile in self.offgrid_tiles:
#             surf.blit(self.game.assets[tile['type']][tile['varian']], tile['pos'])
#         # i = 0
#         for tile in self.tilemap.values():
#             surf.blit(self.game.assets[tile['type']][tile['varian']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))
#             # surf.blit(pygame.image.load('assets/player/charactor_af_process/charactor.png'), (i*self.tile_size, i*self.tile_size))
#             # i += 1
        

import sqlite3
# import pygame ?
from scripts.settings import *

database = sqlite3.connect('database/Knight_database.db')
cursor = database.cursor()

# cursor.execute("""
# select * from TileMap_1;
#                """)

# dataMap_1 = cursor.fetchall()

class TileMap:
    def __init__(self, game, tile_size = TILE_SIZE):
        self.game = game
        self.tile_size = tile_size
        
    def __add_TileMap_1(self):
        cursor.execute("""
insert into TileMap_1
values                  
    (1, 1, 1, 'ground', 'grass', 1),
	(1, 2, 1, 'ground', 'grass', 21),
	
	(2, 1, 1, 'ground', 'grass', 3),
	(2, 2, 1, 'ground', 'grass', 13),
	(2, 3, 1, 'ground', 'grass', 11),
	(2, 4, 1, 'ground', 'grass', 11),
	(2, 5, 1, 'ground', 'grass', 11),
	(2, 6, 1, 'ground', 'grass', 11),
	(2, 7, 1, 'ground', 'grass', 21),
	
	(3, 1, 1, 'ground', 'grass', 4),
	(3, 2, 1, 'ground', 'grass', 13),
	(3, 3, 1, 'ground', 'grass', 13),
	(3, 4, 1, 'ground', 'grass', 13),
	(3, 5, 1, 'ground', 'grass', 13),
	(3, 6, 1, 'ground', 'grass', 13),
	(3, 7, 1, 'ground', 'grass', 23),
	
	(4, 2, 1, 'ground', 'grass', 3),
	(4, 3, 1, 'ground', 'grass', 13),
	(4, 4, 1, 'ground', 'grass', 13),
	(4, 5, 1, 'ground', 'grass', 13),
	(4, 6, 1, 'ground', 'grass', 14),
	(4, 7, 1, 'ground', 'grass', 24),
	
	(5, 2, 1, 'ground', 'grass', 3),
	(5, 3, 1, 'ground', 'grass', 13),
	(5, 4, 1, 'ground', 'grass', 14),
	(5, 5, 1, 'ground', 'grass', 24),

	(6, 1, 1, 'ground', 'grass', 1),
	(6, 2, 1, 'ground', 'grass', 13),
	(6, 3, 1, 'ground', 'grass', 23),
	
	(7, 1, 1, 'ground', 'grass', 3),
	(7, 2, 1, 'ground', 'grass', 13),
	(7, 3, 1, 'ground', 'grass', 23),
	
	(8, 1, 1, 'ground', 'grass', 4),
	(8, 2, 1, 'ground', 'grass', 14),
	(8, 3, 1, 'ground', 'grass', 24);
               """)
        
    def TileMap(self, map):
        cursor.execute(f"""
select * from TileMap_{map}
order by y;
               """)
        data = dict()
        for i in cursor.fetchall():
            if i[2] not in data.keys():
                # data[i[2]] = {'ground': [],
                #               'wall': [],
                #               'deco': []}
                data[i[2]] = [[(i[0], i[1]), i[3], i[4], i[5]]]
            else:
                data[i[2]].append([(i[0], i[1]), i[3], i[4], i[5]])
        return data
        
    def __add_TileMap_2(self):
        cursor.execute("""
insert into TileMap_2
values
    (4, 2, 1, 'ground', 'stone', 0),
    (4, 3, 1, 'ground', 'stone', (abs(random()) % 2) * (8 - 4) + 4),
    (4, 4, 1, 'ground', 'stone', (abs(random()) % 2) * (8 - 4) + 4),
    (4, 5, 1, 'ground', 'stone', (abs(random()) % 2) * (8 - 4) + 4),
    (4, 6, 1, 'ground', 'stone', (abs(random()) % 2) * (8 - 4) + 4),
    (4, 7, 1, 'ground', 'stone', 12),
    
    (5, 2, 1, 'ground', 'stone', 1),
    (5, 3, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (5, 4, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (5, 5, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (5, 6, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (5, 7, 1, 'ground', 'stone', 13),
    
    (6, 2, 1, 'ground', 'stone', 1),
    (6, 3, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (6, 4, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (6, 5, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (6, 6, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (6, 7, 1, 'ground', 'stone', 13),
    
    (7, 2, 1, 'ground', 'stone', 1),
    (7, 3, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (7, 4, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (7, 5, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (7, 6, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (7, 7, 1, 'ground', 'stone', 13),
    
    (8, 2, 1, 'ground', 'stone', 1),
    (8, 3, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (8, 4, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (8, 5, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (8, 6, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (8, 7, 1, 'ground', 'stone', 13),
    
    (9, 2, 1, 'ground', 'stone', 1),
    (9, 3, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (9, 4, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (9, 5, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (9, 6, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (9, 7, 1, 'ground', 'stone', 13),
    
    (10, 2, 1, 'ground', 'stone', 1),
    (10, 3, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (10, 4, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (10, 5, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (10, 6, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (10, 7, 1, 'ground', 'stone', 13),
    
    (11, 2, 1, 'ground', 'stone', 1),
    (11, 3, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (11, 4, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (11, 5, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (11, 6, 1, 'ground', 'stone', (abs(random()) % 2) * (9 - 5) + 5),
    (11, 7, 1, 'ground', 'stone', 13),
    
    (12, 2, 1, 'ground', 'stone', 2),
    (12, 3, 1, 'ground', 'stone', (abs(random()) % 2) * (10 - 6) + 6),
    (12, 4, 1, 'ground', 'stone', (abs(random()) % 2) * (10 - 6) + 6),
    (12, 5, 1, 'ground', 'stone', (abs(random()) % 2) * (10 - 6) + 6),
    (12, 6, 1, 'ground', 'stone', (abs(random()) % 2) * (10 - 6) + 6),
    (12, 7, 1, 'ground', 'stone', 14);
         """)
        
    def render(self):
        pass

# print(TileMap(1).TileMap_1())

