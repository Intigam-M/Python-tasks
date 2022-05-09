
# Istifadəçinin girdiyi mətnlərdəki hərfləri əlifba sırsanıda
# özünən sonra gələn hərflə dəyişdirən program yazın. 
# Örnək: input: Men Python 3 oyrenirem
# output: Nfo Qzuipo 3 pzsfojsfn

user_input = input("Write\n")
result=[]
word = ""
for char in user_input:
    if ord(char) != 32:
        next_char = chr(ord(char)+1)
        word += next_char
    else: 
        result.append(word)
        word =""   
else:
    result.append(word)  

print(*result)


# İstifadəçinin girdiyi mətn daxilindəki hərflərin ingilis əlifbasındakı
# sırasına qarşılıq gələn ədədlərlə dəyişdirilmiş şəkildə göstərin. 
# Örnək: input: Men Javascript oyrenirem
# output: 13,5,14, 10,1,22,1,19,3,18,9,16,20, 15,25,18,5,14,9,18,5,13,

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = ""
user_input = input("Write\n")
for char in user_input:
    if ord(char) != 32:
        letter_index = letters.index(char) + 1
        result+=str(letter_index)+","
print(result)


# Atadan 2 oğula bir ferma miras qalıb. Ata vəsiyyətində deyir ki, 
# fermanı ortadan 2-yə bölün, birinci yarısı böyük oğula, 
# ikinci yarısı isə kiçik oğula verilsin. Ədalətsizliyi aradan qaldırmaq üçün qardaşlar razılaşır ki, 
# gəl hərəmizə düşən fermadakı heyvanların qiymətlərini hesablayaq, 
# əgər kimin ferması daha çox pul edirsə,
# o aradakı fərqi bağlamaq üçün cibindən çıxarıb, digərinə nəğd pul versin. 
# Misal üçün əgər böyük qardaşın ferması 20000 manat,
# kiçik qardaşınkı 15000 manatdırsa, böyük qardaş öz cibindən çıxarıb kiçiyə 2500 manat versin,
# beləliklə hər birinin sərvəti eyni olsun.

ferma = ('at', 'inek', 'inek', 'keci', 'qoyun', 'qoyun', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'inek', 'keci', 'at', 'keci', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'keci', 'keci', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'at', 'keci', 'at', 'keci', 'inek', 'qoyun', 'keci', 'at', 'qoyun', 'inek', 'inek', 'toyuq', 'at', 'at', 'toyuq', 'at', 'inek', 'toyuq', 'inek', 'toyuq', 'toyuq', 'qoyun')
qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}

boyuk_oqul = []
kicik_oqul = []
boyuk_oqlan_pul = 0
kicik_oqlan_pul = 0

for i in range(1,len(ferma)+1):
    
    if i <= len(ferma) // 2:
        boyuk_oqul.append(ferma[i-1])
        boyuk_oqlan_pul += qiymetler[ferma[i-1]]
    else:    
        kicik_oqul.append(ferma[i-1]) 
        kicik_oqlan_pul += qiymetler[ferma[i-1]]

        
result =(abs(boyuk_oqlan_pul - kicik_oqlan_pul)) // 2

print(f'Boyuk qardasin pulu: {boyuk_oqlan_pul}')
print(f'Kicik qardasin pulu: {kicik_oqlan_pul}')

if boyuk_oqlan_pul > kicik_oqlan_pul:
    print(f"Boyuk qardas kiciye {result} manat vermelidir")
else:
    print(f"Kicik qardas boyuye {result} manat vermelidir")
        

