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

def getTotalMoney(people):
    total = sum(person.money for person in people)
    return total

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
    return offsetX, offsetY

def getRect():
    position = x,y = 0,0
    size = w,h = 32,32
    colour = 0,0,0
    rect = pygame.Rect(position, size)
    image = pygame.Surface(size)
    image.fill(colour)
    return rect, image

def doRect():
    rect, image = getRect()
    screen.blit(image, rect)

villagers = grid.getClass("Villager")
ninjas = grid.getClass("Ninja")
oldmen = grid.getClass("OldMan")

while True:
    clock.tick(50)

    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # Clear the screen
    screen.fill((50, 200, 50))

    s = pygame.display.get_surface()
    #rect = pygame.Rect(topleft = (0,0), size=(GRID_SIZE,GRID_SIZE))
    #s.fill(Color("red"), rect)

    # Check input
    offsetX, offsetY = getInput(offsetX, offsetY)
    # Move objects ...
    # Draw objects ...
    for gameobject in grid.gameObjects:
        gameobject.doTurn()
        if inWindow(gameobject, offsetX, offsetY):
            draw(gameobject, offsetX, offsetY)

    #doRect()

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
