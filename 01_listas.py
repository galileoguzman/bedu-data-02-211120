# Archivo explicando listas

numeros = [23, 89, 127, 1289, 8912]
print(numeros)

# Para agregar un elemento a una lista ocupamos append

numero_extra = 33
numero_extra_dos = 1223
numero_extra_tres = 89

nueva_list = [numero_extra, numero_extra_dos, numero_extra_tres]

numeros = numeros + nueva_list

numeros.append(numero_extra)
print(numeros)

# Para eliminar el ultimo elemento de una lista ocupamos pop
numeros.pop()
print(numeros)
