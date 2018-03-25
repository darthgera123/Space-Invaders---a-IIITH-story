# Space-Invaders---a-IIITH-story
===================
*Coded by:*
**Pulkit Gera**

This **README** file contains :
 1. Information About the Game
 2. Rules of the Game
 3. Description of Classes Created
 4. Instructions on how to Run the Code
 5. Requirements

----------


About The Game
-------------

>***Space Invaders*** (Japanese: スペースインベーダー Hepburn: Supēsu Inbēdā) is an arcade video game created by Tomohiro Nishikado and released in 1978.

For more information click [here](https://en.wikipedia.org/wiki/Space_Invaders).

----------


Rules of the Game
-------------------

> - Rules are pretty simple
> - Enemies are created every 10 seconds or when none are present.
> - You have 2 types of missile.
> - The first destroys the enemy. 
> - The second type freezes the enemy for 5 seconds.

------------------------

Description of Classes Created
--------------------------------------------
####Ship:
Creates the ship and is used to move.
####Enemy:
Creates the enemy.
####Missile:
Creates the basic framework of the missile.
####Shorty:
Creates the killer missile.Inherits from missile class.
####Longy:
Creates the freezing missile.Inherits from missile class.
__________________

How To Play:
------------------
>- Run the following code to start the game.
```
python3 run.py
```
>- 'a,d' use these controls for left and right.
>- use 's' to shoot killer missile.
>- use 'space' to shoot freezing missile
>- press 'q' to quit.

___________________

Reqiurements:
--------------------
- Python3

For mac:
```
brew cask update
sudo brew cask install python3
```
For Linux:
```
sudo apt-get update
sudo apt-get install python3
sudo pip3 install pygame
```

_______________

###Pulkit Gera
####20171035
