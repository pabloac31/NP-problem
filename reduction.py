import sys

entrada = input() # aquí es donde está la entrada
salida = ""       # aquí es donde está la salida

# Reducción:
# Contadores:
p = 0  # puntero de lectura
a = 0  # posicion de '#'
i = 1  # subconjunto
j = 1  # elemento del subconjunto
k = 0  # número de elementos

# Vértices
salida += "v "
while(entrada[p] != '#'):
    salida += entrada[p] + " "
    p+=1
a = p
p+=1
while(p < len(entrada)):
    salida += "c" + str(i) + " "
    for j in range(1,4):
        p+=1
    i+=1

# Aristas
salida += " # "
p = a+1
i = 1
while(p < len(entrada)-1):
    salida += "vc" + str(i) + " "
    for j in range(1,4):
        salida += "c" + str(i) + entrada[p] + " "
        p+=1
    i+=1

# R
salida += " # v "
p = 0
while(entrada[p] != '#'):
    salida += entrada[p] + " "
    p+=1
    k+=1

# K
salida += " # "
salida += str(int((k/3)) * 4)

print(salida)
