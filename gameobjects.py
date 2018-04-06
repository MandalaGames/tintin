import random
import Grid

class Direction(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class GameObject(object):
    def __init__(self,grid):
        self.grid = grid
        self.symbol = ""
        self.x = 0
        self.y = 0

    def move(self, dx, dy):
        try:
            self.grid.grid[self.y][self.x].clear()
        except IndexError: # NOTE  offscreen
            pass
        self.x += dx
        self.y += dy
        try:
            self.grid.grid[self.y][self.x].gameobject = self 
        except IndexError: # NOTE go offscreen
            pass

    def moveForward(self, amount):
        self.move(self.direction.x * amount, self.direction.y * amount)

    # Return symbol of object dx, dy away from us FIXME not used?
    def check(self, dx, dy):
        return self.grid.grid[self.y + dy][self.x + dx].gameobject.symbol

    def getInFront(self):
        try:
            return self.grid.grid[self.y + self.direction.y][self.x + self.direction.x].gameobject
        except IndexError: # NOTE at the edge of screen
            return None
        except AttributeError: # NOTE at the edge of screen
            return None

    # Change symbol of object dx, dy away from us
    def change(self, dx, dy, symbol):
        self.grid.grid[self.y + dy][self.x + dx].gameobject.symbol = symbol

    # Check symbol of object in front of us
    def checkInFront(self):
        try:
            return self.getInFront().symbol
        except IndexError: # NOTE at the edge of screen
            return " "
        except AttributeError: # NOTE at the edge of screen
            return " "

    # Change symbol of object in front of us
    def changeInFront(self, symbol):
        try:
            self.grid.grid[self.y + self.direction.y][self.x + self.direction.x].gameobject.symbol = symbol
        except AttributeError: # NOTE at the edge of screen
            pass

    def placeInFront(self, gameobject):
        try:
            gameobject.x = self.x + self.direction.x
            gameobject.y = self.y + self.direction.y
            #self.grid.grid[self.y + self.direction.y][self.x + self.direction.x].gameobject = gameobject
            self.grid.addGameobject(gameobject)
        except AttributeError: # NOTE at the edge of screen
            pass
         
    def doTurn(self):
        pass 

class Person(GameObject):
    def __init__(self, grid):
        super(Person, self).__init__(grid)
        self.symbol = "p"

        self.cardinalDirection = ['n','s','e','w'][random.randint(0,3)]

        if(self.cardinalDirection == 'n'):
            self.direction = Direction(0, -1)
        if(self.cardinalDirection == 's'):
            self.direction = Direction(0, 1)
        if(self.cardinalDirection == 'e'):
            self.direction = Direction(1, 0)
        if(self.cardinalDirection == 'w'):
            self.direction = Direction(-1, 0)
        
        #self.symbol = self.cardinalDirection
    
class Ninja(Person):
    def __init__(self, grid):
        super(Ninja, self).__init__(grid)
        self.symbol = "n"
        self.wood = 0
        self.tomatoes = 0
        self.money = random.randint(0,10)
	self.sprite = "ninja.png"
    def rob(self, person):
        amount = random.randint(0, self.money)
        person.money -= amount
        self.money += amount

    def doTurn(self):
        if self.checkInFront() == 't':
            if self.wood < 6:
                deadTree = DeadTree(self.grid)
                self.placeInFront(deadTree)
                self.wood += 1
            else:
                factory = Factory(self.grid)
                self.placeInFront(factory)
                self.wood = 0 

        elif self.checkInFront() == 'x' or self.checkInFront() == 'F':
            self.moveForward(2)
        elif self.checkInFront() == 'o' or self.checkInFront() == 'v':
            oldman = self.getInFront()
            self.rob(oldman)
            self.moveForward(2)
        else:
            self.moveForward(1)

class Villager(Person):
    def __init__(self, grid):
        super(Villager, self).__init__(grid)
        self.symbol = "v"
        self.wood = 0
        self.tomatoes = 0
        self.money = random.randint(0,10)
	self.sprite = "villager.png"
    def doTurn(self):
        if self.checkInFront() == 't':
            deadTree = DeadTree(self.grid)
            self.placeInFront(deadTree)
            self.wood += 1

        elif self.checkInFront() == 'x' or self.checkInFront() == 'F':
            self.moveForward(2)
        else:
            self.moveForward(1)

class OldMan(Villager):
    def __init__(self, grid):
        super(OldMan, self).__init__(grid)
        self.symbol = "o"
        self.wood = 0
        self.tomatoes = random.randint(2,5)
        self.money = random.randint(5,10)
	self.sprite = "old man.png"
        self.turnCounter = 0
        self.gardenerSkill = random.randint(50,100) # FIXME: high skill means plant less trees

    def plantTree(self, x, y):
        tree = Tree(self.grid)
        tree.x = x
        tree.y = y
        self.grid.addGameobject(tree)
        tree.symbol = "T" #FIXME remove
        print("planted tree") # FIXME remove

    def doTurn(self):
        self.turnCounter  += 1
        if self.turnCounter % 2 == 0:
            if self.checkInFront() == 't' or self.checkInFront() == 'x' or self.checkInFront() == 'F':
                self.moveForward(2)
            else:
                self.moveForward(1)
        if self.turnCounter % self.gardenerSkill == 0:
            x = self.x
            y = self.y
            self.moveForward(1)
            self.plantTree(x, y)
            self.turnCounter = 0

class Factory(GameObject):
    def __init__(self, grid):
        super(Factory, self).__init__(grid)
        self.symbol = "F"
        self.turnCounter  = 0
	self.sprite = "factory.png"
        self.money = 0
    def doTurn(self):
        self.turnCounter  += 1
        if self.turnCounter % 5 == 0:
            self.releaseSmog()
            self.turnCounter = 0
            self.money += 1
    def releaseSmog(self):
        self.grid.environment.co2 += 50

class House(GameObject):
    def __init__(self, grid):
        super(Factory, self).__init__(grid)
        self.symbol = "H"
        self.sprite = ""

class Tree(GameObject):
    def __init__(self, grid):
        super(Tree, self).__init__(grid)
        self.symbol = "t"
	self.sprite = "tree.png"
    def doTurn(self):
        self.grid.environment.co2 -= 1

class DeadTree(GameObject):
    def __init__(self, grid):
        super(DeadTree, self).__init__(grid)
        self.symbol = "x"
	self.sprite = "dead tree.png"
