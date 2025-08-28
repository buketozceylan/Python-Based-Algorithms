word = input("Enter your word: ")

reverse = ''


for i in word:
    reverse = i + reverse
    
print(reverse)