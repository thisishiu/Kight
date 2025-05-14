from scripts.settings import *
import pygame

class Camera:
    def __init__(self, game, target, size=(DISPLAY_WIDTH, DISPLAY_HEIGHT)):
        self.game = game
        self.target = target # object
        self.size = size
        self.surface = pygame.Surface(size)
        
        self.offset_x = min(MAP_WIDTH - DISPLAY_WIDTH, max(0, self.target.pos[0] - DISPLAY_WIDTH//2))
        self.offset_y = min(MAP_HEIGHT - DISPLAY_HEIGHT, max(0, self.target.pos[1] - DISPLAY_HEIGHT//2))
        
        self.box_pos = [LEFT, TOP]
        self.box_size = [self.size[0] - LEFT - RIGHT, self.size[1] - TOP - BOTTOM]
        
        self.rect = pygame.Rect(self.box_pos[0], self.box_pos[1], self.box_size[0] + self.target.frame_size[0], self.box_size[1] + self.target.frame_size[1])
        
    def render(self, surf):

        if self.target.pos[0] > self.offset_x + self.box_pos[0] + self.box_size[0]:
            self.offset_x = min(MAP_WIDTH - DISPLAY_WIDTH, max(0, self.target.pos[0] - (self.box_pos[0] + self.box_size[0])))
        if self.target.pos[0] < self.offset_x + self.box_pos[0]:
            self.offset_x = min(MAP_WIDTH - DISPLAY_WIDTH, max(0, self.target.pos[0] - self.box_pos[0]))
        if self.target.pos[1] < self.offset_y + self.box_pos[1]:
            self.offset_y = min(MAP_HEIGHT - DISPLAY_HEIGHT, max(0, self.target.pos[1] - self.box_pos[1]))
        if self.target.pos[1] > self.offset_y + self.box_size[1] + self.box_pos[1]:
            self.offset_y = min(MAP_HEIGHT - DISPLAY_HEIGHT, max(0, self.target.pos[1] - self.box_pos[1] - self.box_size[1]))
        
        # for layer in self.game.map:
        #     for tile in self.game.map[layer]:
        #         if (self.offset_x < tile[0][0] * TILE_SIZE + self.game.assets[tile[2]][tile[3]].get_size()[0]) and (self.offset_x + DISPLAY_WIDTH > tile[0][0] * TILE_SIZE) and (self.offset_y < tile[0][1] * TILE_SIZE + self.game.assets[tile[2]][tile[3]].get_size()[1]) and (self.offset_y + DISPLAY_HEIGHT > tile[0][1] * TILE_SIZE):
        #             self.surface.blit(self.game.assets[tile[2]][tile[3]], (tile[0][0]*TILE_SIZE - self.offset_x, tile[0][1]*TILE_SIZE - self.offset_y))
        self.surface.blit(self.game.TileMap.current_frame, (self.game.TileMap.pos[0]*TILE_SIZE - self.offset_x, self.game.TileMap.pos[1]*TILE_SIZE - self.offset_y))
        
        for entity in sorted(self.game.entities, key=lambda entity: entity.rect.bottomleft[1]):
            if entity == self.target:
                pygame.draw.rect(self.surface, (255, 100, 100), (self.target.rect.x - self.offset_x, self.target.rect.y - self.offset_y, self.target.frame_size[0], self.target.frame_size[1]))
                self.surface.blit(self.target.current_frame, (self.target.pos[0] - self.offset_x, self.target.pos[1] - self.offset_y))
                # if self.target.mask:
                #     self.surface.blit(self.target.mask.to_surface(setcolor=(255, 0, 0, 255)), (self.target.pos[0] - self.offset_x, self.target.pos[1] - self.offset_y))
            else:
                pygame.draw.rect(self.surface, (100, 255, 100), (entity.rect.x - self.offset_x, entity.rect.y - self.offset_y, entity.frame_size[0], entity.frame_size[1]))
                self.surface.blit(entity.current_frame, (entity.pos[0] - self.offset_x, entity.pos[1] - self.offset_y))
                # if entity.mask_flag:
                    # self.surface.blit(entity.mask.to_surface(setcolor=(0, 0, 255, 255), unsetcolor=(0,0,0,0)), (entity.pos[0] - self.offset_x, entity.pos[1] - self.offset_y))
                 
        # for block in range(len(self.game.TileMap.wall)):
        #     if self.game.player.mask.overlap(self.game.TileMap.wall[block], (self.game.player.pos.x - self.game.TileMap.wall_index[block][0], self.game.player.pos.y - self.game.TileMap.wall_index[block][1])):
        #         pygame.draw.rect(self.surface, (255, 0, 0), ((self.game.TileMap.wall_index[block][0])*TILE_SIZE - self.offset_x, (self.game.TileMap.wall_index[block][1])*TILE_SIZE - self.offset_y, self.game.TileMap.wall_size[block][0]*TILE_SIZE, self.game.TileMap.wall_size[block][1]*TILE_SIZE))
        # self.surface.blit(self.game.assets[self.target.e_type], (self.target.pos[0], self.target.pos[1]))
        
        # surf.blit(self.surface, (self.offset_x, self.offset_y))
        surf.blit(pygame.transform.scale(self.surface, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0,0))
        
        
        
        