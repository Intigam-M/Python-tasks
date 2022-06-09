import time
import os
import json
import uuid
import secrets

# Sual 1
# Geri sayim programi hazirlayin. 
# Input olaraq bir deyer verin və program həmin dəyərdən 0-da doğru saniyə-saniyə geri saysın. 
# 0-a çatdıqda bitdi desin.

set_timer = int(input('write\n'))
while True: 
    print(set_timer)
    if set_timer == 0:
        print('Bitdi') 
        break   
    set_timer -= 1
    time.sleep(0.5)


# Sual 2
# İçində olduğunuz dirin parentinin parentində olan faylların extensionlarını göstərən program hazırlayın.

path = os.path.dirname(os.path.dirname(os.getcwd()))
file_list = os.listdir(path)

for file in file_list:
    if os.path.isfile(path+'\\'+file):
        print(os.path.splitext(file)[1])


# Sual 3
# Bu datanı alıb istifadəçilərə uniqe id və (token ile) şifrə verərək yenidən save edin.

with open('info.json', 'r') as f:
    json_data = f.read()
    users = json.loads(json_data)
    for info in users:
        info['id'] = str(uuid.uuid4())
        info['password'] = secrets.token_hex(8)

with open('info.json', 'w') as f:     
    f.write(json.dumps(users, indent=4, sort_keys=True ))


