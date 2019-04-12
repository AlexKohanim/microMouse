#!/usr/bin/env python3

"""
    Positions for bot: "North" "South" "East" "West"
    4 startting potiential goals, center + North, center + East...
    3 x 3 sub cells, to move from positions, move 2 cells ignore corners

"""

import random


class mapMaze:
    """ Micro mouse Maze solver? """

    def __init__(self, x_init=0, y_init=0, width=31, height=31):
        self.x = x_init
        self.y = y_init
        self.width = width
        self.height = height
        self.matrix = [[0 for _ in range(height)] for __ in range(width)]
        floodfill(0, width//2, height //2)
        

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

    def floodfill(self, distance, matrix, x, y, dx, dy):
        """ Source: https://stackoverflow.com/a/19840816 
            matrix contains integer values
            initial matrix is filled with goal posts and 1's
        """
        # if at a wall, don't invoke
        if matrix[x][y] >= 0:
            matrix[x][y] = distance
            # recursively invoke flood fill on all surrounding cells:
            if x > 0:
                floodfill(matrix, x + dx, y)
            if x < len(matrix[y]) - 1:
                floodfill(matrix, x - dx, y)
            if y > 0:
                floodfill(matrix, x, y- dy)
            if y < len(matrix) - 1:
                floodfill(matrix, x, y+ dy)
        return matrix

    def checkForWall(self, x=self.x, y=self.y):
        offSets = {"North" : (1, 1), "South": (-1, -1), "West": (1, -1), "East": (-1, 1)} 
        if self.x < width:
            if invokeRightSensor():
                self.matrix[x+1][y] = "wall"
                self.matrix = floodfill(self.matrix, x + 1, x)
            else:
                self.matrix[x+1][y] = "open"
        if self.x > 0:
            if invokeLeftSensor():
                self.matrix[x-1][y] = "wall"
                self.matrix = floodfill(self.matrix, x - 1, y)
            else:
                self.matrix[x-1][y] = "open"
        if self.y < height:
            if invokeForwardSensor():
                self.matrix[x][y+1] = "wall"
                self.matrix = floodfill(self.matrix, x, y + 1)
            else:
                self.matrix[x][y+1] = "open"
