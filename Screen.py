import pygame

class Screen(object):
    def __init__(self, widthSquares, heightSquares, pixelsPerSquare):

        self.width_squares = widthSquares
        self.height_squares  = heightSquares
        self.width_pixels  = widthSquares * pixelsPerSquare
        self.height_pixels   = heightSquares * pixelsPerSquare
        self.pygameScreen = pygame.display.set_mode((self.width_pixels, self.height_pixels))
        self.pixelsPerSquare = pixelsPerSquare

    def inWindow(self, gameobject, offsetX, offsetY): 
        return gameobject.x * self.pixelsPerSquare - offsetX < self.width_pixels and gameobject.y * self.pixelsPerSquare - offsetY < self.height_pixels

    def draw(self, gameobject, image, offsetX, offsetY):
        imagerect = image.get_rect(topleft = (gameobject.x * self.pixelsPerSquare  - offsetX, gameobject.y * self.pixelsPerSquare  - offsetY))
        self.pygameScreen.blit(image, imagerect)

    def setOffset(self, offsetX, offsetY):
        self.offsetX = offsetX
        self.offsetY = offsetY


    def getScreenTopLeft(self, gridX, gridY):
        pass

    def drawSquare(grid, x, y):
        pass

    def getRect(self, x, y, w, h, color):
        position = x,y
        size = w,h
        #colour = 0,0,0
        rect = pygame.Rect(position, size)
        image = pygame.Surface(size)
        image.fill(color)
        return rect, image

    def drawRect(self, x, y, w, h, color):
        rect, image = self.getRect(x, y, w, h, color)
        self.pygameScreen.blit(image, rect)


    # NOTE: screenSizeX and screenSizeY are in Squares, not pixels.
    def drawGrid(self, grid, offsetX, offsetY):
        # Clear the screen
        self.pygameScreen.fill((50, 200, 50))
        #self.doRect()
        #offsetScreenX = offsetX * self.pixelsPerSquare
        #offsetScreenY = offsetY * self.pixelsPerSquare

        for y,row in enumerate(grid.grid[offsetY:offsetY + grid.ysize]): # TODO FIXME double check
            for x,square in enumerate(row[offsetX:offsetX + grid.xsize]):

                color = (square.color.r, square.color.g, square.color.b)
                self.drawRect((x - offsetX) * self.pixelsPerSquare, (y - offsetY) * self.pixelsPerSquare, self.pixelsPerSquare, self.pixelsPerSquare, color)

    

