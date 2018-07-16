import re

def starMetacharacter():
    pattern=r"eggs(bacon)*"
    string="eggsbaconbaconbacon"
    print(re.findall(pattern,string))


starMetacharacter()

def groupsInRegex():
    pattern="[A-z]([A-z])+[0-9]"
    string="AA8"
    if re.search(pattern,string):
        print("Match Found")
    else:
        print("Match Not Found")



groupsInRegex()