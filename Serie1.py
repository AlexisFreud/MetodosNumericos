import math
"""
Aplique el método de bisección para encontrar las aproximaciones
de las raíces de la ecuación,
con un error de < 0.0001, considerando los intervalos

Funcion
 x^3 - 7x^2 + 14x - 6 = 0

 Intervalos
[0, 1]
[1, 3.2]
[3.2, 4]
"""
def funBiseccion(x):
    return x ** 3 - 7*(x**2) + 14*x - 6

def biseccion(rangoInf, rangoSup):
    for i in range(100):
        fun0 = funBiseccion(rangoInf )
        fun1 = funBiseccion(rangoSup)
        if fun0*fun1 > 0:
            print("No existe raíz en el rango especificado")
            break
        raiz = (rangoInf+rangoSup)/2
        funRaiz = funBiseccion(raiz)
        if abs(funRaiz) < 0.0001:
            return raiz
        else:
            if funRaiz*fun1 > 0:
                rangoSup = raiz
            else:
                rangoInf = raiz
print("---------------------Bisección-----------------------\n",
      "Rango [0, 1]: %.4f\n" % biseccion(0, 1),
      "Rango [1, 3.2]: %.4f\n" % biseccion(1, 3.2),
      "Rango [3.2, 4]: %.4f\n" % biseccion(3.2, 4))

"""
Encontrar la raiz positiva de 10 con el método de falsa posicion
ErrorS = 0.5%
Valores iniciales:
xi = 3
xu = 3.2
"""

print("---------------------Falsa Posición-----------------------")
def funFalsaPosicion(x):
    return x**2 - 10

def falsaPosicion(x0, x1):
    for i in range(100):
        f0 = funFalsaPosicion(x0)
        f1 = funFalsaPosicion(x1)
        if f0*f1 > 0:
            print("Raiz no encontrada en el rango especificado")
            break
        x = x0 + ((f1*(x1-x0))/(f1-f0))
        fx = funFalsaPosicion(x)
        if(fx*f1<0):
            x0=x
        else:
            x1 = x
        if abs(fx) < 0.005:
            return x

print("Raiz de 10: %.3f"%falsaPosicion(3,3.2))


"""

"""
print("---------------------Newton-Raphson-----------------------")

def funNewton(x):
    return x**4 - 8.6*(x**3) - 33.51*(x**2) + 464*x - 998.46

def fPrima(x):
    return 4*(x**3) - 25.8*(x**2) - 67.02*x + 464

def newton(x):
    for i in range(100):
        Xr = x - (funNewton(x)/fPrima(x))
        if abs(funNewton(Xr)) < 0.001 :
            return Xr
        else:
            x = Xr
    print("Valor no encontrado")

print("Valor inicial x0 = 7. Raiz = %d"%newton(7))


print("---------------------Bairstow-----------------------")
def cuadratica(a,b,c):
    discriminante = b**2 - 4*a*c
    if discriminante > 0:
        rdiscriminante = math.sqrt(discriminante)
        x1 = (-b + rdiscriminante )/(2*a)
        x2 = (-b - rdiscriminante )/(2*a)
        return [(x1,0),(x2,0)]
    if discriminante == 0:
        x = -b / (2*a)
        return [(x,0),(x,0)]
    xr = -b / (2*a)
    xi = math.sqrt(abs(discriminante)) / (2*a)
    return [(xr,xi),(xr,-xi)]

def bn(a):
    return a[-1]
def bn1(a,b,r):
    return a[-2] + r*b
# [bn1, bn]
def bi(i,a,r,s,b):
    return a[i] + r*b[0] + s*b[1]

def cn(b):
    return bn(b)
def cn1(b,c,r):
    return bn1(b,c,r)
def ci(i,b,r,s,c):
    return bi(i,b,r,s,c)

def bairstow(lista):
    r = -1
    s = -1
    b = []
    a = []
    for i in lista:
        a.append(i)
    raices = []
    while True:
        for i in range(100):
            b = []
            c = []
            b.append(bn(a))
            b.insert(0, bn1(a, b[0], r))
            limit = len(a) - 2
            for i in reversed(range(0, limit)):
                b.insert(0, bi(i, a, r, s, b))

            c.append(cn(b))
            c.insert(0, cn1(b, c[0], r))
            for i in reversed(range(0, limit)):
                c.insert(0, ci(i, b, r, s, c))

            def deltaS(b, c):
                return ((-b[1] / c[2]) + (b[0] / c[1])) / ((c[3] / c[2]) - (c[2] / c[1]))

            def deltaR(b, c, dS):
                return (-b[0] / c[1]) - ((c[2] / c[1]) * dS)

            dS = deltaS(b, c)
            dR = deltaR(b, c, dS)

            if abs(dS) < 0.01 and abs(dR) < 0.01:
                break
            r = r + dR
            s = s + dS

        raices.insert(0, cuadratica(1, -r, -s))

        # Actualizar el siguiente polinomio
        a = b[2:]
        grade = len(a)
        if grade == 3:  # El polinomio es de grado 2
            raices.insert(0, cuadratica(a[2], a[1], a[0]))
            break
        if grade == 2:  # El polinomio es de grado 1
            raices.insert(0, -a[0] / a[1])
            break

    return raices

def imprimeBairstow(lista):
    raices = bairstow(lista)
    count = 1
    for raiz in raices:
        print("Raiz {} = {}".format(count, raiz))
        count+=1

imprimeBairstow([-998.46,464,-33.51,-8.6,1])
