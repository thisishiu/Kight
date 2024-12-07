import pygame
from scripts.entities import *
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
        self.assets = {
            # 'player' : load_image('player/charactor_af_process/charactor.png'),
            'stone' : load_images('tilemap/ground/stone'),
            'grass' : load_images('tilemap/ground/grass'),
            'wall' : load_images('tilemap/ground/grass')
        }
        
        # entities
        self.entities = pygame.sprite.Group()
        
        # player
        self.player = Player((8*TILE_SIZE,6*TILE_SIZE))
        self.entities.add(self.player)
        
        # enemy
        self.enemy = Enemy((8*TILE_SIZE,3*TILE_SIZE))
        self.entities.add(self.enemy)
        
        # map 
        self.TileMap = TileMap(self)
        self.map = self.TileMap.TileMap(2)
        
        # set camera
        self.display = Camera(self, self.player)
        
    def run(self):
        while self.game_run:
            # quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_run = False
            
            # clean screen, display
            self.screen.fill((0, 0, 0)) 

            # player
            keys = pygame.key.get_pressed()
            self.player.update(keys)
            self.enemy.update(self.player.pos)
            
            # update screen
            self.display.surface.fill((125, 200, 255))
            self.display.render(self.screen)
             
            pygame.display.update()
            
Game().run()
