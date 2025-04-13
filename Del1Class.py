class BaseShape:
    def __init__(self):
        self._Area = None
    def CalculateArea(): #abstrakt även fast jag tror att python inte direkt har type safety och man nog inte skulle behöva att verifiera att den har CalculateArea() 
        pass

    def SetArea(self, NewArea):
        if not _IsValidNumber():
            return
        self._Area = NewArea
    def GetArea(self):
        return self._Area
    
    def _IsValidNumber(Number):
        if type(Number) != float:
            return False
        return True

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
    def __init__(self, base, height): 
        super().__init__()
        self.Base = base
        self.Height = height
    def CalculateArea(self):
        self.SetArea(self.Base * self.Height)
class Hexagon(BaseShape):
    def __init__(self, base, height): 
        super().__init__()
        self.Base = base
        self.Height = height
    def CalculateArea(self):
        self.SetArea(self.Base * self.Height)



hello = Rectangle(3, 5)
hello.CalculateArea()
print(hello.GetArea())
input()