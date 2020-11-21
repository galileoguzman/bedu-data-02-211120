# Script que calcula la tabla de multiplicar de un número

# Solicitar numero al usuario por consola
numero = input('que numero quieres multiplicar?\t')
# El dato ingresado por el usuario es una cadena "<str>"
# Se debe convertir a numero "<int>" para poder multiplicar
numero = int(numero)

for n in range(10):
    r = numero * (n + 1)
    print(r)


# A continuación se muestra la tabla de multiplicar del número <numero>
# -----------------
# 8 * 1 = 8
# 8 * 2 = 16
# 8 * 3 = 24
# 8 * 4 = 32
# 8 * 5 = 40
# ...
