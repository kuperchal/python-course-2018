# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 00:45:07 2018

@author: User
"""
#создается базовый класс с обыкновенным зомби

class Zombie:
    def __init__(self, name, level, health=100):
        self.name = name
        self.level = level
        self.health = health
    def showzombie(self):
        bio = (self.name + " level: " + str(self.level) + " health: " + str(self.health) )
        print (bio)
        
    def level_up(self):
        self.level += 1
        
#подкласс - усиленный зомби
        
class MegaZombie(Zombie):
    def __init__(self, name, level, health, dangerability=10):
        Zombie.__init__(self, name, level, health)
        self.dangerability = dangerability
        
 #мегазомби имеет запас сил для нанесения удара, после удара его уровень уменьшается на еденицу 
      
    def usedanger(self):
        self.dangerability -= 1
    
    def showzombie(self):
        bio = (self.name + " level: " + str(self.level) + " health: " + str(self.health) + " dangerability: " + str(self.dangerability) )
        print (bio)
 #еще более усиленный зомби       

class BossZombie(MegaZombie):
    def __init__(self, name, level, health, dangerability, infection):
        MegaZombie.__init__(self, name, level, health, dangerability)
        self.infection = infection
        
 #помимо прочего обладает способностью заражения, при заражении человека уровень его способности заражать уменьшается на один, а так же уменьшается здоровье на 10

    def useinfection(self):
        self.infection -= 1
        self.health -= 10
    
    def showzombie(self):
        bio = (self.name + " level: " + str(self.level) + " health: " + str(self.health) + " dangerability: " + str(self.dangerability) + " infection: " + str(self.infection) )
        print (bio)
 
    
    
zombie1 = Zombie('Zombyak', 1)
zombie2 = MegaZombie('Zombiwe', 5, 500)
zombie3 = BossZombie('ZombieBoss', 10, 1000, 500, 100)
zombie1.showzombie()
zombie2.showzombie()
zombie2.usedanger()
zombie2.usedanger()
zombie2.showzombie()
zombie3.showzombie()
zombie3.useinfection()
zombie3.showzombie()
