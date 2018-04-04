# -*- coding: utf-8 -*-

import pygame
import os 
import sys
from environmentSimulator import *

GRID_SIZE = 20
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SPRITE_DIR = "sprites"

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("environment simulation :)")

clock = pygame.time.Clock()

imgDict = {}

def inWindow(gameobject, offsetX, offsetY):
    return gameobject.x * GRID_SIZE - offsetX < SCREEN_WIDTH and gameobject.y * GRID_SIZE - offsetY < SCREEN_HEIGHT

def getImage(spritename):
    try:
        return imgDict[spritename]
    except KeyError:
        imgDict[spritename] = pygame.image.load(os.path.join(SPRITE_DIR, spritename))
        return imgDict[spritename]

def draw(gameobject, offsetX, offsetY):
    myimage = getImage(gameobject.sprite) 
    imagerect = myimage.get_rect(topleft = (gameobject.x * GRID_SIZE - offsetX, gameobject.y * GRID_SIZE - offsetY))

    screen.blit(myimage, imagerect)

offsetX = 0
offsetY = 0
while True:
    clock.tick(50)

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Clear the screen
    screen.fill((50, 200, 50))

    # Check input
    # Move objects ...
    # Draw objects ...

    # Update the screen

    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[pygame.K_UP]:
        offsetY -= 10
    if keys[pygame.K_DOWN]:
        offsetY += 10
    if keys[pygame.K_LEFT]:
        offsetX -= 10
    if keys[pygame.K_RIGHT]:
        offsetX += 10

    for gameobject in grid.gameObjects:
        gameobject.doTurn()
        if inWindow(gameobject, offsetX, offsetY):
            draw(gameobject, offsetX, offsetY)
    pygame.display.flip()
    #print("writing out game grid " + str(turn))
    #grid.writeOut(DATA_DIR, "turn" + str(turn) + ".txt")
    print("num Trees = " + str(grid.getCount("Tree")))
    print("num Factories = " + str(grid.getCount("Factory")))
    print("co2 = " + str(grid.environment.co2))
