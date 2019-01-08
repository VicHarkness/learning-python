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

#help
def gethelp():
    print(
        "Help:\n"
        "x indicates the player position, empty cells can be visited, - is inaccessible\n"
        "To move type go <direction>, e.g. go south\n"
        "To see what's in your current location, type look around\n"
        "To get information on an item type look at <item>, e.g. look at fridge\n"
    )

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
                    "location": row[5],
                    "status": row[6]
                    }
    return (items)

#check what items are in current room
def lookaround(currentroom, items):
    for row in items:
        if (currentroom in items[row]["location"]) and ((items[row]["uses"] == "3") or (items[row]["uses"] == "1")):
            print(items[row]["name"])

#looks at item, checks that item is in current room or in inventory
#checks to see if item has locked/unlocked status, outputs
def lookat(action, items, currentroom):
    lookingat=action[8:].capitalize()
    print(lookingat)
    for row in items:
        if (lookingat == items[row]["name"]) and ((currentroom in items[row]["location"].casefold()) or ("1" in items[row]["owned"])):
            print(items[lookingat]["description"])
            if items[lookingat]["status"] != "0":
                print("It is currently %s." %items[row]["status"])

#check inventory
def checkinv(items):
    print("You have:")
    for row in items:
        if "1" in items[row]["owned"]:
            print(items[row]["name"])    

#take item (if possible)
def takeitem(action, items, currentroom):
    print("You took %s" %action[5:])
    takingitem=action[5:]
    for row in items:
        if (takingitem in items[row]["name"].casefold()) and (items[row]["owned"] == "0") and (items[row]["takeable"] == "1") and (currentroom in items[row]["location"]):
            items[row]["owned"]="1"
            items[row]["location"]="inventory"
    return(items)

#use item 
def useitem(action, items, currentroom):
    useitem, targetitem=action.split(" on ")
    useitem=useitem[4:]
    useitem=useitem.capitalize()
    targetitem=targetitem.capitalize()
    #check if items can be used
    if items[useitem]["uses"] != "3":
        print("%s cannot be used" %useitem)
    elif items[useitem]["owned"] == "0":
        print("You do not own %s" %useitem)
    elif items[targetitem]["location"] != currentroom:
        print("Cannot find target item")
    elif items[targetitem]["uses"] != "3":
        print("%s cannot be used on %s" %(useitem,targetitem))
    #unlocking specific cases
    elif useitem=="Safe key" and targetitem=="Safe":
        print("You have unlocked the safe")
        items["Safe"]["status"]="unlocked"
    elif useitem=="Hands" and targetitem=="Safe" and items["Safe"]["status"]=="unlocked":
        print("You open the safe and find a door key")
        items["Door key"]["uses"]="3"
        items["Door key"]["location"]="bedroom" 
    elif useitem=="Door key" and targetitem=="Front door":
        print("Congratulations, you have found the key and escaped the extra spooky house")
    #other uses
    else:
        print("Nothing happens")

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
    if action.startswith("look at") == True:
        print("Looking at")
        lookat(action, items, currentroom)
    if action == "help":
        gethelp() 
    if action == "inventory":
        checkinv(items)
    if action.startswith("take") == True:
        items=takeitem(action, items, currentroom)
    if action.startswith("use") == True:
        useitem(action, items, currentroom)
    if action == "exit":
        return(False)
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
items = getitems(items)
while True:
    redraw(playerx, playery)
    playerx, playery, currentroom=houselayout(playerx, playery, currentroom)
    playerx, playery, playeroldx, playeroldy, items, currentroom = getaction(playerx, playery, playeroldx, playeroldy, items, currentroom)


