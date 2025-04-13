import turtle
from enum import Enum
def main():
    flagCanvasSize = [500, 500] 
    Screen = turtle.getscreen()
    Cursor = turtle.Turtle()
    for row in Sweden.flagArray2D:
        for index in row:
            color = Sweden.flagColorDictionary[index]
    turtle.done()








#classes
#https://docs.python.org/3/library/enum.html
class Color(Enum):
    Yellow = "Yellow"
    Blue = "Blue"
class BaseFlag:
    flagArray2D = None
    flagColorDictionary = None

class Sweden(BaseFlag):
    flagArray2D = [
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1]]
    flagColorDictionary = {1 : Color.Blue, 2 : Color.Yellow}
    
    





main()