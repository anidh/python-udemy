class Factorial:
    #Default constructor for initialization
    def __init__(self,x):
        self.x=x
    #Factorial Function willl use x of here
    def factorial(self,x):
        if (x==1):
            return 1
        else:
            return (x*(self.factorial(x-1)))

#Calling the function by first creating an object
value=Factorial(5)
print(value.factorial(5))
