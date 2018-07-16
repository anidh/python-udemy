#Usage of range in python
# newList=list(range(1,11,1))
# print(newList)
# def function():
#     list=[1,2,3,4,5,6]
#     print('Printing the numbers from 1 to 10')
#     for x in range(1,11):
#         print(x)
#     print('Now Traversing The List...\n')
#     for traverser in list:
#         print(traverser)
#
# function()
#
#
def even():
    print('Checking for Even Numbers in a given range...\n')
    r=int(input('Enter The Limit till where you want to check...\n'))
    for x in range(1,r,1):
        if(x%2==0):
            print(x)
        else:
            continue


even()

#Printing a thing n times
# for x in range(1,6,1):
#     print('Anidh + Shubhu=<3')