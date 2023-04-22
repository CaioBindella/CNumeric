import math

def Calc(x):
    return ((x**4) - (14*(x**2)) + 24*(x) - 10)

def Fake(a, b, epsilon, max_iter):
    x_k_1 = a
    x_k = b
    count = 0
    
    while abs(Calc(x_k)) > epsilon and count < max_iter:
        x_k_2 = x_k - (Calc(x_k) * (x_k - x_k_1)) / (Calc(x_k) - Calc(x_k_1))
        x_k_1 = x_k
        x_k = x_k_2
        count += 1
    
    if count == max_iter:
        print("Não foi possível encontrar uma raiz dentro do número máximo de iterações")
    else:
        print(f"A raiz é: {x_k} após {count} iterações")

a = float(input('Entre com o valor 1: '))
b = float(input('Entre com o valor 2: '))
epsilon = float(input('Entre com o valor E: '))
max_iter = int(input('Entre com o número máximo de iterações: '))

Fake(a, b, epsilon, max_iter)
