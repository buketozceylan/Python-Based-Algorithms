print("Enter the number by dividing it by (,)")

numbers = input()

numberList = numbers.split(",")

total = 0

for i in numberList:
    total += int(i)

print(f"Your total: {total}")    