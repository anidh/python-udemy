def student_Discount(price):
    return (price-(price*0.10))

def additional_Dicount(newPrice):
    return (newPrice-(newPrice*0.05))

print(additional_Dicount(student_Discount(320)))