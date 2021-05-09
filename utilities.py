import math

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

WIDTH=800

#global variable that keeps track of the total number of rows
TOTAL_ROWS=40

def h(p1, p2):
    x1= p1[0]
    y1=p1[1]
    x2=p2[0]
    y2=p2[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)