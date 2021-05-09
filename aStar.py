from queue import PriorityQueue as pq
from node import *


def aStarAlgorithm(draw, grid, start, end):
    count = 0
    openSet = pq()
    # the set that we're inserting is in the order fValue, count, i.e. when we inserted the node into the
    # queue, and finally, the node itself
    openSet.put((0, count, start))
    cameFrom = {}
    # initially, we set the gValue and fValue for each node to infinity
    gValue = {node: float('inf') for row in grid for node in row}
    fValue = {node: float('inf') for row in grid for node in row}
    # gValue of the start node will be 0
    gValue[start] = 0
    # fValue for the start node is calculated. Euclidean distance used
    fValue[start] = h(start.getCoordinates(), end.getCoordinates())

    # the priority queue does not tell us if we have an element in the queue
    # so we use a dictionary with it so we can track what nodes are present in it
    openSetHash = {start}

    while not openSet.empty():
        draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        # right now we just need the node wuth the lowest fValue
        current = openSet.get()[2]
        # also pop the same node from your dictionary
        openSetHash.remove(current)

        if current == end:
            # make the path and return True
            constructPath(cameFrom, end, draw)
            end.makeNodeEnd()
            start.makeNodeStart()
            return True

        # adding one because right now the eddges arent weigfhted
        tempGValue = gValue[current]+1
        for neighbor in current.neighbors:
            if tempGValue < gValue[neighbor]:
                cameFrom[neighbor] = current
                gValue[neighbor] = tempGValue
                fValue[neighbor] = tempGValue + \
                    h(neighbor.getCoordinates(), end.getCoordinates())
                if neighbor not in openSetHash:
                    count += 1
                    openSet.put((fValue[neighbor], count, neighbor))
                    openSetHash.add(neighbor)
                    neighbor.makeNodeOpen()

        if current != start:
            current.makeNodeClosed()

    return False


def constructPath(cameFrom, end, draw):
    while end in cameFrom:
        end = cameFrom[end]
        end.makeNodePath()
        draw()
