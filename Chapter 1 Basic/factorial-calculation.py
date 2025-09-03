number = int(input('Enter your number: '))
fact = 1

for i in range(1,number+1):
    fact *= i
    
print(fact)