class HiddenClass:
    __hiddenVariable=0

    def add(self,incr):
        self.__hiddenVariable+=incr
        print(self.__hiddenVariable)

x=HiddenClass()
x.add(5)
#Can't use hidden Variable
print(x.__hiddenVariable)