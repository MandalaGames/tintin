import random 
import os
import json 
import gameobjects
import Grid
from DataProcessors import CsvReader 
import Environment

GRID_SIZE = 1000
NUM_NINJAS = 800
NUM_TREES = 20000
NUM_OLDMEN = 100
NUM_VILLAGERS = 800
NUM_TURNS = 100
DATA_DIR = "grids"

#print("making elevationGrid")
#elevationGrid = CsvReader.CsvReader("elev/data/fuji_1000.csv", [int,int,int], maxSize=1000).getGrid()
#print("writing elevationGrid to json")
#with open("elev/data/fuji_1000.json", 'w') as f:
    #f.write(json.dumps(elevationGrid))
#print("exiting")
#exit()

print("loading elevationGrid")
with open("elev/data/fuji_1000.json") as f:
    elevationGrid = json.loads(f.read())
print("elevationGrid size = " + str(len(elevationGrid)) + "x" + str(len(elevationGrid[0])))

print("making game grid")
grid = Grid.Grid(GRID_SIZE, GRID_SIZE, elevationGrid)
grid.environment = Environment.Environment()
print("made game grid")

# Initialize grid:
def placeObjects(number, gameobjectClass, grid):
    for i in range(number):
        square = " "
        x_pos = 0
        y_pos = 0
        while square == " ":
            x_pos = random.randint(0, GRID_SIZE-1)
            y_pos = random.randint(0, GRID_SIZE-1)
            square = grid.getSymbol(x_pos, y_pos)
            if(square == " "):
                gameobject = gameobjectClass(grid)
                square = gameobject.symbol
                gameobject.x = x_pos
                gameobject.y = y_pos
                #addGameObject(gameobject, gameObjects, objectClasses)
                grid.addGameobject(gameobject)
                
            #print ("tree num = " + str(i) + " square =  " + square + " x_pos = " + str(x_pos)  + " y_pos = " + str(y_pos))

placeObjects(NUM_TREES, gameobjects.Tree, grid)
placeObjects(NUM_OLDMEN, gameobjects.OldMan, grid)
placeObjects(NUM_NINJAS, gameobjects.Ninja, grid)
placeObjects(NUM_VILLAGERS, gameobjects.Villager, grid)
