
import re

# Sual 1 
# Aşağıdakı listdə düzgün formada ad və soyad yazılmayan sözləri çıxarın:

users = ['Aygun Kazimova', 'fermer Həsən', 'Namiq Qaracuxurlu', 'Rehim Rehimli', 'roya Ayxan', 'Eynulla']

pattern = '^[A-Z][a-z]+\s[A-Z][a-z]+'
for user in users:
    match = re.match(pattern, user)
    if not match:
        users.remove(user)
        

# Sual 3
# Aşağdakı mətindəki bütün saytları list şəklində çıxarın.      
data = """Dünyada bir çox saytlar mövcuddur. Bunların bir çoxu fərqli məqsədlərə xidmət edirlər. Müsal üçün http://www.google.com saytı axtarış üçün istifadə olunur. Digər yandan https://facebook.com və http://www.instagram.com saytları sosial şəbəkə kimi fəaliyyət göstərirlər"""

pattern = 'https?://(www.)?[a-z]+\.[a-z]+'
sites = re.findall(pattern, data)


# Sual 4
# Istifadəçi adı, email, şifrə tələb olunan bir sistem quracaqsınız. 
# İstifadəçi adı yazlnız kiçik hərflər, 
# altdan xətt və nöqtədən ibarət olmalıdır. 
# Emaildə başlanğıc və sonu çıxmaq şərtiylə ən az bir dənə nöqtə və sadəcə bir dənə @ işarəsi olmalıdır. 
# Şifrədə boşluq xaricində hər şey qəbul edilir. 
# Bunları validasiya etmək üçün regex pattern hazırlayın.

user_name_pattern ='^[a-z]+(\.?|_)[a-z]+'
email_pattern = '[A-Za-z1-9]+\.[A-Za-z1-9]+@[a-z]+\.[a-z]+'
password_pattern = '\S+'


# Sual 5
# Aşağıdakı nömrələr arasında azercell nömrələri bir list daxilində toplayın:

number = """051-235-642-12, 055-236-642-23, 077-623-234-26, 
51-125-646-32, 50-125-542-12, 70-253-644-12, 050-135-346-64"""

pattern = '^0?50|51-\d{3}-\d{3}-\d{2}'
print(re.findall(pattern, number))