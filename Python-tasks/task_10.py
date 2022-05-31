# Sual 1
# 1000-dən 0001-ə qədər sağında nöqtə ilə düzülmüş bir text faylı hazırlayın

with open('text.txt', 'w') as f:
    counter = 1000
    while counter >= 1:
        f.write(str(counter).zfill(4)+'\n')
        counter-=1


#  Sual 2       
# HTML, CSS, JS fayllarını minify (tək sətr) edən program hazirlayin hazırlayın. Örnək:
# input ⇒ Minify etmek istediyiniz faylin adresini girin: C:\Users\Profile\Desktop\Project\app.js
# output ⇒ Fayl uğurla minify edildi!

file_path = input('Minify etmek istediyiniz faylin adresini girin\n')
with open(file_path,'r') as f:
   numbers = f.readlines()
   Minify = "".join([number.rstrip('\n') for number in numbers])
    
with open(file_path,'w') as f1:
    f1.write(Minify)
    print('Fayl uğurla minify edildi!')


# Sual 3  
# Bu fayldaki sətrləri maaşa görə çoxdan aza sıralanmış hala salın

with open('text.txt') as f:
    employees = f.readlines()
    employees.sort(key=lambda employee: employee.split()[2], reverse=True )
    print(employees)
   