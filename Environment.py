import Grid, Map

class Environment(object):
    def __init__(self):
        self.temp = 0
        self.co2 = 0

    def generateLake(self, numSquares, startX, startY, grid):
        x = startX
        y = startY
        squares = []
        
        existingSquare = grid.grid[y][x]

        direction = None

        for i in range(numSquares):
            lakeSquare = Grid.Lake(existingSquare.elev, existingSquare.gameobject)
            grid.setSquare(x, y,lakeSquare)
            lastDirection = direction
            while direction == lastDirection:
                direction = Map.Direction.random()
                x += direction.x
                y += direction.y
