class operatorOverloading:
    def __init__(self,x):
        self.x=x

    def __mul__(self, other):
        return operatorOverloading(self.x+other.x)

    def __str__(self):
        return "({0})".format(self.x)

oo=operatorOverloading(6)
oo1=operatorOverloading(7)

print(oo*oo1)