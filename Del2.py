import turtle
from enum import Enum
def main():
    running = True
    flagDictionary = {"norge" : Norway, "sverige" : Sweden, "danmark" : Denmark}
    while running:
        print("skriv en flagga du vill ska ritas")
        print("just nu finns bara Sverige, Norge, Danmark")
        userInput = input().lower()
        try:
            DrawFlag(flagDictionary[userInput]) #detta är ett lättare sätt en att ha massa if statements baserat på vad man skrev in
        except:
            print("Något gick fel, det du skrev : ", userInput)

def DrawFlag(flag):
    MaxFlagSize = [150 * flag.flagRatio, 150] #alla flaggor är inte kuber så någon av x och y behöver ändras av ration, så den kan bli mindre lika eller större än den andra
    gridSize = [MaxFlagSize[0] / flag.flagWidth, MaxFlagSize[1] / flag.flagHeight]
    turtle.getscreen()
    Cursor = turtle.Turtle()
    Cursor.speed(100) #blir lite snabbare
    startPosition = [-MaxFlagSize[0] / 2, -MaxFlagSize[1] / 2] # så den ritas runt mitten som anchor
    for y in range(flag.flagHeight):
        for x in range(flag.flagWidth):
            color = flag.flagColorDictionary[flag.flagArray2D[y][x]].value
            FillCube(Cursor, gridSize[0] , gridSize[1], startPosition[0] + x * gridSize[0], startPosition[1] +y * gridSize[1], color) 
            #gridsize[0] = height, gridsize[1] = width, startPosition + x * gridSize för att sätta offsetten

def FillCube(cursor ,Height, Width, StartX, StartY, Color):
    CursorGoToPositionWithoutDraw(cursor, StartX, StartY)
    cursor.color(Color)
    cursor.begin_fill()
    cursor.fd(Width) #finns säkert något bättre sätt än att skriva detta om 4 gånger
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
class Color(Enum): #https://cs111.wellesley.edu/labs/lab02/colors alla färger
    #anledningen varför jag har enums är för att det är lättare när man skapar flaggan att bara skriva color. sen välja färgen man vill ha
    Yellow = "Yellow"
    Blue = "Blue" 
    Red = "Red"
    White = "White"
    DarkBlue = "blue4"

class Sweden():
    #anledningen varför jag använder en 2d array är för att man ska kunna skapa mer flaggor som inte behöver vara samma form, där index är färgerna
    #det skulle kunna gå att senare göra något bättre sätt att skapa dessa 2d arrays t.ex att lägga in bilder som den läser från
    flagArray2D = [ 
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1]]
    flagColorDictionary = {1 : Color.Blue, 2 : Color.Yellow} 
    flagWidth =  len(flagArray2D[0]) #skulle skapa problem ifall det inte finns någon [0]
    flagHeight = len(flagArray2D)
    flagRatio = flagWidth / flagHeight

class Denmark():
    flagArray2D = [
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,2,1,1,1,1,1,1,1,1,1]]
    flagColorDictionary = {1 : Color.Red, 2 : Color.White}
    flagWidth =  len(flagArray2D[0])
    flagHeight = len(flagArray2D)
    flagRatio = flagWidth / flagHeight

class Norway():
    flagArray2D = [
        [1,1,1,3,2,3,1,1,1,1,1,1,1,1],
        [1,1,1,3,2,3,1,1,1,1,1,1,1,1],
        [3,3,3,3,2,3,3,3,3,3,3,3,3,3],
        [2,2,2,2,2,2,2,2,2,2,2,2,2,2],
        [3,3,3,3,2,3,3,3,3,3,3,3,3,3],
        [1,1,1,3,2,3,1,1,1,1,1,1,1,1],
        [1,1,1,3,2,3,1,1,1,1,1,1,1,1]]
    flagColorDictionary = {1 : Color.Red, 2 : Color.Blue, 3 : Color.White}
    flagWidth =  len(flagArray2D[0])
    flagHeight = len(flagArray2D)
    flagRatio = flagWidth / flagHeight





main()