###Defines classes for the player, enemies, items, etc.

class Enemy:
    'Base class for all enemies'
    #Is it alive
    alive = False
    #Its name
    Type = "None"
    #Health and damage
    health = 0
    damage = 0
    #If it's hp is zero or less kill it
    if self.health <= 0;
        self.alive = False
        print(self.Type + " is dead!")
    def __init__(self, Type, health, damage):
        self.damage = damage
        self.Type = Type
        self.health = health
        Enemy.alive = True
        Enemy.Type = Type
        Enemy.health = health
        Enemy.damage = damage
    def attack(self, target):
        #Attack the player
        print(self.Type + " Is attacking!")
        target.hp -= self.damage

class Player:
    'The Player'
    alive = True
    hp = 50
    dm = 1
    inventory = []
    #If it's hp is zero or less kill it
    if self.health <= 0;
        self.alive = False
        print("You're is dead!")
    def __init__(self, name, hp, dm, inventory):
        self.hp = hp
        self.dm = dm
        self.inventory = inventory
        Enemy.alive = True
        Enemy.hp = hp
        Enemy.dm = dm
        Enemy.inventory = inventory
    def attack(self, target):
        print("You attacked " + target.Type)
        target.health -= self.dm
        print(target.Type + "\'s HP is now "+str(target.health))
    def pickUp(self, inventory, item):
