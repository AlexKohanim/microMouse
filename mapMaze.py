#!/usr/bin/env python3

"""
    Positions for bot: "North" "South" "East" "West"
"""


class mapMaze:
    """ Micro mouse Maze solver? """

    def invokeLeftMotor(self, count):
        # invoke motor for turn, multiplier is count
        pass

    def invokeRightMotor(self, count):
        # invoke motor for turn, multiplier is count
        pass

    def setOrientation(self, orientation):
        self.orientation = orientation

    def getOrientation(self):
        return self.orientation

    def turnMouse(self, direction, count):
        if direction == "right":
            invokeLeftMotor(count)
        else:
            invokeRightMotor(count)

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
        orientation = getOrientation()
