import random

class Direction(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def random():
        cardinalDirection = ['n','s','e','w'][random.randint(0,3)]

        if(cardinalDirection == 'n'):
            direction = Direction(0, -1)
        if(cardinalDirection == 's'):
            direction = Direction(0, 1)
        if(cardinalDirection == 'e'):
            direction = Direction(1, 0)
        if(cardinalDirection == 'w'):
            direction = Direction(-1, 0)
        return direction
        
