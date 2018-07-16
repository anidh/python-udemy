#Functional Programming is nothing but having to break down the program into various functions
#Just To add 10 to the value
def add_Ten(value):
    return value+10
#This functions firsts calls the add_Ten funcction and then calls it's again
def twice_Call(func,ar):
    return func(func(ar))
#Value Of 30 as 10 is added twice to 10
print(twice_Call(add_Ten,10))