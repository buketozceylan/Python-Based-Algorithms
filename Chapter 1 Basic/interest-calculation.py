mainMoney = int(input("Main Money: "))
interestRate = int(input("Interest Rate (monthly): "))
time = int(input("Time (month): "))

interest = int((mainMoney / 100) * (interestRate / 12) * time)

print(f"Basic interest: {interest}")