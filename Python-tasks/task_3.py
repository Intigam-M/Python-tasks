
# Istifadəçi sizə "5 salam" şəklində solda ədəd, 
# ortada, boşluq, sağda isə bir input alacaqsınız. 
# Buna əsasən sağdakı yazını istifadəçinin qeyd etdiyi ədəd qədər yazıb, istifadəçiyə qatarın. 
# Örnək yuxaridakı inputun outputu salam salam salam salam salam  

user_val = input("Write...\n")
split_user_val = user_val.split()
result = [split_user_val[1] for x in range(int(split_user_val[0]))]
print(*result)


# ['alma', 'armud', 'heyva', 'nar', 'saftali']` şəklində listimiz var. 
# Bu listdən istifadə edərək bir dictionary qurun. 
# Keylər listin elementləri, value-lar isə elementin hərf sayı olsun. 
# Bunun üçünü dictionary comprehensions yöntəmindən yararlana bilərsiniz. 
# Misal: `{'alma': 4, ...}

fruits = ['alma', 'armud', 'heyva', 'nar', 'saftali']
fruits_dict = {key: len(key) for key in fruits}
print(fruits_dict)


# Aşağıdakı fake databazanı istifadə edərək login sistemi qurun.

users = [
    {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
    {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
    {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
]

user_name = input("Username\n")
user_pass = input("Password\n")

user_not_found = True
for user_info in users:
    if user_name == user_info['name']:
        user_not_found = False
        if user_pass == user_info['password']:
            if not user_info['blocked']:
                print('Successful!')
            else: 
                print('Account blocked!')
        else:
             print('Wrong password!')
if user_not_found:
    print('User not found!')


# -100-dən müsbət 100-ə qədər ədədlər arasında 7-yə bölünən 
# ədədlərin 3-ə vurulmasından ibarət bir list qurun. 
# Bunun üçün range və list comprehensions istifadə edin.

print([x * 3 for x in range(-100,100) if x % 7 == 0 ])


# options = {'key': len, reverse: True} bu dictionary-dən istifadə edərək 
# ['alma', 'armud', 'heyva', 'nar', 'saftali'] listi sort edin.

fruits = ['alma', 'armud', 'heyva', 'nar', 'saftali']
fruits.sort(key=lambda x: len(x), reverse=True)
print(fruits)


# Istifadəçi sizə bir input vasitəsilə bunun kimi bir məlumat girəcək:
# input: firstname Elcin, username elchina, birthday 18-08-2000
# Bu inputa əsasən yuxarıdakı dictionary-ni update edin ve istifadəçiye gosterin. 
# Misal yuxarıdakı inputa əsasən dictionary son halı aşağıdakı kimi olacaq.

user_info = {
    'firstname': 'Elvin',
    'lastname': 'Huseynov',
    'username': 'elivin_h_ov',
    'password': '12345',
    'birthday': '19-08-1997'
}

user_data = input("Write\n")
split_data=user_data.split(',')

for word in split_data:
    split_word = word.split()
    for key in user_info.keys():
        if key == split_word[0]:
            user_info.update({split_word[0]: split_word[1]})
     
print(user_info)

