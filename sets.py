mySet={x for x in range(10)}
print(mySet)
#Functions of Sets Membership Test
print(5 in mySet)
#Add Element
mySet.add(10)
print(mySet)
#Remove A Element
mySet.remove(4)
print(mySet)
#Perform ALgerbraic Expression
#Using Another Set
newSet={y for y in range(10,20) if y%2==0}
print(newSet)
newSet.add(4)
newSet.add(10)
#Using Union of Sets
print(mySet|newSet)
#Using Intersection
print(mySet&newSet)
#using Diffrence
print(mySet-newSet)