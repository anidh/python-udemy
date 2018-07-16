#BMI Calculator
def bmiCalc(weight,height):
    bmi=(weight)/(height**2)
    return bmi

weight=int(input('Give Weight In Kgs\n'))
height=float(input('Give Height In Ms\n'))
result=bmiCalc(weight,height)
print('Your BMI Score is:'+str(result))