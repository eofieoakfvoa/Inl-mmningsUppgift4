import turtle
from enum import Enum
def main():
    MaxFlagSize = [150 * Sweden.flagRatio, 150]
    print(MaxFlagSize)
    gridSize = [MaxFlagSize[0] / Sweden.flagWidth, MaxFlagSize[1] / Sweden.flagWidth]
    Screen = turtle.getscreen()
    Cursor = turtle.Turtle()
    Cursor.goto(-MaxFlagSize[0] / 2, MaxFlagSize[1] / 2)
    for row in Sweden.flagArray2D:
        for index in row:
            color = Sweden.flagColorDictionary[index].value
            FillCube(Cursor, gridSize[0], gridSize[1], 0, 0, color)
    turtle.done()

def FillCube(cursor ,Height, Width, StartX, StartY, Color):
    print(Color)
    cursor.fd(Width)
    cursor.rt(90)
    cursor.fd(Height)
    cursor.rt(90)
    cursor.fd(Width)
    cursor.rt(90)
    cursor.fd(Height)
    cursor.rt(90)





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