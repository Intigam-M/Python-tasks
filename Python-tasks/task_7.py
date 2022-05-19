# Sual 1
# Girilen stringlərin ilk hərfini böyüdüb,
# birləşdirən bir funksiya hazırlayın.

import math


def abbr(str):
    print(*[char[0].upper() for char in str.split()])


abbr('birlesmis', 'milletler', 'teskilati')

# Sual 2
# Girilen stringi qeyd edilen sekilde deyisen bir funksiya hazirlayin
# chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren')
# => 'Kitabi sehife-sehife oxumalisan ki, oyrenesen'


def chstr(args, **kwargs):
    correct_str = []
    for key, value in kwargs.items():
        if correct_str:
            correct_str[0] = correct_str[0].replace(key, value)
        else:
            correct_str.append(args.replace(key, value))
    print(*correct_str)


chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen',
      sehve='sehife', orgen='oyren')
# Sual 3
# Birinci argument ilk qiyməti, ikinci argument isə yeni qiyməti göstərir.
# Yeni qiymətin ilkindən neçə faiz fərqləndiyini print edən funksiya düzəldin.


def find_percent(old_price, new_price):
    result = old_price - new_price
    if result > 0:
        print(str(result * 100 // old_price) + "% azalmisdir")
    else:
        print(str(abs(result) * 100 // old_price) + "% artmisdir")


find_percent(200, 60)  # output: qiymet 70% azalmisdir
find_percent(100, 150)  # output: qiymet 50% artmisdir


# Sual 4
# Mətnlər üzərində işləmək üçün böyük bir program hazırlamsınız ancaq sonradan öyrənirsiniz ki,
# programı çalışdıracaq müştərinin komputeri azərbaycan şriftlərini dəstəkləmir.
# Bütün funksiyaları yenidən yazmaq yerinə elə bir dekorator yazın ki,
# həmin funksiyaların return etdiyi stringlərdəki aze hərfləri ingilis qarşılığıyla dəyişdirilmiş olsun.


def convert_eng(func):
    abc_dict = {"ə": "e", "ü": "u", "ç": "c", "ğ": "g", "ö": "o"}

    def inner(ad, soyad):
        for char in ad:
            if char in abc_dict:
                ad = ad.replace(char, abc_dict[char])

        for char in soyad:
            if char in abc_dict:
                soyad = soyad.replace(char, abc_dict[char])

        return func(ad, soyad)
    return inner


@convert_eng
def salam_ver(ad, soyad):
    return f'Salam hörmətli {ad} {soyad}, necəsiniz?'


print(salam_ver('name', 'surname'))

# Sual 5
# Girilən listin ən böyük ədədindən ən kiçiyini çıxarıb, nəticə verən bir funksiya hazırlayın.
# big_dif_sml([6, 3, 8, 9, 2]) => 7 # en  boyuk 9, en kicik 2


def big_dif_sml(args):
    boyuk_eded = -math.inf
    kicik_eded = math.inf
    for n in args:
        if n > boyuk_eded:
            boyuk_eded = n
        if n < kicik_eded:
            kicik_eded = n
    print(boyuk_eded - kicik_eded)


big_dif_sml([6, 3, 8, 9, 2])

# Sual 6
# üç rəqəmli ədədləri sözə çevirən bir funksiya hazırlayın.


def eded_cevir(num):
    num_onluq = ["Bir", "Iki", "Uc", "Dord",
                 "Bes", "Alti", "Yeddi", "Sekkiz", "Doqquz"]
    num_yuzluk = ["On", "Iyirmi", "Otuz", "Qirx",
                  "Elli", "Altimis", "Yetmis", "Seksen", "Doqsan"]

    result = []
    counter = 0
    for i in str(num):

        if counter == 0:
            result.append(num_onluq[int(i)-1])
        elif counter == 1:
            result.append("Yuz")
            if i != str(0):
                result.append(num_yuzluk[int(i)-1])
        else:
            if i != str(0):
                result.append(num_onluq[int(i)-1])
        counter += 1
    print(result)


eded_cevir(311)
