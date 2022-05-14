# Sual 1 
# n1 = 15 və n2 = 13. Başqa bir variable yaratmadan aşağıdakı sual işarələrini doludurun.
# print('%s + %s = %s' ??????????) 
# Output bu şəkildə olmalıdır: 15 + 13 = 28

n1 = 15 
n2 = 13

print('%s + %s = %s' %(n1, n2, n1 + n2)) 

# Sual 2
# userData variablendan istifadə edərək aşağıdakı outputu çıxarın
# Hormetli A. E. Serifov, sizin 5326-6644********** nomreli
# kredit kartiniza 341.35AZN odenis edildi.
# Umumi 12,543AZN teskil eden borcunuzdan 2.72% borc silinmisdir!

userData = [
    {
        'debt': 12543,
        'payed': 341.346742,
        'payed_percent': 0.027214122777644904,
        'card_number': '5326-6644-1234-6432',
        'first_name': 'Akif',
        'last_name': 'Serifov',
        'father_name': 'Elekber',
    }
]

print('''Hormetli {first_name:.1}.{father_name:.1}.{last_name}, sizin {card_number:*<17.9} nomreli
kredit kartiniza {payed:.2f}AZN odenis edildi.
Umumi {debt:,}AZN teskil eden borcunuzdan {payed_percent:%} borc silinmisdir!'''.format(**userData[0]))

# Sual 3
# Aşağıdakı outputu çıxaran kod yazın.
	#      0         0         0         0
    #      1         1         1         1
    #      2        10         2         2
    #      3        11         3         3
    #      4       100         4         4
    #      5       101         5         5

print ("{:<10} {:<10} {:<10} {:<10}".format('Decimal','Binary','Octal','Hex'))

for i in range(30):
    print ("{:<10} {:<10} {:<10} {:<10}".format(i, bin(i)[2:], oct(i)[2:], hex(i)[2:]))
    
# Sual 4
# Örnək outputa nəzər yetirərək nəticənin həmin formada alınmasına diqqət edin.

# Axtarilan Heyvan: At
# --------------------
# Fermadaki at sayi:  12
# Diger heyvanlara olan faizi: 24.00%
# At umumi qiymeti: 14,400 AZN
    
animal = input('Ferma admin paneline xos geldiniz. Axtardiginiz heyvani daxil edin: ')
farm = ['inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', 'at', 'toyuq', 'inek', 'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'qoyun', 'keci', 'keci', 'qoyun', 'at', 'qoyun', 'inek', 'at', 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 'keci', 'inek', 'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek']
qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}

text = f"""
Axtarilan Heyvan: {animal}
{"-"*25}
Fermadaki {animal} sayi:  {farm.count(animal)}
Diger heyvanlara olan faizi: {farm.count(animal) * 100 // len(farm):.2f}%
{animal} umumi qiymeti: {farm.count(animal) * qiymetler[animal]:,} AZN
"""
print(text)
    
