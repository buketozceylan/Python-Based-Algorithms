grade = input('Enter your grade: ')
g = int(grade)

if (100 > g >= 70 ) :
    print('Your grade is ' + grade)
    print('Passed')
elif (0 <= g < 70) :
    print('Your grade is ' + grade)
    print('Failed')
else:
    print('Please enter right format')    
