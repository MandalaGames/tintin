from genetics import *

grid.writeOut(DATA_DIR, "turn0.txt")

for turn in range(1, NUM_TURNS):
    print("executing turn " + str(turn))
    for gameobject in grid.gameObjects:
        gameobject.doTurn()
    print("writing out game grid " + str(turn))
    grid.writeOut(DATA_DIR, "turn" + str(turn) + ".txt")
    print("num Trees = " + str(grid.getCount("Tree")))
    print("num Factories = " + str(grid.getCount("Factory")))
    print("co2 = " + str(grid.environment.co2))
