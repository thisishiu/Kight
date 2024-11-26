import pygame
from scripts.entities import PhysicsEntity
from scripts.utils import load_image, load_images
from scripts.tilemap import Tilemap
from scripts.settings import *

class Game:
    def __init__(self):
        # initial
        pygame.init()

        #create screen
        self.screen = pygame.display.set_mode((MAP_WIDTH,MAP_HEIGHT))
        self.display = pygame.Surface((DISPLAY_WIDTH,DISPLAY_HEIGHT))
        self.display_pos = [0, 0]

        # title and icon
            # title of the window game
        pygame.display.set_caption('Glory')
            # icon of the window game
        pygame.display.set_icon(pygame.image.load('sword.png'))

        # frame
        self.clock = pygame.time.Clock()
        self.clock.tick(60)

        # continue the game
        self.game_run = True 
        
        
        
        # # entity-------------------------------------
        #     # main_charater
        # self.main_character = pygame.image.load('assets/entity1.png')
        # self.main_character.set_colorkey((255,255,255))
        # self.main_character_position = [100,100]
        # self.main_character_movement_y = [False, False]
        # self.main_character_movement_x = [False, False]
        
        # # testing collision
        # self.wall = pygame.Rect(200, 200, 100, 100)
        #--------------------------------------------
        
        
        # assets
        self.assets = {
            'player' : load_image('player/charactor_af_process/charactor.png'),
            'stone_bottom' : load_images('arena/ground_af_process/stone'),
            'grass' : load_images('arena/ground_af_process/grass'),
            'wall_front' : load_images('arena/ground_af_process/grass')
        }
        
        self.layer = [
            ['stone_bottom'],
            ['grass'],
            ['wall_front'],
            ['player']
        ]
        
        # player
        # self.player_pos = (int(self.screen.get_width()/2), int(self.screen.get_height()/2))
        self.player_pos = (0,0)
        self.player = PhysicsEntity(self, 'player', self.player_pos, (self.assets['player'].get_width(),self.assets['player'].get_height())) 
        # self.movement = [False, False]
        self.player_movement_y = [False, False]
        self.player_movement_x = [False, False]
        # self.player.scale_velocity_x = 1
        # self.player.scale_velocity_y = 1 * 0.707
               
               
        # tile map
        self.tilemap = Tilemap(self)
                
    def run(self):
        while self.game_run:
            # set screen
            self.display.fill((255,255,255))
            
            # tile map
            self.tilemap.render(self.display)   
            
            # player
            self.player.update([self.player_movement_x[0] - self.player_movement_x[1], self.player_movement_y[0] - self.player_movement_y[1]])
            self.player.render(self.display)
            
            print(self.player.pos, end='  ')
            # print(self.tilemap.tile_around(self.player.pos))
            
            # screen
            self.display_pos = [min(MAP_WIDTH - DISPLAY_WIDTH, max(0, self.player.pos[0] - DISPLAY_WIDTH//2)), min(MAP_HEIGHT - DISPLAY_HEIGHT, max(0, self.player.pos[1] - DISPLAY_HEIGHT//2))]
            self.screen.blit(pygame.transform.scale(self.display, (DISPLAY_WIDTH, DISPLAY_HEIGHT)), (self.display_pos[0],self.display_pos[1]))
            
            # Event in game
            for event in pygame.event.get():
                # quit game
                if event.type == pygame.QUIT:
                    self.game_run = False
                    # pygame.quit()
                # moverment_key
                    # if press
                if event.type == pygame.KEYDOWN:
                    # move up
                    if event.key == pygame.K_w:
                        self.player_movement_y[1] = True
                    # move down
                    if event.key == pygame.K_s:
                        self.player_movement_y[0] = True 
                    # move right
                    if event.key == pygame.K_d:
                        self.player_movement_x[0] = True 
                    # move left    
                    if event.key == pygame.K_a: 
                        self.player_movement_x[1] = True 
                    # if release
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        self.player_movement_y[1] = False
                    if event.key == pygame.K_s:
                        self.player_movement_y[0] = False
                    if event.key == pygame.K_a:
                        self.player_movement_x[1] = False
                    if event.key == pygame.K_d:
                        self.player_movement_x[0] = False
  
            # update screen  
            # for layer in self.layer:
            #     self.assets[]
            
            # display_tmp_pos = [self.player.pos[0], self.player.pos[1]]
            # self.display_pos = [self.player.pos[0], self.player.pos[1]]
            
            
            # self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (self.display_pos[0], self.display_pos[1]))
            
            # display_tmp_pos = [self.player.pos[0] - int(self.display.get_width()/2), self.player.pos[1] - int(self.display.get_height()/2)]
            
            
            
            print(self.display_pos)
            pygame.display.update()

Game().run()