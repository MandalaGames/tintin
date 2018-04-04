import random 
import os
import gameobjects
import Grid

GRID_SIZE = 1000
NUM_NINJAS = 500
NUM_TREES = 10000
NUM_VILLAGERS = 800
NUM_TURNS = 10
DATA_DIR = "grids"


def writeOut(filename, gridInstance):
    text = ""
    for line in gridInstance.grid:
        for square in line:
            text += square
        text += "\n" 

    with open(os.path.join(DATA_DIR, filename), 'w') as f:
        f.write(text)

grid = Grid.Grid(GRID_SIZE)
gameObjects = []
objectClasses = {}

def addGameObject(gameobject, masterList, classListContainer):
    # add to master list:
    masterList.append(gameobject)
    # add to class list: 
    try:
        classListContainer[gameobject.__class__.__name__].append(gameobject)
    except KeyError:
        classListContainer[gameobject.__class__.__name__] = [gameobject]

# Initialize grid:
def placeObjects(number, gameobjectClass):
    for i in range(number):
        square = " "
        x_pos = 0
        y_pos = 0
        while square == " ":
            x_pos = random.randint(0, GRID_SIZE-1)
            y_pos = random.randint(0, GRID_SIZE-1)
            square = grid.get(x_pos, y_pos)
            if(square == " "):
                gameobject = gameobjectClass()
                square = gameobject.symbol
                gameobject.x = x_pos
                gameobject.y = y_pos
                addGameObject(gameobject, gameObjects, objectClasses)
                grid.set(x_pos, y_pos, square)
                
            #print ("tree num = " + str(i) + " square =  " + square + " x_pos = " + str(x_pos)  + " y_pos = " + str(y_pos))

placeObjects(NUM_TREES, gameobjects.Tree)
placeObjects(NUM_NINJAS, gameobjects.Ninja)

for ninja in objectClasses["Ninja"]:
    #print ("x = " + str(ninja.x))
    #print ("y = " + str(ninja.y))
    if grid.getNorth(ninja.x, ninja.y)  == "t":
        grid.set(ninja.x, ninja.y, "N")

writeOut("turn0.txt", grid)

#for turn in range(NUM_TURNS):

