print('This is a sample list....\n')
list=['Anidh','Shubhangi','Anshuman']
print(list)
print('This is another sample list...\n')
listNew=[1,2,3]
print(listNew)
emptyList=[]
# print('Welcome to the list Program..\n')
# print('1)Replace Value\n2)Adding Two List\n3)Multiply Two List\n4)Checking for a value in List\n')
# choice=int(input())
# if choice==1:
#     print('Enter The Value to be substituted\n')
#     value=int(input())
#     print('Enter The index from which value will be substituted\n')
#     index=int(input())
#     list[index]=value
#     print(list)
# elif choice==2:
#     print('We are going to add two list..\n')
#     emptyList=list+listNew
#     print(emptyList)
# elif choice==3:
#     print('We are going to multiply a list by a constant...')
#     print('Enter the constant value..\n')
#     constant=int(input())
#     emptyList=list*constant
#     print(emptyList)
# elif choice==4:
#     print('Enter the value which you want to check in the list\n')
#     key=input()
#     if key in list:
#         print('Value found!!')
#     else:
#         print('Not Found')
# else:
#     print('Enter a valid value\n Exiting....')

print('Welcome to list functions program...\n')
print('1)Add a new value to the list\n2)Find length of the List\n3)Add value at paticular position \n4)Return index of a value\n')
choice=int(input('Enter Your Choice\n'))
if choice==1:
    value=input('Enter the value to be added\n')
    list.append(value)
    print(list)

elif choice==2:
    print('Finding the length of the list......\n')
    print(len(list))
elif choice==3:
    print('Inserting a paticular value at a paticular index...\n')
    value=input('Enter The Value To Be Inserted\n')
    index=int(input('Enter The Index Where To be Inserted'))
    list.insert(index,value)
    print(list)
elif choice==4:
    print('Finding the Index Of A Value...\n')
    value=input('Value To Be Found')
    print(list.index(value))
else:
    print('Enter a Valid Value...\nExiting....\n')
