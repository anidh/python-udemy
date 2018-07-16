grade=input('Enter Your Grades\n')
grade=grade.capitalize()
if grade=='A':
    print('You secured more than 90 percent')
elif grade=='B':
    print('You secured marks between 60 and 89 Percent')
else:
    print('You Failed')