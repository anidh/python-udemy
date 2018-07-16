def fileHandling():
    file=open('demo.txt','r')
    #Doing Something with file
    content=file.read()
    print(content)
    file.close()
    newFile=open('newDemo.txt','a')
    #Writing Old Content To The New File
    newFile.write(content)
    newFile.close()
    #Reading content of new Files Now!!!
    updatedFile=open('newDemo.txt','r')
    newContent=updatedFile.read()
    print(newContent)
    updatedFile.close()


fileHandling()
