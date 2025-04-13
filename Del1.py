import math

class BaseShape:
    def __init__(self):
        self._Area = None
        self.CalculateArea() # eftersom __Init__ kallas EFTER objektet redan existerar betyder att det som inheritar detta kommer redan att ha overridat CalculateArea()
        # och då kommer detta använda dens version. är ganska glad att jag kom på detta, dock betyder det att super() kommer behövas vara sist, och det kanske pånågot sätt kan skapa problem

    def CalculateArea(): #abstrakt även fast jag tror att python inte direkt har type safety och man nog inte skulle behöva att verifiera att den har CalculateArea() 
        print("ANVÄND INTE BASESHAPE KLASSEN!!!!! ifall du inte gjorde det vet jag inte hur du lyckades")

    def SetArea(self, newArea):
        if not self._IsValidNumber(newArea):
            return
        self._Area = newArea
    def GetArea(self):
        return self._Area
    
    def _IsValidNumber(self, Number):
        return isinstance(Number, (float, int))

class Rectangle(BaseShape):
    def __init__(self, base, height): # basically en constructor, gör mycket av vad en construktor gör men by defenition är inte en constructor där __new__ värkar vara mer som en construktor :p
        self.Base = base
        self.Height = height
        super().__init__() # super() gör så att BaseShapes __Init__ också kallas annars så hade denna __init__ overrida BaseShape __init__ 
    def CalculateArea(self):
        self.SetArea(self.Base * self.Height)

class Square(BaseShape):
    def __init__(self, base, height): 
        self.Base = base
        self.Height = height
        super().__init__()
    def CalculateArea(self):
        self.SetArea(self.Base * self.Height)

class Triangle(BaseShape):
    def __init__(self, base, height): 
        self.Base = base
        self.Height = height
        super().__init__()
    def CalculateArea(self):
        self.SetArea((self.Base * self.Height) / 2)

class Circle(BaseShape):
    def __init__(self, radius): 
        self.Radius = radius
        super().__init__()
    def CalculateArea(self):
        self.SetArea(math.pi * self.Radius**2)

class Hexagon(BaseShape):
    def __init__(self, sidelength):  
        self.SideLength = sidelength
        super().__init__()
    def CalculateArea(self):
        self.SetArea((3 * math.sqrt(3) * (self.SideLength ** 2)) / 2) #https://how.dev/answers/how-to-get-the-area-of-a-hexagon-in-python



testHexagon = Hexagon(5)
testCircle = Circle(5)
testTriangle = Triangle(5, 5)
testSquare = Square(5,5)
testRectangle = Rectangle(5,5)
print("Areor: ",
      f"\n Kvadrat : {testSquare.GetArea()} , bas : {testSquare.Base} , höjd , {testSquare.Height}",
      f"\n Rektangle : {testRectangle.GetArea()} , bas : {testRectangle.Base} , höjd , {testRectangle.Height}",
      f"\n Triangle : {testTriangle.GetArea()} , bas : {testTriangle.Base} , höjd , {testTriangle.Height}",
      f"\n Cirkel : {testCircle.GetArea()} , radien : {testCircle.Radius}",
      f"\n Hexagon : {testHexagon.GetArea()} , sidlängd : {testHexagon.SideLength}")