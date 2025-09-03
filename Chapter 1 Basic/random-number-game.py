import random

num = random.randint(1,100)
guess = 0
guessCount = 0

while num != guess:
    guess = int(input('Your Guess: '))
    if num > guess:
        print('Higher!')
        guessCount += 1
    elif num < guess:
        print('Lower!')
        guessCount += 1
    else:
        print(f'You find it! You guessed {guessCount} times!')
        break
