import re

def findAndReplace():
    string="This is a simple string"
    pattern=r"is"
    newString=re.sub(pattern,"iss",string)
    print(newString)

findAndReplace()
#dot metacharacter to replace a dot with an alphabet
def matchFunction():
    pattern=r"gr......y"
    string="greygraygrwygreeeeeey"
    print(re.findall(pattern,string))
matchFunction()

#Caret Metacharacter

def otherMetacharacter():
    pattern=r"^gr.y$"
    string="grey"
    print(re.findall(pattern,string))

otherMetacharacter()