'''
Game : Space Invaders
Author : Pulkit Gera
'''

import pygame
import colours as col

class Enemy:
    #initializing enemy object
    def __init__(self,x,y,time,life=8):
        self.x= x
        self.y =y
        self.time=time
        self.life = life
        
    #drawing the,
    def draw(self):
        pygame.draw.circle(col.gameDisplay,col.green,(self.x,self.y),40)

    def retx(self):
        return self.x
    
    def rety(self):
        return self.y
    #lifetime
    def retlife(self):
        return self.life
    #timestamp for creation
    def rettime(self):
        return self.time    
    
    def zombied(self,value=5):
        self.life+=value

    def drawz(self): 
        pygame.draw.circle(col.gameDisplay,col.blue,(self.x,self.y),20)