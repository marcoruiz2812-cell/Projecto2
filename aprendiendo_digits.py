import math
from sklearn import datasets

misdatos = datasets.load_digits()

X= misdatos.data
y= misdatos.target

data = np.loadtxt("numeros.csv", delimiter=",")

digitos = []
buffer = []
for fila in data:
    if np.all(fila == 0):
        if len(buffer) > 0:
            digitos.append(np.array(buffer))
            buffer = []
    else:
        buffer.append(fila)
if len(buffer) > 0:
    digitos.append(np.array(buffer))

#Flatten
vectores = [mat.flatten() for mat in digitos]


def distancia_eucli(a,b):
    suma= 0
    for i in range(len(a)):
        suma += (a[i]-b[i])**2
    return math.sqrt(suma)

distancias=[]
for i in range(len(X)):
    d= distancia_eucli(nose, X[i])
    distancias.append(d)
