item_Price=[x for x in range(102) if x%3 ==0 if x%4 ==0 ]
def discount(x):
    return x-(x*0.10)

print(list(map(discount,item_Price)))