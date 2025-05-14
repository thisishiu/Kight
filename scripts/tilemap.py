from scripts.settings import *
from scripts.utils import *

class TileMap:
    def __init__(self):
        self.tile_size = TILE_SIZE
    #     self.map_1 = [
    #         (4, 2, 1, 'ground', 'grass', 1),
    #         (4, 3, 1, 'ground', 'grass', 11),
    #         (4, 4, 1, 'ground', 'grass', 11),
    #         (4, 5, 1, 'ground', 'grass', 11),
    #         (4, 6, 1, 'ground', 'grass', 21),
            
    #         (5, 2, 1, 'ground', 'grass', 3),
    #         (5, 3, 1, 'ground', 'grass', 13),
    #         (5, 4, 1, 'ground', 'grass', 13),
    #         (5, 5, 1, 'ground', 'grass', 13),
    #         (5, 6, 1, 'ground', 'grass', 23),
            
    #         (6, 2, 1, 'ground', 'grass', 3),
    #         (6, 3, 1, 'ground', 'grass', 13),
    #         (6, 4, 1, 'ground', 'grass', 13),
    #         (6, 5, 1, 'ground', 'grass', 13),
    #         (6, 6, 1, 'ground', 'grass', 23),
            
    #         (7, 2, 1, 'ground', 'grass', 3),
    #         (7, 3, 1, 'ground', 'grass', 13),
    #         (7, 4, 1, 'ground', 'grass', 13),
    #         (7, 5, 1, 'ground', 'grass', 13),
    #         (7, 6, 1, 'ground', 'grass', 23),
            
    #         (8, 2, 1, 'ground', 'grass', 3),
    #         (8, 3, 1, 'ground', 'grass', 13),
    #         (8, 4, 1, 'ground', 'grass', 13),
    #         (8, 5, 1, 'ground', 'grass', 13),
    #         (8, 6, 1, 'ground', 'grass', 23),
            
    #         (9, 2, 1, 'ground', 'grass', 4),
    #         (9, 3, 1, 'ground', 'grass', 14),
    #         (9, 4, 1, 'ground', 'grass', 14),
    #         (9, 5, 1, 'ground', 'grass', 14),
    #         (9, 6, 1, 'ground', 'grass', 24),
    #     ]
    #     self.map = {
    #         1: self.map_1
    #     }

    # def TileMap(self, map):
    #     data = dict()
    #     for i in self.map[map]:
    #         if i[2] not in data.keys():
    #             # data[i[2]] = {'ground': [],
    #             #               'wall': [],
    #             #               'deco': []}
    #             data[i[2]] = [[(i[0], i[1]), i[3], i[4], i[5]]]
    #         else:
    #             data[i[2]].append([(i[0], i[1]), i[3], i[4], i[5]])
    #     return data
    def update(self): ...   

class TileMap_1(TileMap):
    def __init__(self):
        super().__init__()
        self.ground = load_images(r"tilemap/tilemap_1")
        self.pos = (0, 0)
        self.set_player_pos = (1 * TILE_SIZE, 1 * TILE_SIZE)
        self.set_enemy_pos = (2 * TILE_SIZE, 3 * TILE_SIZE)
        
        self.__current_frame_index = 0
        self.current_frame = self.ground[self.__current_frame_index]
        self.__frame_time = 1000//FPS * 8
        self.__last_update_time =  pygame.time.get_ticks()
        
        self.wall_size = [
            [1 * TILE_SIZE, 5 * TILE_SIZE],
            [5 * TILE_SIZE, 1 * TILE_SIZE],
            [1 * TILE_SIZE, 5 * TILE_SIZE],
            [5 * TILE_SIZE, 1 * TILE_SIZE]
        ]
        self.wall_index = [
            [0 * TILE_SIZE, 1 * TILE_SIZE],
            [1 * TILE_SIZE, 0 * TILE_SIZE],
            [6 * TILE_SIZE, 1 * TILE_SIZE],
            [1 * TILE_SIZE, 6 * TILE_SIZE]
        ]
        self.wall = [
            pygame.mask.from_surface(pygame.Surface((x[0]*TILE_SIZE, x[1]*TILE_SIZE))) for x in self.wall_size
        ]

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.__last_update_time > self.__frame_time:
            self.__current_frame_index = (self.__current_frame_index + 1) % len(self.ground)
            self.__last_update_time = current_time
            self.current_frame = self.ground[self.__current_frame_index]