#Girilən ədədin faktorialını tapan kod hazırlayın.

input_num = input("Write number\n") 
factorial = 1
for x in range(1,int(input_num)+1):
    factorial*=x
print(factorial)   



# İstifadəçinin girdiyi cümlədə neçə heca olduğunu deyən program hazırlayın. Hecaların sayını tapmaq üçün saitlərdən istifadə edin.

input_sentence = input("Write sentence\n").lower() 
saitler = ["a","e","ə","i","ı","u","ü","o","ö"]
counter = 0
for sait in input_sentence:
    if sait in saitler:
        counter+=1
print(counter)   


# İstifadəçidən nömrə istəyən bir program hazırlayın. 
# Nömrələr +994 ilə başlamalı və uzunluğu 13 ədəddən ibarət olmalıdı. 
# İlk characteri olan + çıxmaq şərtilə ancaq ədədlərdən ibarət olmalıdır. 
# Əgər istifadəçi səhv yazarsa istifadəçiyə səhfini bildirib, yenidən soruşun. 
# Bunu etmək üçün while istifadə edin. 
# İstifadəçi düzgün yazdıqda isə break edib, ardından məlumatın düzgün olduğunu bildirin. 
# Əgər istifadəçi məlumatı girən zaman sağda solda boşluq buraxarsa həmin boşlquqları silin.



while True:
    input_phone_number = input("Write your phone number\n").strip()
    length = len(input_phone_number[1:])
    prefix =input_phone_number.startswith("+994")
    if input_phone_number[1:].isnumeric():
        if prefix:
            if length == 13 :
                 print("Duzgun nomre daxil edildi !!!!")
                 break
            else:
                print("13 reqem daxil edin")
        else:
            print("Nomre +994 ile baslamalidir")
    else:
        print("Nomre yalniz reqemlerden ibaret ola biler")



# Print argumentlerinden istifade

a = '123456789'
print(*a[::-1], sep = " saniye \n", end = "Vaxt bitdi \n")


# Girilən ədədin sadə bölənlərini göstərən kod hazırlayın. Örnək 12 ⇒ 2, 2, 3

bolen = 2
input_number = int(input("Write number\n")) 
while True:
    if input_number % bolen == 0:
        input_number = input_number // bolen
        print(bolen)
    else:
        bolen+=1
    if input_number == 1:
        break