# Operadores Lógicos
a = 50
b = 40

if a < b:
    print('A es menor que B')
elif a == b:
    print('A es igual a B')
else:
    print('A es mayor que B')

print('---------')

# Bucle While
contador = 1;
while contador <=10:
    print('Contador es: ', contador)
    contador += 1

print('---------')

# Par o Impar
contador = 1
while contador <= 10:
    if contador % 2 == 0:
        print(contador, ' Es par')
    else:
        print(contador, ' Es impar')
    contador +=1
    
print('---------')

# Bucle For
lista = [1, 2, 3, 4]

for value in lista:
    print(value)

print('---------')

# La utilización del break es importante
palabras = ['Hola', 'Mensaje', 'Chau']

for palabra in palabras:
    if palabra == 'Mensaje':
        print('Palabra encontrada!')
        break
else:
    print('Palabra no encontrada.')

print('---------')

# Match Case (Switch)

valor = 4

match valor:
    case 1:
        print('El valor es 1')
    case 2:
        print('El valor es 2')
    case 3:
        print('El valor es 3')
    case 4:
        print('El valor es 4')