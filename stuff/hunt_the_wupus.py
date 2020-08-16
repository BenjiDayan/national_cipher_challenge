#Hunt the Wumpus - simple linear text based game

from random import choice

caves = range(1, 21)
wumpusLocation = choice(caves)
playerLocation = choice(caves)
while playerLocation == wumpusLocation:
    playerLocation = choice(caves)

print("Welcome to Hunt the Wumpus!")
print("You can see", len(caves), "caves before you")
print("To move to a cave simply type it's number")

while True:
    print("Your current location is cave", playerLocation)
    if (playerLocation == wumpusLocation + 1 or
        playerLocation == wumpusLocation - 1):
        print ("You think you smell a wumpus")

    playerLocation = int(input("Which cave do you want to move to?"))
    while not type(playerLocation) == int or not playerLocation in caves:
        playerLocation = int(input("Please type a number from 1 to", len(caves)))

    if playerLocation == wumpusLocation:
        print("The wumpus ate you!")
        break
    
        
