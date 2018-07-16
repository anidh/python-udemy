principal=int(input('Enter The Principal Amount\n'))
roi=float(input('Enter The Rate Of Interest\n'))
tp=int(input('Enter The Time Period\n'))
si=(principal*roi*tp)/100
print('The Value of Simple Interest '+ str(tp)+ ' Years is '+str(si))
