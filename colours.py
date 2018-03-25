'''
Game : Space Invaders
Author : Pulkit Gera
'''
import pygame
display_width = 800
display_height = 600
black = (0,0,0)
white = (255,255,255)
red =(255,0,0)
green =(0,255,0)
yellow = (255, 255, 0)
blue =(0,0,255)
gameDisplay = pygame.display.set_mode((display_width,display_height))
#events for missile
MAYDAY = pygame.USEREVENT+1
HASTALAVISTA = pygame.USEREVENT+2
pygame.time.set_timer(MAYDAY,200)
pygame.time.set_timer(HASTALAVISTA,200)
