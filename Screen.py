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

    def getRect(self, x, y, w, h):
        position = x,y
        size = w,h
        rect = pygame.Rect(position, size)
        return rect

    def multiplyColor(self, r, g, b, multiplier):
        r = (r * multiplier / 1000) % 255
        g = (g * multiplier / 1000) % 255
        b = (b * multiplier / 1000) % 255
        print (r,g,b)
        return (r,g,b)


    def drawRect(self, x, y, w, h, color):
        rect = self.getRect(x, y, w, h)
        pygame.draw.rect(self.pygameScreen, color,(x,y,w,w))

    # NOTE: screenSizeX and screenSizeY are in Squares, not pixels.
    def drawGrid(self, grid, offsetX, offsetY):

        # Clear the screen
        #self.pygameScreen.fill((50, 200, 50))

        size = self.width_squares, self.height_squares

        offsetXSq = int( offsetX / self.pixelsPerSquare)
        offsetYSq = int( offsetY / self.pixelsPerSquare)

        offsetXPix = offsetX - self.pixelsPerSquare * offsetXSq
        offsetYPix = offsetY - self.pixelsPerSquare * offsetYSq

        print("offsetXPix, offsetYPix")
        print(offsetXPix, offsetYPix)
        x_range= offsetXSq, offsetXSq + self.width_squares
        y_range = offsetYSq, offsetYSq + self.height_squares
        for y in range(y_range[0], y_range[1]): # TODO FIXME double check
            row = grid.grid[y]
            for x in range(x_range[0], x_range[1]): # TODO FIXME double check
                square = row[x]
                color = self.multiplyColor(square.color.r, square.color.g, square.color.b, square.elev)
                self.drawRect((x - offsetXSq) * self.pixelsPerSquare - offsetXPix, (y - offsetYSq) * self.pixelsPerSquare - offsetYPix, self.pixelsPerSquare, self.pixelsPerSquare, color)
