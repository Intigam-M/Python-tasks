ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']

# Fermada keçinin sırasını tapın
print(ferma.index("keci"))

# Fermadakı heyvanları ad sırasına görə sıralayın
ferma.sort()
print(ferma)

# Fermadan bir at çıxarıb, ən sağdan bir toyuq əlavə edin
ferma.remove("at")
ferma.append("toyuq")

# Ən soldan bir keci əlavə edin
ferma.insert(0,'keci')


# Fermanın yarısını dinamik bir şəkildə silin
half= int(len(ferma)) // 2
ferma[0:half] = []

# Fermadakı heyvanları 3 qatına çıxarın
print(ferma * 3)

# Fermadakı heyvanları tərsinə sıralayın
ferma.reverse()
print(ferma)

# Yeni gələn `['at', 'qoyun', 'inek', 'inek', 'qoyun']` heyvanları fermaya əlavə edin
ferma.extend(['at', 'qoyun', 'inek', 'inek', 'qoyun'])
print(ferma)

# Fermadakı ineklerin sayının ümumi fermanın neçə faizi olduğunu tapın
general_count = int(len(ferma))
cow_count =int(ferma.count("inek"))
result = cow_count * 100 // general_count
print(result)

# Oxşar fermadan istəyən basqa bir fermerə fermamızın kopyasını verini
ferma_copy = ferma.copy()
print(ferma_copy)

# Fermada təmir işi getməlidi, heyvanları çölə çıxarmaq üçün fermanı təmizləyin
ferma.clear()
print(ferma)


# Aşağıdakı result listinin 0-cı indexinə numbers listi daxilindəki müsbət ədədlərin cəmini, 
# 1-ci indexə isə mənfi ədədlərin cəmini yerləşdirin. 
result = [0, 0]
numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]

positive_number_sum = 0
negative_number_sum = 0

for number in numbers:
    if number > 0:
        positive_number_sum+=number
    else:
        negative_number_sum+=number
        
result[:]=[positive_number_sum, negative_number_sum]    
print(result)

# İstifadəçinin girdiyi ədədi tək ədədlərdən ibarət tərsinə çevirilmiş list şəklinə salın. 
# Listin bütün elementlərinin integer olmasına diqqət edin. Örnək:
numbers = input("Write number\n")
result = []

for number in numbers:
    if int(number) % 2 == 0:
        result.append(number)

result.reverse()
print(result)


# list içərisindəki ən böyük və ən kiçik ədədi dinamik şəkildə tapın.
numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
max_num = max(numbers) 
min_num = min(numbers) 
print(max_num, min_num)



#  Aşağıda tələbələrin semestr nəticələri qeyd edilmişdir. 
#  Buna əsasən qeyd olunmuş statistik məlumatları eyni anda print edin.
#     1. Tələbə sayı
#     2. Ümumi ortalama.
#     3. Kəsilən tələbələrin ümumi faizi (51- qiymət alanlar)
#     4. Yüksək nəticə göstərən tələbələrin ümumu faizi (80+ qiytət alanlar)


points=[31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]

students = len(points)

points_sum = 0
for point in points:
    points_sum+=int(point)
avarage = points_sum // students

failed_count = 0
for point in points:
    if point < 51:
        failed_count += 1
failed_per = failed_count * 100 // students

max_point= 0
for point in points:
    if point >= 80:
        max_point += 1
max_point_per = max_point * 100 // students

print("Students: " + str(students), "General Avarage: " + str(avarage), "Failed percentage: " + str(failed_per),"Max percentage: " + str(max_point_per), sep = "\n")
