#Simple program to display regular expression
import re

def regularExpression():
    pattern= r"cats"
    string="baconcatscatscatsbacon"
    if re.match(pattern,string):
        print("Match Found")
    else:
        print("Match Not Found")


def searchFunctiion():
    pattern=r"cats"
    string="baconcatsBacon"
    if re.search(pattern,string):
        print("Match Found")
    else:
        print("Match Not Found")

def findAll():
    pattern=r"cats"
    string="baconbaconcatsbacon"
    if re.findall(pattern,string):
        print("Match Found Nigga",len(re.findall(pattern,string))," times")
    else:
        print("Value Not Found")


regularExpression()
searchFunctiion()
findAll()