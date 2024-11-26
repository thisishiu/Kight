from scripts.settings import *

NEIGHTBOR_OFFSETS = [(-1, 1), (-1, 0), (1, 1), (-1, 0), (0, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

class Tilemap:
    def __init__(self, game, tile_size = TILE_SIZE):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {}
        self.offgrid_tiles = []
        
        # test
        for i in range(2,4):
            for j in range(1,4):
                self.tilemap[str(i) + ';' + str(j)] = {'type' : 'stone_bottom', 'varian' : 5, 'pos' : (i, j)}
        self.tilemap['2;1'] = {'type' : 'stone_bottom', 'varian' : 15, 'pos' : (2, 1)}
        
        
    def tile_around(self, pos):
        tile = []
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size)) 
        for offset in NEIGHTBOR_OFFSETS:
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            if check_loc in self.tilemap:
                tile.append(self.tilemap[check_loc])
        return tile
        
    def render(self, surf):
        for tile in self.offgrid_tiles:
            surf.blit(self.game.assets[tile['type']][tile['varian']], tile['pos'])
        # i = 0
        for tile in self.tilemap.values():
            surf.blit(self.game.assets[tile['type']][tile['varian']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))
            # surf.blit(pygame.image.load('assets/player/charactor_af_process/charactor.png'), (i*self.tile_size, i*self.tile_size))
            # i += 1
        