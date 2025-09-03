word = input('Enter your word: ')
reverse = ""

if len(word) % 2 == 0:
    print('Your word is not Palindrom!')
else:
    for i in word:
        reverse = i + reverse
    if reverse == word:
        print('Your word is Palindrom!')
    else: 
        print('Your word is not Palindrom!')