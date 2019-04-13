#!/usr/bin/env python3

"""
    Positions for bot: "North" "South" "East" "West"
    4 startting potiential goals, center + North, center + East...
    3 x 3 sub cells, to move from positions, move 2 cells ignore corners

"""

import random
import sys
import pprint


class mapMaze:
    """ Micro mouse Maze solver? """

   
    def invokeLeftMotor(self, count):
        # invoke motor for turn, multiplier is count
        orientations = ["North", "West", "South", "East"]
        previosPosition = orientations.index(self.orientation)
        self.orientation = orientations[(previosPosition + count) % 4]
        pass

    def invokeRightMotor(self, count):
        # invoke motor for turn, multiplier is count
        orientations = ["North", "East", "South", "West"]
        previosPosition = orientations.index(self.orientation)
        self.orientation = orientations[(previosPosition + count) % 4]

    def setOrientation(self, orientation):
        self.orientation = orientation

    def getOrientation(self):
        return self.orientation

    def getMaze(self):
        return self.matrix

    def turnMouse(self, direction, count):
        """ Use this for Turning """
        if direction == "right":
            invokeLeftMotor(count)
        else:
            invokeRightMotor(count)

    def invokeLeftSensor(self):
        # check for 20 cm distance from object
        return True if random.randrange(0, 2) == 0 else False
        pass

    def invokeRightSensor(self):
        # check for 20 cm distance from object
        return True if random.randrange(0, 2) == 0 else False
        pass

    def invokeForwardSensor(self):
        # check for 20 cm distance from object
        return True if random.randrange(0, 2) == 0 else False
        pass

    def resetVisitedMatrix(self):
        self.visited = [[0 for _ in range(self.height)] for __ in range(self.width)]

    def resetFillQueue(self):
        self.fillQueue = []

    def checkSurrounding(self, x, y):
        """ return a list of tupes of cords that are valid """
        valid = []
        if x > 1 and self.matrix[x-1][y] >= 0 and self.visited[x-2][y] < 1:
            valid.append((x-2, y))
        if x < self.width - 2 and self.matrix[x+1][y] >= 0 and self.visited[x+2][y] < 1:
            valid.append((x+2, y))
            self.visited[x+2][y] = 1
        if y > 1 and self.matrix[x][y-1] >= 0 and self.visited[x][y-2] < 1:
            valid.append((x, y-2))
            self.visited[x][y-2] = 1
        if y < self.height - 2 and self.matrix[x][y+1] >= 0 and self.visited[x][y+2] < 1:
            valid.append((x, y+2))
            self.visited[x][y+2] = 1
        return valid

    def floodfill(self, distance, matrix, x, y, fillQueue=[]):
        """ Source: https://stackoverflow.com/a/19840816 
            matrix contains integer values
            initial matrix is filled with goal posts and 1's
        """

        #print(self.visited)
        self.visited[x][y] = 1
        # if not at a wall, invoke
        if self.matrix[x][y] >= 0:
            self.matrix[x][y] = distance
            fillQueue.append((x,y))

            toVisit = []

            for fq in fillQueue:
                toVisit.extend(self.checkSurrounding(*fq))
           
            #toVisit = [self.checkSurrounding(*fq) for fq in fillQueue ][0] # getting next layer
            for _ in range(len(fillQueue)): # updating current layer
                cords = fillQueue.pop(0)
                self.matrix[cords[0]][cords[1]] = distance
                self.visited[cords[0]][cords[1]] = 1

            if len(toVisit) > 0:
                first = toVisit[0]
                x_1, x_2 = first[0], first[1]
                self.floodfill(distance+1, self.matrix, x_1, x_2, toVisit)
                #self.floodfill(distance +1, self.matrix, *fillQueue.pop(0))
        #self.resetVisitedMatrix()
        return matrix

    def checkForWall(self, x, y):
        offSets = {"North" : (2, 2), "South": (-2, -2), "West": (2, -2), "East": (-2, 2)} 
        dx, dy = offSets[self.orientation]
        if self.x < self.width:
            if invokeRightSensor():
                self.matrix[x+(dx // abs(dx))][y]  = -1 # wall
                self.matrix = floodfill(self.matrix, x + dx, x)
                self.resetFillQueue()
            else:
                pass
        if self.x > 0:
            if invokeLeftSensor():
                self.matrix[x-(dx // abs(dx))][y] = -1
                self.matrix = floodfill(self.matrix, x - dx, y)
                self.resetFillQueue()
            else:
                pass
        if self.y < self.height:
            if invokeForwardSensor():
                self.matrix[x][y+(dy // abs(dy))] = -1
                self.matrix = floodfill(self.matrix, x, y + dy)
                self.resetFillQueue()
            else:
                pass


    def __init__(self, x_init=0, y_init=0, width=31, height=31):
        sys.setrecursionlimit(15000)
        self.x = x_init
        self.y = y_init
        self.width = width
        self.height = height
        self.matrix = [[0 for _ in range(height)] for __ in range(width)]
        self.resetVisitedMatrix()
        self.resetFillQueue()
        self.matrix = self.floodfill(1, self.matrix, width//2, height //2)
        self.resetFillQueue()
        self.orientation = "North"

def runMaze():
    maze = mapMaze()
    theMaze = maze.getMaze()
    #print(theMaze)
    [print( m ) for m in theMaze]

runMaze()
