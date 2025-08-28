phone = input('Enter your phone number: ')

# phoneList = list(str(phone))      #make list of the numbers one by one         

numbers = ("Zero" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine")

write = []

for i in phone:
    write.append(numbers[int(i)]) 

print(write)
