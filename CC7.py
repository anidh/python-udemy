product_Info={"TV":25000,"Radio":1200,"Laptop":53000,"Phone":80000,"Charger":800}
product=input("Enter The Product Name")
print(product_Info.get(product,"Item Not Found Try Again!"))