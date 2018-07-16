class Car:
    def __init__(self,model,price):
        self.model=model
        self.price=price
    def printDetail(self):
        print("Car Name is ",self.model,"Price of the care is",self.price)

    def getDetails(self):
        self.model=input("Enter Car Name")
        self.price=int(input("Enter Price Of The Car"))

class hondaCar(Car):
    def __init__(self,model,price,gear):
        self.model=model
        self.price=price
        self.gear=gear
    def hondaCompany(self):
        print("This is Honda Class Methods....")


civicCar=hondaCar("Honda Civic",2500000,"Manual")
civicCar.hondaCompany()
civicCar.getDetails()
civicCar.printDetail()