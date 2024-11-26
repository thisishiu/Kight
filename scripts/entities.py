import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.e_type = e_type
        self.pos = list(pos)    # (x, y)
        self.size = size
        self.velocity = [0, 0]  # (x, y)
        self.scale_velocity = 0.75
        
    def update(self, movement=[0,0]):
        if (movement[0] and movement[1]):
            frame_movement = [movement[0] * self.scale_velocity / (2**0.5) + self.velocity[0], movement[1] * self.scale_velocity / (2**0.5) + self.velocity[1]]
        else:        
            frame_movement = [movement[0] * self.scale_velocity + self.velocity[0], movement[1] * self.scale_velocity + self.velocity[1]]
        
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]
        
    def render(self, surf):
        surf.blit(self.game.assets[self.e_type], self.pos)