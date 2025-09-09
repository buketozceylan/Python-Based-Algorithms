codes = {
    'a' : 'Adana', 'b' : 'Bolu', 'c' : 'Ceyhan', 'd' : 'Denizli', 'e' : 'Edirne', 'f' : 'Fatsa', 'g' : 'Giresun', 'ğ' : 'Yumusak G', 'h' : 'Hatay', 'i' : 'İzmir', 'ı' : 'Isparta', 'j' : 'Jandarma', 'k' : 'Kars', 'l' : 'Lüleburgaz', 'm' : 'Mersin', 'n' : 'Niğde', 'o' : 'Ordu', 'ö' : 'Ödemiş', 'p' : 'Polatlı', 'r' : 'Rize', 's' : 'Sinop', 'ş' : 'Şırnak', 't' : 'Tokat', 'u' : 'Uşak', 'ü' : 'Ünye', 'v' : 'Van', 'y' : 'Yozgat', 'z' : 'Zonguldak'
}

word = input('Enter your word: ')

word = word.lower()

for i in range(0, len(word)):
    print(word[i].upper() + ': '+ codes[word[i]])

