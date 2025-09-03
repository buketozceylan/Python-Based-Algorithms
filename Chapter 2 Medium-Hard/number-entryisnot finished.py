total = 0
numberList = []

while True:
    number = int(input('Enter a number: '))
    if type(number) == "str":
        break
    total += number
    print(total)
    