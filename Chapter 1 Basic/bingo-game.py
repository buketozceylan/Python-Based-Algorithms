import random
guessCount = 0
guesslist = []

while True:
    guess = random.randint(0,91)
    
    input('Press [Enter] for generate code')
    print(guess)
    
    guessCount = guesslist.count(guess)
    
    if guessCount == 0:
        guesslist.append(guess)
        
    guesslist.sort()
    print(guesslist)
    
    if len(guesslist) >= 90:
        break
    
    