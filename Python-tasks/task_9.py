baliqlar = {
    'qeleseme teneffusu', '2 kamerali urek', 'uzgec', 'korteks yoxdur',
    'yumurtlama', 'dis yoxdur', '4 ayaq'
}

cuculer = {
    'toraks teneffusu', 'urek yoxdur', '6 ayaq',
    'korteks vardir', 'beyin yoxdur', 'yumurtlama', 'metamorfoz', 
    'dis yoxdur'
}

amfibialar = {
    'qelseme teneffusu', 'agciyer teneffusu', 'uzgec', '4 ayaq', 
    '2 kamerali urek', '3 kamerali urek', 'metamorfoz', 'kotex vardir',
    'yumurtlama', 'dis yoxdur'
}

surunenler = {
    'agciyer teneffusu', '3 kamerali urek', '4 ayaq', 'korteks vardir', 'yumurtlama',
    'dis var'
}

quslar = {
    'agciyer teneffusu', '4 kamerali urek', 'korteks vardir',
    'yumurtlama', 'dis yoxdur'
}

memeliler = {
    'agciyer teneffusu', '4 kamerali urek', '4 ayaq', 'korteks vardir',
    'dogma', 'dis vardir'
}

sinifler = {
    'baliqlar': baliqlar,
    'cuculer': cuculer,
    'amfibialar': amfibialar,
    'surunenler': surunenler,
    'quslar': quslar,
    'memeliler': memeliler,
}
# Quşların xüsusiyyətlərinə "2 ayaq" əlavə edin.
quslar.add('2 ayaq')
print (quslar)

# Balıqların xüsusiyyətlərindən "4 ayaq" məlumatını çıxarın
baliqlar.remove('4 ayaq')
print (baliqlar)

# Amfibialar ilə cücülərin ortaq cəhətlərini göstərən kod yazın
print(amfibialar.intersection(cuculer))

# Balıqlar ilə amfibiaların fərqli cəhətlərini göstərən kod yazın
print(baliqlar.symmetric_difference(amfibialar))

# Balıqlar ilə heç bir ortaq cəhətə sahib olmayan sinifi tapan kod yazın
for sinif,info in sinifler.items():
    if sinif != 'baliqlar':
        if not baliqlar.intersection(info):
            print(f'Heç bir ortaq cehete sahib olmayan sinif: {sinif}')
        else:
            print(f'Ortaq cehete sahib olan sinif: {sinif}')


# Quşlar ilə ən çox ortaq cəhətə sahib olan sinifi tapın
result={}
for sinif,info in sinifler.items():
    if sinif != 'quslar':
        common = quslar.intersection(info)    
        if common:
          result[sinif] = len(common)
print(max(result))

     
# İstifadəçi input ilə sizə bəzi özəlliklər girəcək. 
# Siz həmin özəlliklərə əsasən heyvanın hansı sinifə aid ola biləcəyini təxmin edən kod yazın.
user_data = input("Write\n")     

user_data = 'dis yoxdur, agciyer teneffusu, korteks vardir'
user_data = user_data.split(", ")    
user_data = set(user_data)

for sinif,info in sinifler.items():
    common = user_data.intersection(info) 
    if len(user_data) == len(common):
        print(f'Bu heyvan {sinif} alemine aid ola biler')
           


           