import math

class BaseShape:
    def __init__(self):
        self._Area = None
    def CalculateArea(): #abstrakt även fast jag tror att python inte direkt har type safety och man nog inte skulle behöva att verifiera att den har CalculateArea() 
        pass

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
        super().__init__() # super() gör så att BaseShapes __Init__ också kallas annars så hade denna __init__ overrida BaseShape __init__ 
        self.Base = base
        self.Height = height
    def CalculateArea(self):
        self.SetArea(self.Base * self.Height)

class Square(BaseShape):
    def __init__(self, base, height): 
        super().__init__()
        self.Base = base
        self.Height = height
    def CalculateArea(self):
        self.SetArea(self.Base * self.Height)

class Triangle(BaseShape):
    def __init__(self, base, height): 
        super().__init__()
        self.Base = base
        self.Height = height
    def CalculateArea(self):
        self.SetArea((self.Base * self.Height) / 2)

class Circle(BaseShape):
    def __init__(self, radius): 
        super().__init__()
        self.Radius = radius
    def CalculateArea(self):
        self.SetArea(math.pi * self.Radius**2)

class Hexagon(BaseShape):
    def __init__(self, sidelength):  
        super().__init__()
        self.SideLength = sidelength
    def CalculateArea(self):
        self.SetArea((3 * math.sqrt(3) * (self.SideLength ** 2)) / 2) #https://how.dev/answers/how-to-get-the-area-of-a-hexagon-in-python



hello = Hexagon(5)
hello.CalculateArea()
print(hello.GetArea())
input()