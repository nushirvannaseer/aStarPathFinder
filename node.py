
import pygame
from utilities import *


class Node:
    def __init__(self, coordinates, width):
        # needs to know where it is in the grid
        # coordinates is basically a tuple
        self.coordinates = coordinates
        # needs to know what its width is
        self.width = width
        # needs to know the absolute position in the window
        # absoluteCoordinates[0]= row and absoluteCoordinates[1]=col
        self.absoluteCoordinates = (coordinates[0]*width, coordinates[1]*width)
        # needs to know what its neighbors
        self.color = BLACK
        self.neighbors = []

    def getCoordinates(self):
        return self.coordinates

    def isClosedNode(self):
        return self.color == RED

    def isOpenNode(self):
        return self.color == GREEN

    def isBarrierNode(self):
        return self.color == WHITE

    def isStartNode(self):
        return self.color == ORANGE

    def isEndNode(self):
        return self.color == TURQUOISE

    def resetNode(self):
        self.color = BLACK

    def makeNodeStart(self):
        self.color = ORANGE

    def makeNodeClosed(self):
        self.color = RED

    def makeNodeOpen(self):
        self.color = GREEN

    def makeNodeBarrier(self):
        self.color = WHITE

    def makeNodeEnd(self):
        self.color = TURQUOISE

    def makeNodePath(self):
        self.color = PURPLE

    def drawNodeOnScreen(self, win):
        pygame.draw.rect(
            win, self.color, (self.absoluteCoordinates[0], self.absoluteCoordinates[1], self.width, self.width))

    def updateNodeNeighbors(self, grid):
        self.neighbors = []
        if self.coordinates[0] < TOTAL_ROWS - 1 and not grid[self.coordinates[0]+1][self.coordinates[1]].isBarrierNode():  # down
            self.neighbors.append(
                grid[self.coordinates[0]+1][self.coordinates[1]])

        if self.coordinates[0] > 0 and not grid[self.coordinates[0]-1][self.coordinates[1]].isBarrierNode():  # up
            self.neighbors.append(
                grid[self.coordinates[0]-1][self.coordinates[1]])

        if self.coordinates[1] < TOTAL_ROWS - 1 and not grid[self.coordinates[0]][self.coordinates[1]+1].isBarrierNode():  # right
            self.neighbors.append(
                grid[self.coordinates[0]][self.coordinates[1]+1])

        if self.coordinates[1] > 0 and not grid[self.coordinates[0]][self.coordinates[1]-1].isBarrierNode():  # left
            self.neighbors.append(
                grid[self.coordinates[0]][self.coordinates[1]-1])

        # if self.coordinates[0] < TOTAL_ROWS -1 and self.coordinates[1]< TOTAL_ROWS-1 and not grid[self.coordinates[0]+1][self.coordinates[1]].isBarrierNode() and not grid[self.coordinates[0]][self.coordinates[1]+1].isBarrierNode():#down-right
        #     self.neighbors.append(grid[self.coordinates[0]+1][self.coordinates[1]+1])

        # if self.coordinates[0] < TOTAL_ROWS -1 and self.coordinates[1] >0 and not grid[self.coordinates[0]][self.coordinates[1]-1].isBarrierNode() and not grid[self.coordinates[0]+1][self.coordinates[1]].isBarrierNode():#down-left
        #     self.neighbors.append(grid[self.coordinates[0]+1][self.coordinates[1]-1])

        # if self.coordinates[0] >0 and not grid[self.coordinates[0]-1][self.coordinates[1]].isBarrierNode() and self.coordinates[1] < TOTAL_ROWS -1 and not grid[self.coordinates[0]][self.coordinates[1]+1].isBarrierNode():#up-right
        #     self.neighbors.append(grid[self.coordinates[0]-1][self.coordinates[1]+1])

        # if self.coordinates[0] >0 and not grid[self.coordinates[0]-1][self.coordinates[1]].isBarrierNode() and self.coordinates[1] >0 and not grid[self.coordinates[0]][self.coordinates[1]-1].isBarrierNode():#up-left
        #     self.neighbors.append(grid[self.coordinates[0]-1][self.coordinates[1]-1])

    # #__lt__ means less than. operator overloading
    # def __lt__(self, obj):
    #     return False
