class BaseShape:
    Area = None
    def CalculateArea():
        pass

class Rectangle(BaseShape):
    def __init__(self, base, height): # basically en constructor, värkar som att många på internet blir arga ifall man säger att det är en construktor
        self.Base = base
        self.Height = height
    