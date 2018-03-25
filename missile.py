'''
Game : Space Invaders
Author : Pulkit Gera
'''


import pygame
import colours as col

class Missile:
    
    def __init__(self,x,y,width,height,speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height

    def retx(self):
        return self.x
    
    def rety(self):    
        return self.y

    def retspeed(self):
        return self.speed
    
class Shorty(Missile):

    def __init__(self,x,y,width,height,speed):
        Missile.__init__(self,x,y,speed,width,height)

    def draw(self):
        pygame.draw.rect(col.gameDisplay,col.white,(self.x,self.y,self.height,self.width))

class Longy(Missile):

    def __init__(self,x,y,width,height,speed):
        Missile.__init__(self,x,y,speed,width,height)

    def draw(self):
        pygame.draw.rect(col.gameDisplay,col.red,(self.x,self.y,self.height,self.width))




