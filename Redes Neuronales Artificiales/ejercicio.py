import random
from math import e, pow

# Funcion Sigmoide
def sigmoide(z):
    return 1/(1+pow(e, -z))

# Peso sinaptico
def p_sinaptico():
    return random.randint(0, 100)/100

# Calculo inicial
def calcular(entrada, pesos):
    suma = 0
    for i in range(len(entrada)):
        suma += entrada['x'+str(i+1)] * pesos['w'+str(i+1)]
    return suma


entrada = {'x1': 5, 'x2': 8, 'x3': 4}
peso_sinaptico = {}
umbral = 0.5

for i in range(len(entrada)):
    peso_sinaptico['w'+str(i+1)] = p_sinaptico()

func_sigmoide = sigmoide(calcular(entrada, peso_sinaptico))

print('Entrada =', entrada)
print('Peso Sinaptico =', peso_sinaptico)
print('Funcion sigmoide =', func_sigmoide)
print('Calculo inicial =', calcular(entrada, peso_sinaptico))
print('----------------------------------------')
if func_sigmoide >= umbral:
    print('salida:', 1)
else:
    print('salida:', 0)
