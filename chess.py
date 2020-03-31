import pygame
from pygame.locals import *

moves = [0]
fix = True

class boardTile:
    def __init__(self, name, pos, sprite=pygame.image.load("./images/missing.png"), piece=None):
        self.name = name
        self.pos = pos
        self.sprite = sprite
        self.piece = piece
        self.hitbox = [pos[0], pos[1], pos[0]+52, pos[1]+52]
        self.moved = False
        

    def update(self):
        global moves
        if self.is_pressed() and moves[-1] != self:
            moves.append(self)
            
        try:
            if moves[-1].piece == None and moves[-2].piece and moves[-2] == self and self.moved == False:
                self.moved = True
                return
            else:
                self.moved = False
                return
        except:
            pass
    
    def is_pressed(self):
        pos = pygame.mouse.get_pos()
        if (pos[0] > self.hitbox[0] and pos[1] > self.hitbox[1]) and (pos[0] < self.hitbox[2] and pos[1] < self.hitbox[3]) and (pygame.mouse.get_pressed()[0]):
            return True
        else:
            return False

class piece:
    def __init__(self, uid, name, sprite=pygame.image.load("./images/missing.png")):
        self.name = name
        self.sprite = sprite
        self.uid = uid
        if name[1] == "B":
            self.team = "B"
        elif name[1] == "W":
            self.team = "W"
            
