import pygame
from scripts.entities import *
from scripts.logic import *
from scripts.utils import *
from scripts.tilemap import *
from scripts.settings import *
from scripts.camera import *

class Game:
    def __init__(self): 
        # set game
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # self.display = pygame.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        # self.display = Camera(self, self.player, )
        self.clock = pygame.time.Clock()
        self.clock.tick(FPS)
        self.game_run = True
        
        # assets
        # self.assets = {
        #     # 'player' : load_image('player/charactor_af_process/charactor.png'),
        #     'stone' : load_images('tilemap/ground/stone'),
        #     'grass' : load_images('tilemap/ground/grass'),
        #     'wall' : load_images('tilemap/ground/grass')
        # }
        
        # entities
        self.entities = pygame.sprite.Group()

        # map 
        self.TileMap = TileMap_1()
        # self.map = self.TileMap.TileMap(1)
        
        # enemy
        self.enemy = Enemy((self.TileMap.set_enemy_pos[0],self.TileMap.set_enemy_pos[1]))
        self.entities.add(self.enemy)
        self.enemies = pygame.sprite.GroupSingle(self.enemy)
        # print(self.enemy.mask.get_size())
        
        # player
        self.player = Player((self.TileMap.set_player_pos[0],self.TileMap.set_player_pos[1]))
        self.entities.add(self.player)
        self.players = pygame.sprite.GroupSingle(self.player)
        
        # set camera
        self.display = Camera(self, self.player)
        
    def run(self):
        while self.game_run:
            # quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_run = False
            
            # clean screen, display
            self.screen.fill((100, 100, 100)) 

            # map
            self.TileMap.update()

            # player
            keys = pygame.key.get_pressed()
            self.player.update(keys)
            self.enemy.update(self.player.pos, self.player.state, self.player.frame_size)
            
            # collision
            if self.player.mask:
                if self.player.mask.overlap(self.enemy.mask, (self.enemy.pos.x - self.player.pos.x, self.enemy.pos.y - self.player.pos.y)):
                    # print('1')
                    ...
                                
            # update screen
            self.display.surface.fill((125, 200, 255))
            self.display.render(self.screen)
             
            pygame.display.update()
            
Game().run()
