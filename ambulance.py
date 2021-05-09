from aStar import *
from tkinter import *
from tkinter import messagebox

import random

# set the dimensions of the grid
WIN = pygame.display.set_mode((WIDTH, WIDTH))
# set the window title
pygame.display.set_caption(
    "Ambulance Routefinding Simulator (Created in PyGame)")


# returns an estimate of the distance between two points in space
# will be using euclidean distance

def makeGrid(rows, width):
    grid = []
    # gap is basically the width of a node
    gap = width//rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node((i, j), gap)
            grid[i].append(node)

    return grid


def drawGrid(win, rows, width):
    gap = width//rows
    for i in range(rows):
        pygame.draw.line(win, WHITE, (0, i*gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, WHITE, (j*gap, 0), (j*gap, width))


def drawRoutePlanner(win, grid, rows, width):
    win.fill(BLACK)
    for row in grid:
        for node in row:
            node.drawNodeOnScreen(win)
    drawGrid(win, rows, width)
    pygame.display.update()


def getClickedPosition(position, rows, width):
    gap = width//rows
    y, x = position
    row = y//gap
    col = x//gap

    return (row, col)


def main(win, width):
    ROWS = 40
    grid = makeGrid(ROWS, width)
    startPosition, endPosition = None, None
    run = True
    started = False

    # generating a random maze
    for row in grid:
        for node in row:
            if random.randint(0, 100) % 3 == 0:
                node.makeNodeBarrier()

    while run:
        drawRoutePlanner(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            # this condition checks whether the algorithm has started running
            # if yes, then it shouldn't be affected by other events
            if started:
                continue

            # 0th index means left mouse button
            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                coordinates = getClickedPosition(position, ROWS, width)
                node = grid[coordinates[0]][coordinates[1]]
                if not startPosition and node != endPosition:
                    startPosition = node
                    startPosition.makeNodeStart()
                elif not endPosition and node != startPosition:
                    endPosition = node
                    endPosition.makeNodeEnd()
                # elif node!=endPosition and node!=startPosition:
                #     node.makeNodeBarrier()

            # 2nd index means right mouse button
            elif pygame.mouse.get_pressed()[2]:
                position = pygame.mouse.get_pos()
                coordinates = getClickedPosition(position, ROWS, width)
                node = grid[coordinates[0]][coordinates[1]]

                if node.isStartNode():
                    startPosition = None
                elif node.isEndNode():
                    endPosition = None
                node.resetNode()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and started == False:
                    for row in grid:
                        for node in row:
                            node.updateNodeNeighbors(grid)
                    return aStarAlgorithm(lambda: drawRoutePlanner(win, grid, ROWS, width), grid, startPosition, endPosition)

    pygame.quit()


if __name__ == "__main__":
    while True:
        msg = ""
        if main(WIN, WIDTH) == False:
            msg = "No path found! Continue?"
        else:
            msg = "Path found! Continue?"
        Tk().wm_withdraw()  # to hide the main window
        if messagebox.askquestion('Continue?', msg) != "yes":
            exit()
        else:
            Tk().destroy()
