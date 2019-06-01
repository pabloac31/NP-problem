import sys

entrada = input()

elementos = entrada[:entrada.find("#")]
subconjuntos = entrada[entrada.find("#")+1:]
X = elementos.split()
Y = subconjuntos.split()
C = []
for i in range(0,int(len(Y)/3)):
    C.append(Y[3*i:3*i+3])

V = ["v"]
for i in range(0,len(C)):
    V.append("c" + str(i))
V += X

E = []
for i in range(0,len(C)):
    E.append("(v,c" + str(i) + ")")
    for j in range(0,3):
        E.append("(c" + str(i) + ",x" + C[i][j] + ")")

R = ["v"]
R += X

K = int(4*len(X)/3)

# Salida
for i in range(0,len(C)):
    print("C" + str(i) + " = " + str(C[i]))

print("V = " + str(V))
print("E = " + str(E))
print("R = " + str(R))
print("K = " + str(K))


