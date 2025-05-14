import pygame
from scripts.settings import *
from scripts.utils import *

class PhysicsEntity(pygame.sprite.Sprite):
    def __init__(self, pos, e_type):
        super().__init__()
        self.e_type = e_type
        self.pos = pygame.math.Vector2(pos)
        self.velocity = pygame.math.Vector2(0,0)  # (x, y)
        
    
    def update(self, *args, **kwargs): ...
    
class Player(PhysicsEntity):
    def __init__(self, pos, e_type='player'):
        super().__init__(pos, e_type)
        self.speed = PLAYER_SPEED
        self.sprite_sheet = 'player/character_3_sheet_DONE-sheet.png'
        
        self.state = 'idle'     # default state
        self.__last_state = self.state    # lated state of player, default is idle_1
        
        self.__frame_time = { # time between two frames of an action
            'hurt': 1000 // FPS,
            'attack_1': 1000 // FPS * 5, 
            'idle': 1000 // FPS * 20,
            'road': 1000 // FPS * 5,
            'attack_2': 1000 // FPS * 5, 
            'run': 1000 // FPS * 5,
            'die': 1000 // FPS,
        }
        self.__act = [act for act in self.__frame_time.keys()]
        self.__counter = 0
        self.frame_size = [96, 40]
        self.frame = self.__preloadImage(self.sprite_sheet) # a sheet
        self.current_frame_index = 0    # index of frame(list)
        self.current_frame = self.frame[self.state][self.current_frame_index]
        self.mask = pygame.mask.from_surface(self.frame[self.state][self.current_frame_index])
        self.mask_flag = True
        
        self.__directions = {1: 'right', -1: 'left'}    # asset has two directions
        self.direction = self.__directions[1]   # default diretion is right
        
        self.__last_update_time = pygame.time.get_ticks()   # time of the last frame action
        
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.frame_size[0], self.frame_size[1])

        
    def __preloadImage(self, link):
        sprite_sheet = load_image(link)
        frames = {}
        sheet_width, sheet_height = sprite_sheet.get_size()
        rows = sheet_height // self.frame_size[1]
        columns = sheet_width // self.frame_size[0]
        for y in range(rows):
            name = self.__act[y]
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
        move_x = (keys[pygame.K_d] - keys[pygame.K_a])  # movement each axes
        move_y = (keys[pygame.K_s] - keys[pygame.K_w])
         
        if move_x and move_y: # diagonal move
            movement = pygame.Vector2(move_x, move_y).normalize()*self.speed
        else:
            movement = pygame.Vector2(move_x * self.speed, move_y * self.speed)
        
        __current_time = pygame.time.get_ticks()
        
        self.mask_flag = True
        self.__counter = max(0, self.__counter)
        if not self.__counter:
            if keys[pygame.K_k]:
                self.state = 'attack_2'
                self.__counter = len(self.frame['attack_2'])
            elif keys[pygame.K_SPACE]:
                self.state = 'road'
                self.__counter = len(self.frame['road'])
            elif move_x or move_y:
                self.state = 'run'
            elif not (move_x or move_y):
                self.state = 'idle'
        else:
            if self.state == 'attack_2':
                movement = pygame.Vector2(0,0)    # can not move when attack
            elif self.state == 'road':
                if self.__counter != 7 and self.__counter != 6:
                    movement = pygame.Vector2(0,0)
                else:
                    self.mask_flag = False
                movement = movement * 3
    
        if move_x:  # direction of frame
            self.direction = self.__directions[move_x]
            
        if self.__last_state == self.state:
            if __current_time - self.__last_update_time > self.__frame_time[self.state]:
                self.current_frame_index = (self.current_frame_index + 1) % len(self.frame[self.state])
                self.__last_update_time = __current_time
                if self.direction == 'right':
                    self.current_frame = self.frame[self.state][self.current_frame_index]
                else:
                    self.current_frame = pygame.transform.flip(self.frame[self.state][self.current_frame_index], True, False)
                if self.mask_flag:
                    self.mask = pygame.mask.from_surface(self.current_frame)
                else:
                    self.mask = None
                self.__counter = self.__counter - 1
        else:
            self.current_frame_index = 0
            self.__last_update_time = __current_time
            self.__last_state = self.state
            if self.direction == 'right':
                self.current_frame = self.frame[self.state][self.current_frame_index]
            else:
                self.current_frame = pygame.transform.flip(self.frame[self.state][self.current_frame_index], True, False)
            if self.mask_flag:
                    self.mask = pygame.mask.from_surface(self.current_frame)
            else:
                self.mask = None
        
        # uodate pos
        self.pos += movement + self.velocity
        self.rect.topleft = self.pos
        
        # print('===>',self.mask_flag)
        
class Enemy(PhysicsEntity):
    def __init__(self, pos, e_type='enemy'):
        super().__init__(pos, e_type)
        self.speed = 0.1
        self.sprite_sheet = 'enemy/darkboss/boss.png'
        
        self.state = 'idle'     # default state
        self.__last_state = self.state    # lated state of player, default is idle
        
        self.__frame_time = { # time between two frames of an action
            'idle': 1000 // FPS * 6,
            'walk': 1000 // FPS * 6,
            'attack': 1000 // FPS * 8, 
            'turn back': 1000 // FPS * 20
        }
        self.__act = [act for act in self.__frame_time.keys()]
        self.__counter = 0
        self.frame_size = [256, 96]
        self.frame = self.__preloadImage(self.sprite_sheet) # a sheet
        self.current_frame_index = 0    # index of frame(list)
        self.current_frame = self.frame[self.state][self.current_frame_index]
        self.mask = pygame.mask.from_surface(self.frame[self.state][self.current_frame_index])
        self.mask_flag = True
        
        self.__directions = {1: 'right', -1: 'left'}    # asset has two directions
        self.direction = self.__directions[1]   # default diretion is right
        self.__last_direction = self.direction
        self.attacking = False
        self.moving = False
        
        self.__last_update_time = pygame.time.get_ticks()   # time od the last frame action
        
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.frame_size[0], self.frame_size[1])
        
        
    def __preloadImage(self, link):
        sprite_sheet = load_image(link)
        frames = {}
        sheet_width, sheet_height = sprite_sheet.get_size()
        rows = sheet_height // self.frame_size[1]
        columns = sheet_width // self.frame_size[0]
        for y in range(rows):
            name = self.__act[y]
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
    
    def update(self, player_pos: pygame.Vector2, player_status: str, player_size:  list):
        distance_x = int(player_pos.x + player_size[0]/2 - self.pos.x - self.frame_size[0]/2)
        distance_y = int(player_pos.y + player_size[1] - self.pos.y - self.frame_size[1])
        
        def isInAttackRange(attacking):
            if attacking:
                return False
            elif -70 < distance_x < 70 and -10 < distance_y < 15:
                self.attacking = True
                return True
            
        def move():
            pass    
        
        # print(isInAttackRange())
        
        movement_x = distance_x
        movement_y = distance_y
        
        if movement_x or movement_y:
            movement = pygame.Vector2(movement_x, movement_y).normalize()*self.speed
        else:
            movement = pygame.Vector2(0, 0)*self.speed
        
        if movement_x:
            self.direction = self.__directions[movement_x//abs(movement_x)]
            
        if isInAttackRange(self.attacking) and self.state != 'attack':
            self.state = 'attack'
            self.__counter = len(self.frame['attack']) + 1
            movement = pygame.Vector2(0,0)
            self.direction = self.__last_direction
            
        else:
            self.__counter = max(0, self.__counter)    
            if not self.__counter:
                if movement_x or movement_y:
                    self.state = 'walk'
                    self.__counter = 14
                else:
                    self.state = 'idle'
                self.attacking = False
            else:
                if self.state == 'walk':
                    if self.__counter in [1, 2, 3, 7, 8,9]: # [4, 5, 6, 9, 10, 11, 12] is moving
                        movement = pygame.Vector2(0, 0)
                elif self.state == 'attack':
                    movement = pygame.Vector2(0,0)
                    self.direction = self.__last_direction
            
        __current_time = pygame.time.get_ticks()
        
        if self.__last_state == self.state:
            if __current_time - self.__last_update_time > self.__frame_time[self.state]:
                self.current_frame_index = (self.current_frame_index + 1) % len(self.frame[self.state])
                self.__last_update_time = __current_time
                self.__last_direction = self.direction
                if self.direction == 'right':
                    self.current_frame = self.frame[self.state][self.current_frame_index]
                else:
                    self.current_frame = pygame.transform.flip(self.frame[self.state][self.current_frame_index], True, False)
                if self.mask_flag:
                    self.mask = pygame.mask.from_surface(self.current_frame)
                else:
                    self.mask = None
                self.__counter = self.__counter - 1
        else:
            self.current_frame_index = 0
            self.__last_update_time = __current_time
            self.__last_state = self.state
            self.__last_direction = self.direction

            if self.direction == 'right':
                self.current_frame = self.frame[self.state][self.current_frame_index]
            else:
                self.current_frame = pygame.transform.flip(self.frame[self.state][self.current_frame_index], True, False)
            if self.mask_flag:
                    self.mask = pygame.mask.from_surface(self.current_frame)
            else:
                self.mask = None
            
        self.pos += movement + self.velocity
        self.rect.topleft = self.pos

# pygame.sprite.GroupSingle()
        # print("--->", self.attacking, isInAttackRange(self.attacking))