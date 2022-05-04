# Dictionary Comprehension vasitesile qiymeti 3 azn-den asaqi olan mehsullarin 3 qat bahalasdir
pr = {"sud": 2, "corek": 1, "cipsi": 5, "cola": 4} 

new_pr = {key: value * 3 if value < 3 else value for key, value in pr.items()}

print(new_pr)


# Comprehension vasitesile 100-e qeder 3 ve 5 bolunen edeleri goster
fizzbuzz = [ num for num in range(1,100) if num % 3 == 0 if num % 5 == 0 ]
print(fizzbuzz)


# Comprehension vasitesile 20-e qeder olan ededleri tekdirse TEK cutdurse CUT yazdir
number = [ "Cut" if x % 2 == 0 else "Tek" for x in range(1,20) ]
print(*number)

# Comprehension vasitesile 20-e qeder olan CUT ededleri goster
number = [ x for x in range(1,20) if x % 2 ==0 ]
print(*number)


# Cumlede en cox isledilen characteri tap
sentence = "dlksajlksssssssssssssssssshsfkdhjkds"

char_count = {}
for char in sentence:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
        
char_count_sorted = sorted(char_count.items(), key = lambda item : item[1], reverse = True )        
        
print(char_count_sorted[0])       


# string metodlarini alt-alta sirala
print(*[methods for methods in dir(str) if not methods.startswith("__")], sep="\n")

