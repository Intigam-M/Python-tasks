questions = [
    {
        'question': 'Asagidakilardan hansi bitkiler alemine aiddir?',
        'options': ['Ordek', 'Gobelek', 'At', 'Sam agaci'],
        'answer': 3
    },
    {
        'question': 'Bunlardan hansi saitdir',
        'options': ['b', 'a', 'c', 'd'],
        'answer': 1
    },
    {
        'question': 'En boyuk materik hansidir',
        'options': ['Antarktika', 'Avstraliya', 'Avrasiya', 'Simali Amerika'],
        'answer': 2
    },
    {
        'question': 'Azerbaycan Respublikasi ne vaxt yaranib?',
        'options': ['1928', '1918', '1500', '1930'],
        'answer': 1
    },
    {
        'question': 'Quvvetin vahidi?',
        'options': ['Newton', 'Vold', 'Watt', 'Metr'],
        'answer': 0
    },
    {
        'question': 'Asagidakilardan hansi radioaktivdir?',
        'options': ['Plutonium', 'Cive', 'Lithium', 'Cupper'],
        'answer': 0
    },
    {
        'question': 'Bextiyar Vahabzedenin ilk seiri',
        'options': ['Leyli ve Mecnun', 'Latin dili', 'Ana ve Sekil', '20 yanvar'],
        'answer': 2
    },
    {
        'question': 'sin90 nece edir?',
        'options': ['1', '2', '3', '4'],
        'answer': 0
    },
]

variants = {"A":0, "B":1, "C":2, "D":3, "E":4}

sual_count = 1
duzgun_cavablar = 0
for sual in questions:
    
    print(str(sual_count)+".", sual['question'],  end="\n\n")
    print(list(variants.keys())[0]+")", sual['options'][0], end = "\n")
    print(list(variants.keys())[1]+")", sual['options'][1], end = "\n")
    print(list(variants.keys())[2]+")", sual['options'][2], end = "\n")
    print(list(variants.keys())[3]+")", sual['options'][3], end = "\n\n")

    cavab = input("Cavab yazin:\n").upper()

    if cavab in variants:
        if variants[cavab] == sual['answer']:
            duzgun_cavablar +=1
            print("Cavab Doqrudur!\n")
        else:
            print(f"Cavab yanlisdir! Duzgun cavab {list(variants.items())[sual['answer']][0]} variantidir\n")
    else:
     print(f"Cavab yanlisdir! Duzgun cavab {list(variants.items())[sual['answer']][0]} variantidir\n")
    
    print("-" *70, end = "\n\n")    
    sual_count+=1
        
        
print("Duzgun cavab sayi", duzgun_cavablar)



