import math

a = float(input('Entre com o valor 1: '))
b = float(input('Entre com o valor 2: '))
epislon = float(input('Entre com o valor E: '))

count = 0
tol = 0

def Calc(x):
    return ((x**3) - 7*(x**2) + 14*(x) - 6)

# def Interacoes( y, z, E):
#     return (((math.log(y*z)) - math.log(E))/math.log(2))

def CalcTol(x, y):
    return (abs(y - x)) 
    

inter = 0
f_a = Calc(a)
f_b = Calc(b)

tol = CalcTol(a, b)

while(tol > epislon):
    #Calcula xn
    x_n = (b + a)/2
    #Calcula f xn
    f_x_n = Calc(x_n)

    if(((f_x_n) * (f_a)) < 0):
        b = x_n
    else:
        a = x_n

    inter = inter + 1
    tol = CalcTol(a, b)        

print(f'Range of possible solutions: [{a:.4f}, {b:.4f}]')
print(f'Total of iterations: {inter:.1f}')


