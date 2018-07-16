class Coordinate:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self, other):
        x=self.x+other.x
        y=self.y+other.y
        return Coordinate(x,y)
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)


point=Coordinate(3,4)
point2=Coordinate(4,12)
print(point+point2)