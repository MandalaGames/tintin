# -*- coding: utf-8 -*-

import pygame
import os 
import sys
from environmentSimulator import *
import Screen

SCREEN_PIXELS_PER_GRID_SQUARE = 20
WIDTH_SQUARES = 32 
HEIGHT_SQUARES = 24

SPRITE_DIR = "sprites"

pygame.init()

screen= Screen.Screen(WIDTH_SQUARES, HEIGHT_SQUARES, SCREEN_PIXELS_PER_GRID_SQUARE)

pygame.display.set_caption("environment simulation :)")

clock = pygame.time.Clock()

# TODO: move to Image class
imgDict = {}

def getImage(spritename):
    try:
        return imgDict[spritename]
    except KeyError:
        imgDict[spritename] = pygame.image.load(os.path.join(SPRITE_DIR, spritename))
        return imgDict[spritename]
# end TODO: move to Image class

# TODO: move
def getTotalMoney(people):
    total = sum(person.money for person in people)
    return total
# end TODO: move

offsetX = 0
offsetY = 0

def getInput(offsetX, offsetY):
    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP]:
        offsetY -= 10
    if keys[pygame.K_DOWN]:
        offsetY += 10
    if keys[pygame.K_LEFT]:
        offsetX -= 10
    if keys[pygame.K_RIGHT]:
        offsetX += 10
    if keys[pygame.K_p]:
        paused = True
    else :
        paused = False
    return offsetX, offsetY, paused


def paintElev():
    pass


def drawSquare(grid, screenXSquares, screenYSquares):
    pass

villagers = grid.getClass("Villager")
ninjas = grid.getClass("Ninja")
oldmen = grid.getClass("OldMan")

paused = False

while True:
    clock.tick(50)

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    screen.drawGrid(grid, offsetX, offsetY)#, screen.width_squares, screen.height_squares)

    # Check input
    offsetX, offsetY, paused = getInput(offsetX, offsetY)
    # Move objects ...
    # Draw objects ...
    if not paused:
        for gameobject in grid.gameObjects:
            gameobject.doTurn()
            if screen.inWindow(gameobject, offsetX, offsetY):
                image = getImage(gameobject.sprite) 

                screen.draw(gameobject, image, offsetX, offsetY)

    paintElev()

    # Update the screen

    pygame.display.flip()

    # Print debug messages:
    #print("writing out game grid " + str(turn))
    #grid.writeOut(DATA_DIR, "turn" + str(turn) + ".txt")
    print("num Trees = " + str(grid.getCount("Tree")))
    print("num Factories = " + str(grid.getCount("Factory")))
    print("co2 = " + str(grid.environment.co2))
    print("villager money= " + str(getTotalMoney(villagers))) 
    print("ninja money= " + str(getTotalMoney(ninjas))) 
    print("old man money= " + str(getTotalMoney(oldmen))) 
