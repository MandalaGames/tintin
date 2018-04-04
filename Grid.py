import os 

class Square(object):
    def __init__(self, elev, gameobject):
        self.elev = elev
        self.gameobject = gameobject 
    def getSymbol(self):
        if(self.gameobject != None):
            return self.gameobject.symbol
        else:
            return " "
    def clear(self):
        self.gameobject = None

class Grid(object):
    # data can be a size for a square grid with no elevation data, 
    # or a list of elevation data. 
    def __init__(self, xsize, ysize, elevData):
        self.initEmptyGrid(xsize, ysize)
        self.insertElevationData(elevData)
        self.gameObjects = []
        self.objectClasses = {}

    def initEmptyGrid(self, xsize, ysize):
        self.grid = []
        for i in range(xsize):
            line = []
            for j in range(ysize):
                line.append(Square(0, None))
            self.grid.append(line)

    def getCount(self, classname):
        try:
            return len(self.objectClasses[classname])
        except KeyError:
            return 0

    def placeGameobject(self, gameobject):
        oldGameobject = self.grid[gameobject.y][gameobject.x].gameobject 

        if oldGameobject != None:
            self.gameObjects.remove(oldGameobject)
            self.objectClasses[oldGameobject.__class__.__name__].remove(oldGameobject)

        self.grid[gameobject.y][gameobject.x].gameobject = gameobject
        # add to master list:
        self.gameObjects.append(gameobject)
        # add to class list: 
        try:
            self.objectClasses[gameobject.__class__.__name__].append(gameobject)
        except KeyError:
            self.objectClasses[gameobject.__class__.__name__] = [gameobject]

    def insertElevationData(self, elevationGrid):
        for row in elevationGrid:
            line = []
            x = row[0]
            y = row[1]
            z = row[2]
            try:
                self.grid[y][x].elev = z
            except IndexError:
                continue

    def getSymbol(self, x, y):
        if(self.grid[y][x].gameobject != None):
            return self.grid[y][x].gameobject.symbol
        else:
            return " "
    
    def getGameObject(self, x, y):
        return self.grid[y][x].gameobject

    def getNorth(self, x, y):
        try:
            return self.grid[y-1][x]
        except IndexError:
            return None

    def getSouth(self, x, y):
        try:
            return self.grid[y+1][x]
        except IndexError:
            return None

    def getEast(self, x, y):
        try:
            return self.grid[y][x+1]
        except IndexError:
            return None

    def getWest(self, x, y):
        try:
            return self.grid[y][x-1]
        except IndexError:
            return None

    def setGameobject(self, x, y, gameObject):
        self.grid[y][x].gameobject = gameObject

    def writeOut(self, dataDir, filename):
        text = ""
        for line in self.grid:
            for square in line:
                if square != None:
                    text += square.getSymbol()
                else:
                    text += " "
            text += "\n" 

        with open(os.path.join(dataDir, filename), 'w') as f:
            f.write(text)
