number = int(input('Enter a number: '))

count = 0

for i in range(1,number+1):
    if number / i == True:
        count += 1
        print(count)
        
if count > 2:
    print(f'{number} is not prime number')
else:
    print(f'{number} is prime number')