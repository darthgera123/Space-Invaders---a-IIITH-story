'''
Game : Space Invaders
Author : Pulkit Gera
'''

import pygame
import colours as col
import random
import time
from enemy import Enemy
from missile import Missile
from ship import Ship
#function to check for collisions
def check(short,trail,zombie):
    count=0
    to_remove_missile=[]
    to_remove_alien=[]
    for i in trail:
        for s in short:
            if i.retx()-40<=s.retx() and i.retx()+40>=s.retx() and i.rety()-40<=s.rety() and i.rety()+40>=s.rety():
                to_remove_missile.append(s)
                to_remove_alien.append(i)

    for i in zombie:
        for s in short:
            if i.retx()-40<=s.retx() and i.retx()+40>=s.retx() and i.rety()-40<=s.rety() and i.rety()+40>=s.rety():
                to_remove_missile.append(s)
                to_remove_alien.append(i)

    for s in to_remove_alien:
        if s in trail:
            trail.remove(s)
            count = count+1 
        if s in zombie:
            zombie.remove(s)
            count = count+1           
    
    for m in to_remove_missile:
        if m in short:
            short.remove(m)
    return count
#function to check for stunned
def torture(trail,longm,zombie):
    to_remove_missile=[]
    to_remove_alien=[]
    for i in trail:
        for s in longm:
            if i.retx()-40<=s.retx() and i.retx()+40>=s.retx() and i.rety()-40<=s.rety() and i.rety()+40>=s.rety():
                to_remove_missile.append(s)
                to_remove_alien.append(i)

    for s in to_remove_alien:
        if s in trail:
            s.zombied()
            zombie.append(s)
            trail.remove(s)
            
    for m in to_remove_missile:
        if m in longm:
            longm.remove(m)
#function to create a new alien
def create(trail):
	p = random.randint(col.display_width*0.1,col.display_width*0.8)
	q = random.randint(col.display_height*0.2,col.display_height*0.3)
	generate=round(time.time())
	palpatine = Enemy(p,q,generate)
	trail.append(palpatine)
#function to destro alien
def destroy(trail,zombie,current):
    for i in trail:
        if (current - i.rettime())%i.retlife() == 0 and current - i.rettime() != 0:
            trail.remove(i)
    for i in zombie:
        if (current - i.rettime())%i.retlife() == 0 and current - i.rettime() != 0:
            zombie.remove(i)

