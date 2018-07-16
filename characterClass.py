import re
pattern=r"[a-zA-z][a-zA-z][0-9]"
string="aa2"
print(re.findall(pattern,string))