#Using a function here to add string to a value
def add_String(ar):
    return ar+"Hello"

print(list(map(add_String,["Anidh","Shubhu","Forever"])))

#Using Lambda Expression + Maps Here

print(list(map(lambda x:x+"Forever",["Anidh","Shubhu"])))