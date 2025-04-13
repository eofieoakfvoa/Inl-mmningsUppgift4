import turtle
from enum import Enum
def main():
    print("skriv en flagga du vill ska ritas")
    
def DrawFlag(flag):
    MaxFlagSize = [150 * Sweden.flagRatio, 150]
    gridSize = [MaxFlagSize[0] / Sweden.flagWidth, MaxFlagSize[1] / Sweden.flagHeight]
    Screen = turtle.getscreen()
    Cursor = turtle.Turtle()
    Cursor.speed(50)
    startPosition = [-MaxFlagSize[0] / 2, -MaxFlagSize[1] / 2]
    for y in range(Sweden.flagHeight):
        for x in range(Sweden.flagWidth):
            color = Sweden.flagColorDictionary[Sweden.flagArray2D[y][x]].value
            FillCube(Cursor, gridSize[0], gridSize[1], startPosition[0] + x * gridSize[0], startPosition[1] +y * gridSize[1], color)
    turtle.done()
def FillCube(cursor ,Height, Width, StartX, StartY, Color):
    CursorGoToPositionWithoutDraw(cursor, StartX, StartY)
    cursor.color(Color)
    cursor.begin_fill()
    cursor.fd(Width)
    cursor.rt(90)
    cursor.fd(Height)
    cursor.rt(90)
    cursor.fd(Width)
    cursor.rt(90)
    cursor.fd(Height)
    cursor.rt(90)
    cursor.end_fill()
def CursorGoToPositionWithoutDraw(cursor, x, y):
    cursor.penup()
    cursor.goto(x, y)
    cursor.pendown()




#classes
#https://docs.python.org/3/library/enum.html
class Color(Enum):
    Yellow = "Yellow"
    Blue = "Blue"

class Sweden():
    flagArray2D = [
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1]]
    flagColorDictionary = {1 : Color.Blue, 2 : Color.Yellow}
    flagWidth =  len(flagArray2D[0])
    flagHeight = len(flagArray2D)
    flagRatio = flagWidth / flagHeight
    





main()