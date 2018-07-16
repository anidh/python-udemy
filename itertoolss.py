#Importing itertools
from itertools import count,accumulate,takewhile

for i in count(10):
    print(i)
    if i>=20:
        break

#Ussing accumalate to add the previous values to the new value
numbers=list(accumulate(range(8)))
print(numbers)

#Using the take while function to take items from a list only when the condition is true
print(list(takewhile(lambda x:x<=6,numbers)))