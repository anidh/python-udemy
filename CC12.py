class Computer:
    def __init__(self,modelName,yearOfMfg):
        self.modelName=modelName
        self.yearOfMfg=yearOfMfg

    def getSpecs(self):
        self.modelName=input("Enter The Model Name")
        self.yearOfMfg=input("Enter The Year Of Manufacturing")

    def displaySpecs(self):
        print("The Model Name Is",self.modelName," Year Of Manufacturing Is",self.yearOfMfg)

class desktopComputer(Computer):
    def __init__(self,modelName,yearOfMfg,Weight):
        self.modelName = modelName
        self.yearOfMfg = yearOfMfg
        self.Weight=Weight

    def getSpecs(self):
        self.modelName = input("Enter The Model Name")
        self.yearOfMfg = input("Enter The Year Of Manufacturing")
        self.Weight=int(input("Enter The Weight Of The Desktop"))

    def displaySpecs(self):
        print("The Model Name Is", self.modelName, " Year Of Manufacturing Is", self.yearOfMfg," The Weight of Desktop is ", self.Weight)

class laptopComputer(Computer):
    def __init__(self,modelName,yearOfMfg,processor):
        self.modelName = modelName
        self.yearOfMfg = yearOfMfg
        self.processor = processor

    def getSpecs(self):
        self.modelName = input("Enter The Model Name")
        self.yearOfMfg = input("Enter The Year Of Manufacturing")
        self.processor=(input("Enter The Processor Of The Laptop"))

    def displaySpecs(self):
        print("The Model Name Is", self.modelName, " Year Of Manufacturing Is", self.yearOfMfg," The Processor of Laptop is ", self.processor)


computer=Computer("Compaq","2017")
computer.getSpecs()
computer.displaySpecs()
#Using Desktop Computer Methods
desktop=desktopComputer("HP","2018",3)
desktop.getSpecs()
desktop.displaySpecs()
#Using Laptop Computer Methods
laptop=laptopComputer("Lenovo",2013,"i7")
laptop.getSpecs()
laptop.displaySpecs()