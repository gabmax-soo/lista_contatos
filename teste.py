pares = [x for x in range(10) if x % 2 == 0]

quadrados = [x ** 2 for x in range(10) ]

letras = ['A', 'B', 'C', 'D', 'E','F','G', 1,2,3,4]

print(pares)
print(quadrados)
print(letras)

number = 2
for i in range(1,11):
    print(f'{i} * {number} = {i*number}')

def first_arr(letras,number):
    return letras[:number]

print(first_arr(letras,number))

for letra in letras:
    if isinstance(letra,(int,float)):
        print(letra)