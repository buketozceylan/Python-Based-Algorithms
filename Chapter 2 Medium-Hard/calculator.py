calculate = input("islem: ")

num1 = calculate[0:1]
num2 = calculate[2:3]

def sum():
    result = int(num1) + int(num2)
    print(result)

def extract():
    result = int(num1) - int(num2)
    print(result)

def multip():
    result = int(num1) * int(num2)
    print(result)
    
def divide():
    result = int(num1) / int(num2)
    print(result)
    
if "+" in calculate:
    sum()
elif "-" in calculate:
    extract()
elif "*" in calculate:
    multip()
elif "/" in calculate:
    divide()
else:
    print("Wrong parameter!")