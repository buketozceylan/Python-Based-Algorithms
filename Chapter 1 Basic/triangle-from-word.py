word = input("Enter your word: ")

for i in range(len(word)):
    print(word[:i+1]) #Writes from 0 to i+1th letter
    
    