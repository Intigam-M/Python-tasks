import math
import random
import datetime

# Sual 1
# Kürə və koni həcmlərini tapan funksiyalar hazırlayın

def circle_volume(r):
    return 4/3 * math.pi * pow(r, 3)

def koni_volume(r, h):
    return 1/3 * math.pi * pow(r, 2) * h


# Sual 2
# Permutasiya və kombinasiya tapan funksiyalar hazırlayın.

def permutasiya(n, r):
    return math.factorial(n) / math.factorial(n-r)

def kombinasiya (n, r):
    return math.factorial(n) /  (math.factorial(r) * math.factorial(n-r))


# Sual 3
# Give away programi duzeldin. 
# Adamlar bitənə qədər hər enter basanda bir ad göstərsin.

user_input = input('Adlari girin\n').split(',')
for name in user_input:
    print(random.choice(user_input))
    input()


# Sual 4
# Ədəd təxmin etmə oyunu hazırlayın. 
# Müəyən bir araılq verin və program həmin aralıqda bir ədəd təyin etsin.
# Daha sonra siz həmin ədədi tapana qədər oyun davam etsin. 
# Siz gizli ədədin aşağısında bir təxmin etdikdə program daha yuxarı,
# yuxarısında təxmin etdikdə isə daha aşağı desin.
# Ən sonda ədədi neçə səfərə tapdığınızı qeyd etsin. 
# Əgər 10 üzərində təxmin etdikdən sonra tapıbsızsa məğlub sayılırsız, əks təqdirdə qalib. 

def fun_brain(start, end, given_num):
    count = 0
    while True:
        random_num = random.randint(start, end)
        print(random_num)
        if random_num == given_num:
            result = 'Qalib' if count <= 10 else 'Meqlub'
            print (f'{result} Oldunuz! Verilən ədədi {count}-ci səfərdə tapdınız')
            break
        else:
            print ('Daha yuxarı' if random_num < given_num else 'Daha aşağı')

        input()    
        count+=1    


# Sual 5
# Random modulu ilə lotoreya kağızı düzəldən program hazırlayın.

lotoreya = ''
for i in range(15):
    num = random.randint(1,100)
    lotoreya+=str(num)+','
print(lotoreya)


# Sual 6
# Yer kürəsi ilə Pluton arasındakı məsfə 5.058 milyard kilometrdir. 
# Saatda 90 km/saat sürətlə, fasiləsiz hərəkət edən Niva maşını hansı tarixdə Plutona çatar?

hours = 5058000000 / 90
print(datetime.date.today() + datetime.timedelta(hours=hours)) 

