#initialise grid
grid=[["-"," ","-"],[" "," "," "],[" "," "," "],["-"," ","-"]]

#player start position
playerx=int(0)
playery=int(1)

#items
#0 if owned, 1 if not owned
key=int(0)
towel=int(0)

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
def nogo():
    print("You cannot go that way")

#check movement would not take player off edge of map
def boundscheck(playerx, playery):
    if playerx < 0:
        nogo()
        playerx=0
    if playerx > 2:
        nogo()
        playerx=2
    if playery < 0:
        nogo()
        playery=0
    if playery > 2:
        nogo()
        playery=2
    #if playerx == 0 and playery=0:
    #    nogo()

#get action from user text input
def getaction(playerx, playery):
    action=input("What do you want to do? ")
    if action == "help":
        print("Directions are: north, east, south, west.  \nCommands are take item, use item.")
    if action == "go north":
        clearold()
        playerx -= 1
        boundscheck(playerx, playery)
    if action == "go south":
        clearold()
        playerx += 1
        boundscheck(playerx, playery)
    if action == "go east":
        clearold()
        playery += 1
        boundscheck(playerx, playery)
    if action == "go west":
        clearold()
        playery -= 1
        boundscheck(playerx, playery)
    return (playerx, playery)

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
while True:
    redraw(playerx, playery)
    houselayout(playerx, playery)
    playerx, playery = getaction(playerx, playery)


