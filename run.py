'''
Game : Space Invaders
Author : Pulkit Gera 
'''
import colours as col #This has all the colour constants and other constants
import pygame
import random
import time
from ship import Ship #the main ship
from missile import * #missile classes
from enemy import Enemy #enemy class
from functions import * #helper functions
'''
Importing all the game objects 
'''

pygame.init()
pygame.font.init()
#initializing pygame and pygame font
pygame.display.set_caption('Space Invaders')
clock = pygame.time.Clock()
running = True
#lists required
trail=[]	#list for aliens
short=[]	#list for missiles
longm=[]	#list for other type of missile
zombie=[]	#list for stunned aliens aka zombies

global count
count=0		#count of killed aliens
global available
available = 0	#availablity for creation

start = round(time.time())
#creation of ship object
ship=Ship((col.display_width * 0.45),(col.display_height * 0.94))    
#creation of initial alien
create(trail)
#x_change=0
while running:
    x_change=0
    current = round(time.time())
    #generation of alien every 10 seconds
    if (current - start)%10 == 0 and current-start !=0 and available ==0:
   		create(trail)
   		available =1
    
    if(current - start)%9 == 0:
   		available =0

   
    col.gameDisplay.fill(col.black)
    #event getting
    for event in pygame.event.get():    
        #event for short missile
        if event.type == col.MAYDAY:
            if len(short)>0:
                for s in short:
                    s.y -= s.retspeed()
        #event for long missile
        if event.type == col.HASTALAVISTA:
            if len(longm)>0:
                for s in longm:
                    s.y -=s.retspeed()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x_change = -ship.retspeed()
            #movement of ship
            elif event.key == pygame.K_d:
                x_change = ship.retspeed()
            #firing of missile
            elif event.key == pygame.K_s:
                missile = Shorty(ship.retx()+75,col.display_height*0.85,10,col.display_height*0.05,40)
                short.append(missile)
            
            elif event.key == pygame.K_SPACE:
                missile = Longy(ship.retx()+75,col.display_height*0.85,8,col.display_height*0.10,40)
                longm.append(missile)    
            elif event.key == pygame.K_q:
            	running = False
              
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_q:
                    x_change = 0 
                      
    #printing score
    myfonty = pygame.font.SysFont('Arial', 40)
    texty = myfonty.render('Score : '+str(count*10), False, (255, 255, 255))
    col.gameDisplay.blit(texty,(0,0))
    #updating the board
    ship.change(x_change,col.display_width)          
    ship.draw()
    
    if short:
    	for i in short:
        	i.draw()
    
    if longm:
    	for i in longm:
        	i.draw()
    
    if trail:
    	for i in trail:
        	i.draw()
    
    count = count+ check(short,trail,zombie)
    torture(trail,longm,zombie)
    
    if zombie:
    	for i in zombie:
    		i.drawz()
    
    destroy(trail,zombie,current)
    #create aliens if all destroyed
    if not trail :
    	create(trail)
    
           
    pygame.display.update()
    clock.tick(20)
    if running == False:
        col.gameDisplay.fill(col.black)
        col.gameDisplay.fill(col.yellow) 
        myfont = pygame.font.SysFont('Arial', 40)
        creditsfont = pygame.font.SysFont('Arial', 20)
        textsurface = myfont.render('Game Over', True, (0, 0, 0))
        text = myfont.render('Your Score is = '+str(count*10), False, col.black)
        creditsurface = creditsfont.render('A darth_gera production', False, col.red)
        col.gameDisplay.blit(textsurface,(col.display_width*0.35,col.display_height*0.4))
        col.gameDisplay.blit(text,(col.display_width*0.35,col.display_height*0.5))
        col.gameDisplay.blit(creditsurface,(col.display_width*0.35,col.display_height*0.96))
        print("Your score is = "+str(count*10))
        pygame.display.update()	
        time.sleep(2)
