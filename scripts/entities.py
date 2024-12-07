import pygame
from scripts.settings import *
from scripts.utils import *

# import pygame
# from settings import *
# from utils import *

# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class PhysicsEntity(pygame.sprite.Sprite):
    def __init__(self, pos, e_type):
        super().__init__()
        self.e_type = e_type
        self.pos = pygame.math.Vector2(pos)
        self.velocity = pygame.math.Vector2(0,0)  # (x, y)
        
    # def update(self, movement=[0,0]): pass
    
class Player(PhysicsEntity):
    def __init__(self, pos, e_type='player'):
        super().__init__(pos, e_type)
        self.speed = PLAYER_SPEED
        self.sprite_sheet = 'player/charactor.png'
        
        self.__state = 'idle_1'     # default state
        self.__last_state = self.__state    # lated state of player, default is idle_1
        
        self.frame_size = [32, 32]
        self.frame = self.__preloadImage(self.sprite_sheet) # a sheet
        self.current_frame_index = 0    # index of frame(list)
        self.current_frame = self.frame[self.__state][self.current_frame_index]
        
        self.__directions = {1: 'right', -1: 'left'}    # asset has two directions
        self.direction = self.__directions[1]   # default diretion is right
        
        self.__last_update_time = pygame.time.get_ticks()   # time od the last frame action
        
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.frame_size[0], self.frame_size[1])
        
        self.__frame_time = { # time between two frames of an action
            'idle_1': 1000 // FPS * 20,
            'idle_2': 1000 // FPS,
            'idle_3': 1000 // FPS,
            'die': 1000 // FPS,
            'attack': 1000 // FPS * 5, 
            'walk': 1000 // FPS,
            'run': 1000 // FPS * 5,
            'jump': 1000 // FPS
        }
        
    def __preloadImage(self, link):
        """
        frame:
            0: idle 1 
            1: idle 2
            2: walk
            3: run
            4: idle 3
            5: jump
            6: faded
            7: die
            8: attack

        """
        
        sprite_sheet = load_image(link)
        frames = {}
        sheet_width, sheet_height = sprite_sheet.get_size()
        rows = sheet_height // self.frame_size[1]
        columns = sheet_width // self.frame_size[0]
        for y in range(rows):
            if y == 0:
                name = 'idle_1'
                frames[name] = []
            elif y == 1:
                name = 'idle_2'
                frames[name] = []
            elif y == 2:
                name = 'walk'
                frames[name] = []
            elif y == 3:
                name = 'run'
                frames[name] = []
            elif y == 4:
                name = 'idle_3'
                frames[name] = []
            elif y == 5:
                name = 'jump'
                frames[name] = []
            elif y == 6:
                name = 'faded'
                frames[name] = []
            elif y == 7:
                name = 'die'
                frames[name] = []
            elif y == 8:
                name = 'attack'
                frames[name] = []
            for x in range(columns):
                frame = sprite_sheet.subsurface(
                    pygame.Rect(
                        x * self.frame_size[0],
                        y * self.frame_size[1],
                        self.frame_size[0],
                        self.frame_size[1]
                    )
                ) #.copy()
                if self.__isEmptyFrame(frame):
                    frames[name].append(frame)
        return frames
                   
    def __isEmptyFrame(self, frame: pygame.Surface):
        for x in range(self.frame_size[0]):
            for y in range(self.frame_size[1]):
                if frame.get_at((x,y))[3] != 0:
                    return True
        return False

    def update(self, keys):             
        move_x = (keys[pygame.K_d] - keys[pygame.K_a])
        move_y = (keys[pygame.K_s] - keys[pygame.K_w])
        
        if move_x:  # direction of frame
            self.direction = self.__directions[move_x]
         
        if move_x and move_y: # diagonal move
            movement = pygame.Vector2(move_x, move_y).normalize()*self.speed + self.velocity
        else:
            movement = pygame.Vector2(move_x * self.speed, move_y * self.speed) + self.velocity
        
        __current_time = pygame.time.get_ticks()
        
        if keys[pygame.K_SPACE]:
            self.__state = 'attack'
            movement = self.velocity    # can not move when attack
        elif move_x or move_y:
            self.__state = 'run'
        elif not (move_x or move_y):
            self.__state = 'idle_1'
        
        if self.__last_state == self.__state:
            if __current_time - self.__last_update_time > self.__frame_time[self.__state]:
                self.current_frame_index = (self.current_frame_index + 1) % len(self.frame[self.__state])
                self.__last_update_time = __current_time
                if self.direction == 'right':
                    self.current_frame = self.frame[self.__state][self.current_frame_index]
                else:
                    self.current_frame = pygame.transform.flip(self.frame[self.__state][self.current_frame_index], True, False)
        else:
            self.current_frame_index = 0
            self.__last_update_time = __current_time
            self.__last_state = self.__state
            if self.direction == 'right':
                self.current_frame = self.frame[self.__state][self.current_frame_index]
            else:
                self.current_frame = pygame.transform.flip(self.frame[self.__state][self.current_frame_index], True, False)
        
        # uodate pos
        self.pos += movement
        self.rect.topleft = self.pos
            
            
        # print(self.pos[0])     

        
class Enemy(PhysicsEntity):
    def __init__(self, pos, e_type='enemy'):
        super().__init__(pos, e_type)
        self.speed = 10
        self.sprite_sheet = 'enemy/darkboss/boss.png'
        
        self.__state = 'idle'     # default state
        self.__last_state = self.__state    # lated state of player, default is idle_1
        
        self.frame_size = [240, 96]
        self.frame = self.__preloadImage(self.sprite_sheet) # a sheet
        self.current_frame_index = 0    # index of frame(list)
        self.current_frame = self.frame[self.__state][self.current_frame_index]
        
        self.__directions = {1: 'right', -1: 'left'}    # asset has two directions
        self.direction = self.__directions[1]   # default diretion is right
        
        self.__last_update_time = pygame.time.get_ticks()   # time od the last frame action
        
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.frame_size[0], self.frame_size[1])
        
        self.__frame_time = { # time between two frames of an action
            'idle': 1000 // FPS,
            # 'die': 1000 // FPS,
            'attack_1': 1000 // FPS, 
            'attack_2': 1000 // FPS, 
            'walk': 1000 // FPS,
            # 'run': 1000 // FPS * 5,
            # 'jump': 1000 // FPS
        }
        
        
        
    def __preloadImage(self, link):
        """
        frame:
            0: idle
            1: walk
            2: attack_1
            3: attack_2


        """
        
        sprite_sheet = load_image(link)
        frames = {}
        sheet_width, sheet_height = sprite_sheet.get_size()
        rows = sheet_height // self.frame_size[1]
        columns = sheet_width // self.frame_size[0]
        for y in range(rows):
            if y == 0:
                name = 'idle'
                frames[name] = []
            elif y == 1:
                name = 'walk'
                frames[name] = []
            elif y == 2:
                name = 'attack_1'
                frames[name] = []
            elif y == 3:
                name = 'attack-2'
                frames[name] = []
            for x in range(columns):
                frame = sprite_sheet.subsurface(
                    pygame.Rect(
                        x * self.frame_size[0],
                        y * self.frame_size[1],
                        self.frame_size[0],
                        self.frame_size[1]
                    )
                ) #.copy()
                if self.__isEmptyFrame(frame):
                    frames[name].append(frame)
        return frames
        
    def __isEmptyFrame(self, frame: pygame.Surface):
        for x in range(self.frame_size[0]):
            for y in range(self.frame_size[1]):
                if frame.get_at((x,y))[3] != 0:
                    return True
        return False
    
    def update(self, player_pos):
        pass
    
    
# frame = Player(0).frame  
        
# print(frame)

# while True:
#     screen.fill((255,255,255))
    
#     suf = pygame.Surface((100, 100))
#     for i in frame.keys():
#         for j in range(len(frame[i])):
            
#             screen.blit(frame[i][j], (i*64,j*64))
#     # screen.blit(suf, (100,100))

#     pygame.display.update()
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit(0)
    
#     pygame.display.update()
    