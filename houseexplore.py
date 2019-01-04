import csv

#initialise grid
grid=[["-"," ","-"],[" "," "," "],[" "," "," "],["-"," ","-"]]

#player start position
playerx=int(0)
playery=int(1)
playeroldx=int(0)
playeroldy=int(1)
items={}

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
def lookaround(playerx, playery, items):
    for row in items:
        if "bedroom" in items[row]["location"]:
            print(items[row]["name"])    

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
def getaction(playerx, playery, playeroldx, playeroldy, items):
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
        lookaround(playerx, playery, items)
    return (playerx, playery, playeroldx, playeroldy)

#what the rooms are
def houselayout(playerx, playery):
    if grid[playerx][playery] == grid[0][1]:
        print("You are in the entryway.")
    if grid[playerx][playery] == grid[1][1]:
        print("You are in the hallway.")
    if grid[playerx][playery] == grid[1][0]:
        print("You are in the living room.")
    if grid[playerx][playery] == grid[1][2]:
        print("You are in the kitchen.")
    if grid[playerx][playery] == grid[2][0]:
        print("You are in the bathroom.")
    if grid[playerx][playery] == grid[2][1]:
        print("You are in the hallway.")
    if grid[playerx][playery] == grid[2][2]:
        print("You are in the dining room.")
    if grid[playerx][playery] == grid[3][1]:
        print("You are in the bedroom.")

#main loop
getitems()
while True:
    getitems(items)
    redraw(playerx, playery)
    houselayout(playerx, playery)
    playerx, playery, playeroldx, playeroldy, items = getaction(playerx, playery, playeroldx, playeroldy, items)


