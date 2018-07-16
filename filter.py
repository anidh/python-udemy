numbers=[x for x in range(100) if x%5==0]
newList=list(filter(lambda x:x%2==0,numbers))
print(newList)
