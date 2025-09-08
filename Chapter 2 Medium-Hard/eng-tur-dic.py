print('English-Turkish Colors Dictionary')
print('Enter your color and then We translate')
print('***************************************')


cont = ''

Colors = {
    'red' : 'kirmizi',
    'black' : 'siyah',
    'white' : 'beyaz',
    'orange' : 'turuncu',
    'purple' : 'mor',
    'green' : 'yesil',
    'yellow' : 'sari',
    'blue' : 'mavi',
    'brown' : 'kahverengi',
}
def colorDict():
    color = input('Color: ')
    color = color.lower()
    if color in Colors:
        print(Colors[color])
        
    else:
        print('Please enter simple color! ')
        color = input('Color: ')
        

while True:
    colorDict()
    cont = input('Do you want to continue? Y/N ')
    cont == cont.lower()
    if cont == 'y' or cont == 'yes':
        colorDict()
    else:
        break
    
    