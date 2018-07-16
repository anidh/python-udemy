# #Using Cube Values
#
# def cubedValues(x):
#     cube=int(x)**3
#     return cube
#
# result=cubedValues(3)
# print('The Cubed Value of 3 is:' + str(result))

#Using Function as Parameters

def add(a,b):
    c=a+b
    return c

def multiply(a,b):
    d=a*b
    return d

def squared(a,b):
    e=a**b
    return e

print(squared(add(1,2),multiply(1,2)))