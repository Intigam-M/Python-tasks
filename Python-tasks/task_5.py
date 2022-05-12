# Istifadəçinin girdiyi stringi binary şəklində göstərin. 

print(" ".join(format(ord(char), 'b') for char in input("Cumle daxil edin\n")))


# Istifadəçi input olaraq color: rgb(127, 255, 12) şəklində CSS rəngi girəcək. 
# Siz istifadəçinin girdiyi rəngi 16-lıq sistemdəki qarşılığına çevirin. 

print("".join(hex(int(i))[2:] for i in  input("cumle daxil edin\n")[11:-1].split(", ")))   
