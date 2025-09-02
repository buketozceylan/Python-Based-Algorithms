word = input('Enter your word: ')

if len(word) % 2 != 0:
    print('Word is not symmetrical!')
else:
    
    mid = int(len(word) / 2)
    begin = word[:mid]
    end = word[mid:]
    if begin == end:
        print('Word is symmetrical!')
    else:
        print('Word is not symmetrical!')