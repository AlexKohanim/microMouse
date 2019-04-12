#!/usr/bin/env python3

"""
    Positions for bot: "North" "South" "East" "West"
"""

import random


class mapMaze:
    """ Micro mouse Maze solver? """

    def __init__(self, x_init=0, y_init=0, width=11, height=11):
        self.x = x_init
        self.y = y_init
        self.width = width
        self.height = height
        self.matrix = [["open" for _ in range(height)] for __ in range(width)]

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

    def floodfill(self, matrix, x, y):
        """ Source: https://stackoverflow.com/a/19840816 
            matrix contains values "open" "wall" and "connected"
            initial matrix is filled with "open"
        """
        # if at a wall, don't invoke
        if matrix[x][y] == "open":
            matrix[x][y] = "connected"
            # recursively invoke flood fill on all surrounding cells:
            if x > 0:
                floodfill(matrix, x-1, y)
            if x < len(matrix[y]) - 1:
                floodfill(matrix, x+1, y)
            if y > 0:
                floodfill(matrix, x, y-1)
            if y < len(matrix) - 1:
                floodfill(matrix, x, y+1)
        return matrix

    def checkForWall(self):
        if self.x < width:
            self.matrix[x+1][y] = "wall" if invokeRightSensor() else "open"
        if self.x > 0:
            self.matrix[x-1][y] = "wall" if invokeLeftSensor() else "open"
        if self.y < height:
            self.matrix[x][y+1] = "wall" if invokeForwardSensor() else "open"
