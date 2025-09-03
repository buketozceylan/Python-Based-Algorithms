count = int(input('Enter a countdown number: '))
countdown = []

for i in range(1,count+1):
    countdown.append(i)
    countdown.sort(reverse = True)

for j in range(0,count+1):
    print(countdown[j])

   
        

    
    
