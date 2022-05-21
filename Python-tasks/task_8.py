# Sual 1
# Aşağıdakı düsturladan 10-unu seçib, 
# valueləri lambda ilə yazılmış funksya olan, 
# 10 itemdən ibarət dictionary düzəldin. 
# Daha sonra həmin funksiyaları istifadə edin.

physic = {
	'F': lambda m, a: m * a,
    'W': lambda f, s: f * s,
    'T': lambda f: 1 / f,
    'P': lambda m, v: m / v,
    'U': lambda w, q: w / q,
    'I': lambda q, t: q * t
}
print(physic.get('F')(5, 4)) 
print(physic.get('W')(3, 20)) 
print(physic.get('T')(2)) 
print(physic.get('P')(27, 9)) 
print(physic.get('U')(100, 4)) 
print(physic.get('I')(7, 15)) 


# Sual 2
# Lambda ilə factorial hesablayan recursive function hazırlayın.

factorial = lambda n: n if n == 1 else n * factorial(n-1)


# Sual 3
# Dictionary datalarını düzləşdirən bir recursive funksiya hazırlayın. Örnək:
# letdict = {'a': 1, 'v': {'b': 2}, 'c': {'f': 3, 'c': 3, 'h': {'r': 5}, 'p': 3}, 'y': 9} 

def unnest_dict(d):
    result = {}
    for k,v in d.items():
        if isinstance(v, dict):
            result.update(unnest_dict(v))
        else:
            result[k] = v
    return result