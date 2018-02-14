###Initiate Everything
from "Classes.py" import *
print(welcome)
#A Goblin
goblin = Enemy("Goblin", 20, 7)
#A Spider
spider = Enemy("Spider", 10, 5)
#A Zombie
zombie = Enemy("Zombie", 15, 9)

#Initiate the Player
Name = input("Please enter the name of your character:")
startingInventory = []
joe = Player(Name, 50, 1, startingInventory)
