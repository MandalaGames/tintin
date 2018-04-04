class Grid(object):
    def __init__(self, size):
        self.grid = []
        # Set up empty grid:
        for i in range(size):
            line = []
            for j in range(size):
                line.append(" ")
            self.grid.append(line)

    def get(self, x, y):
        return self.grid[y][x]

    def getNorth(self, x, y):
        try:
            return self.grid[y-1][x]
        except IndexError:
            return ""

    def getSouth(self, x, y):
        try:
            return self.grid[y+1][x]
        except IndexError:
            return ""

    def getEast(self, x, y):
        try:
            return self.grid[y][x+1]
        except IndexError:
            return ""

    def getWest(self, x, y):
        try:
            return self.grid[y][x-1]
        except IndexError:
            return ""

    def set(self, x, y, value):
        self.grid[y][x] = value
