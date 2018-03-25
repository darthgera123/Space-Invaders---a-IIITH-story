'''
Game : Space Invaders
Author : Pulkit Gera
'''
import pygame
import colours as col

class Ship:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 150
        self.height = 20
        self.speed = 30

    def draw(self):
        pygame.draw.rect(col.gameDisplay,col.yellow,(self.x,self.y,self.width,self.height))
    
    def change(self,x_change,display_width):
        if self.x + x_change >= display_width-self.width:
            x_change=0
        elif self.x + x_change <= 0:
            x_change=0    
        self.x += x_change

    def retspeed(self):
        return self.speed
    def retx(self):
        return self.x    
