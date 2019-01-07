import csv

#initialise grid
grid=[["-"," ","-"],[" "," "," "],[" "," "," "],["-"," ","-"]]

#player start position
playerx=int(0)
playery=int(1)
playeroldx=int(0)
playeroldy=int(1)
items={}
currentroom=""

#read in items list
#0 if not owned, 1 if owned
#note: using dict literal
def getitems(items):
    with open('itemlist.csv', 'rt') as itemlist:
        itemreader=csv.reader(itemlist, delimiter=',')
        for row in itemreader:
            items[row[0]] = {
                    "name": row[0],
                    "takeable": row[1],
                    "owned": row[2],
                    "description": row[3],
                    "uses": row[4],
                    "location": row[5]
                    }
    return (items)

#check what items are in current room
def lookaround(currentroom, items):
    for row in items:
        if currentroom in items[row]["location"]:
            print(items[row]["name"])    

def lookat(action, items, currentroom):
    print(action[8:])
    for row in items:
        if (action[8:] in items[row]["name"]) and (currentroom in items[row]["location"]):
            print(items[row]["description"])    

#draws out the grid
def redraw(playerx, playery):
    grid[playerx][playery]="x"   
    for row in grid:
        print("[{}][{}][{}]".format(*row))
    return (playerx, playery)

#clears x from player previous location
def clearold():
    grid[playerx][playery]=" "

#inform player they cannot move that direction
def nogo(playerx, playery, playeroldx, playeroldy):
    print("You cannot go that way")
    playerx=playeroldx
    playery=playeroldy
    return(playerx, playery, playeroldx, playeroldy)

#check movement would not take player off edge of map
#call nogo() if they're going to go out of bounds
def boundscheck(playerx, playery, playeroldx, playeroldy):
    if playerx == 0 and playery == 0:
        playerx, playery, playeroldx, playeroldy = nogo(playerx, playery, playeroldx, playeroldy)  
    if playerx == 0 and playery == 2:
        playerx, playery, playeroldx, playeroldy = nogo(playerx, playery, playeroldx, playeroldy)  
    if playerx == 3 and playery == 0:
        playerx, playery, playeroldx, playeroldy = nogo(playerx, playery, playeroldx, playeroldy)  
    if playerx == 3 and playery == 2:
        playerx, playery, playeroldx, playeroldy = nogo(playerx, playery, playeroldx, playeroldy)  
    return (playerx, playery, playeroldx, playeroldy)
        
#get action from user text input
#call bounds checking
#update old position to current one if move successfull
def getaction(playerx, playery, playeroldx, playeroldy, items, currentroom):
    action=input("What do you want to do? ")
    if action == "help":
        print("Directions are: north, east, south, west.  \nCommands are take item, use item.")
    if action == "go north":
        clearold()
        playerx -= 1
        playerx, playery, playeroldx, playeroldy=boundscheck(playerx, playery, playeroldx, playeroldy)
        playeroldx, playeroldy=playerx, playery
    if action == "go south":
        clearold()
        playerx += 1
        playerx, playery, playeroldx, playeroldy=boundscheck(playerx, playery, playeroldx, playeroldy)
        playeroldx, playeroldy=playerx, playery
    if action == "go east":
        clearold()
        playery += 1
        playerx, playery, playeroldx, playeroldy=boundscheck(playerx, playery, playeroldx, playeroldy)
        playeroldx, playeroldy=playerx, playery
    if action == "go west":
        clearold()
        playery -= 1
        playerx, playery, playeroldx, playeroldy=boundscheck(playerx, playery, playeroldx, playeroldy)
        playeroldx, playeroldy=playerx, playery
    if action == "look around":
        lookaround(currentroom, items)
    #handling for look at item
    if action.startswith("look at") == True:
        print("looking at")
        lookat(action, items, currentroom)
    
    
    return (playerx, playery, playeroldx, playeroldy, items, currentroom)

#what the rooms are
def houselayout(playerx, playery, currentroom):
    if grid[playerx][playery] == grid[0][1]:
        print("You are in the entryway.")
        currentroom="entryway"
    if grid[playerx][playery] == grid[1][1]:
        print("You are in the hallway.")
        currentroom="hallway"
    if grid[playerx][playery] == grid[1][0]:
        print("You are in the living room.")
        currentroom="living room"
    if grid[playerx][playery] == grid[1][2]:
        print("You are in the kitchen.")
        currentroom="kitchen"
    if grid[playerx][playery] == grid[2][0]:
        print("You are in the bathroom.")
        currentroom="bathroom"
    if grid[playerx][playery] == grid[2][1]:
        print("You are in the hallway.")
        currentroom="hallway2"
    if grid[playerx][playery] == grid[2][2]:
        print("You are in the dining room.")
        currentroom="dining room"
    if grid[playerx][playery] == grid[3][1]:
        print("You are in the bedroom.")
        currentroom="bedroom"
    return(playerx, playery, currentroom)

#main loop
getitems(items)
while True:
    getitems(items)
    redraw(playerx, playery)
    playerx, playery, currentroom=houselayout(playerx, playery, currentroom)
    playerx, playery, playeroldx, playeroldy, items, currentroom = getaction(playerx, playery, playeroldx, playeroldy, items, currentroom)


