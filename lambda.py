#Using a normal function to calculate the square of a value
def suared(x):
    return x**2
print(suared(23))
#This will print the square of a value by normal means i.e functions
#Now using anonymous functions here
#First define a lambda by keyword lambda
#Then use a variable
#Then use the expression which we want

print((lambda x,y,z:x+y+z)(23,25,27))
#Trying With a list here

def app(lists,element):
    return lists.append(element)

print(app([1,2,3],4))
print((lambda x:x.append(2))([1,2,3]))