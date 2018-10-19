# Alexis Mendoza Valencia
# A01631994

# --------------------------------Problema numero 1 -------------------------------------------
"""
Calcular el área de un triángulo rectángulo que tiene las siguientes características:
su perímetro es igual a 24 unidades,
el triple del cateto mayor es cuatro veces el cateto menor y
la suma del cateto mayor más el doble del menor es dos veces la hipotenusa.
x: cateto mayor
y: cateto menor
z: hipotenusa
"""
# x + y + z = 24
# 3x = 4y
# x + 2y = 2z

#  x +  y +  z = 24
# 3x - 4y +  0 = 0
#  x + 2y - 2z = 0


def create_matrix(columns, rows, value):
    new_list = []
    for row in range(columns):
        new_list.append([value]*rows)
    return new_list


def get_dimension(A):
    return len(A), len(A[0])


def sum_matrices(A, B):
    Am, An = get_dimension(A)
    Bm, Bn = get_dimension(B)
    if Am != Bm or An != Bn:
        print("Las dimensiones son diferentes")
        return []

    C = create_matrix(Am, An, 0)
    for i in range(Am):
        for j in range(An):
            C[i][j] = A[i][j] + B[i][j]

    return C


def matrix_multiplication(A, B):
    am, an = get_dimension(A)
    bm, bn = get_dimension(B)
    if an != bm:
        print("Las matrices no son conformables")
        return []

    C = create_matrix(am, bn, 0)
    for i in range(am):
        for j in range(bn):
            for k in range(an):
                C[i][j] += A[i][k] * B[k][j]

    return C


def get_minor_matrix(A, r, c):
    m, n = get_dimension(A)
    C = create_matrix(m - 1, n - 1, 0)
    for i in range(m):
        if i == r:
            continue
        for j in range(n):
            if j == c:
                continue
            ci = i
            if i > r:
                ci = i - 1
            cj = j
            if j > c:
                cj = j - 1
            C[ci][cj] = A[i][j]
    return C


def det_matrix(A):
    m, n = get_dimension(A)
    if m != n:
        print("La matriz no es cuadrada")
        return -1

    if m == 1:
        return m

    if m == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    det = 0
    for j in range(n):
        det += (-1) ** j * A[0][j] * det_matrix(get_minor_matrix(A, 0, j))

    return det


def get_ady_matrix(A):
    m, n = get_dimension(A)
    c = create_matrix(m, n, 0)
    for i in range(m):
        for j in range(n):
            c[i][j] = (-1) ** (i + j) * det_matrix(get_minor_matrix(A, i, j))

    return c


def get_trans_matrix(A):
    m, n = get_dimension(A)
    c = create_matrix(n, m, 0)
    for i in range(m):
        for j in range(n):
            c[j][i] = A[i][j]
    return c


def get_inverse(A):
    det_a = det_matrix(A)
    if det_a == 0:
        print("La matriz no tiene inversa")
        return -1

    at = get_trans_matrix(A)
    ady_at = get_ady_matrix(at)
    m, n = get_dimension(A)
    c = create_matrix(m, n, 0)
    for i in range(m):
        for j in range(n):
            c[i][j] = (1 / det_a) * ady_at[i][j]

    return c


def direct(A, C):
    return matrix_multiplication(get_inverse(A), C)

#  x +  y +  z = 24
# 3x - 4y +  0 = 0
#  x + 2y - 2z = 0


A = create_matrix(3, 3, 0)
A[0] = [1,  1,  1]
A[1] = [3, -4,  0]
A[2] = [1,  2, -2]

C = create_matrix(3, 1, 0)
C[0] = [24]
C[1] = [0]
C[2] = [0]

print("\nEjercicio 1:")
B = direct(A, C)
print("Cateto mayor: ", B[0][0])
print("Cateto menor: ", B[1][0])
print("Hipotenusa:   ", B[2][0])

# --------------------------------Problema numero 2 -------------------------------------------
def find_lu(l, u):
    for I in range(3):
        a = u[I][I]
        if a == 0:
            print("La matriz no tiene LU")
            break

        for J in range(I + 1, 3):
            b = u[J][I]
            c = -1 * b / a
            l[J][I] = -1 * c
            t = create_matrix(1, 3, 0)
            for k in range(3):
                t[0][k] = c * u[I][k]

            for k in range(3):
                u[J][k] += t[0][k]


def z_value(z, c, l):
    for row in range(3):
        z[row][0] = c[row][0]
        for column in range(3):
            if row == column:
                break
            z[row][0] -= l[row][column] * z[column][0]


def b_value(b, z, u):
    for i in range(2, -1, -1):
        b[i][0] = z[i][0]
        for j in range(2, -1, -1):
            if i == j:
                b[i][0] = b[i][0] / u[i][j]
                break

            b[i][0] -= u[i][j] * b[j][0]


def factorization_lu(u, c):
    z = create_matrix(3, 1, 0)
    b = create_matrix(3, 1, 0)
    list_l = create_matrix(3, 3, 0)
    list_l[0] = [1, 0, 0]
    list_l[1] = [0, 1, 0]
    list_l[2] = [0, 0, 1]
    find_lu(list_l, u)
    z_value(z, c, list_l)
    b_value(b, z, u)
    return b


"""
Descripcion del problema 2: 

La empresa TEC construirá tres tipos de viviendas: 
sencilla, normal y de lujo. En un mes se construyen 
20 viviendas. En la zona norte se tienen 2 proyectos 
para la construcción de tipo sencillas y uno para 
viviendas normales, en total se construirán 27 casas 
habitación. En la zona sur se tiene un proyecto para 
la construcción de casas sencillas y tres proyectos 
para la construcción de casas de lujo, en total 
construirán 19 viviendas. ¿Cuántas viviendas de cada 
tipo se construirán en el mes en dicha empresa?
x: sencillas
y: normales
z: de lujo
"""
#  x + y +  z = 20
# 2x + y +  0 = 27
#  x + 0 + 3z = 19

U = create_matrix(3, 3, 0)
U[0] = [1,  1,  1]
U[1] = [2,  1,  0]
U[2] = [1,  0,  3]

C = create_matrix(3, 1, 0)
C[0] = [20]
C[1] = [27]
C[2] = [19]

print("\nEjercicio 2: ")
b = factorization_lu(U, C)
print("Sencillas: ", b[0][0])
print("Normales:  ", b[1][0])
print("De lujo:   ", b[2][0])


# --------------------------------Problema numero 3 -------------------------------------------
def gaussian_elimination(MA):
    for i in range(3):
        pivot = MA[i][i]
        if pivot == 0:
            for j in range(i + 1, 3):
                if MA[j][i] != 0:
                    T = MA[j]
                    MA[j] = MA[i]
                    MA[i] = T
                    pivot = MA[i][i]
                    break

        for k in range(4):
            MA[i][k] = (1 / pivot) * MA[i][k]

        for j in range(i + 1, 3):
            C = -1 * MA[j][i]
            T = create_matrix(1, 4, 0)
            for k in range(4):
                T[0][k] = C * MA[i][k]

            for k in range(4):
                MA[j][k] += T[0][k]

    B = create_matrix(3, 1, 0)
    for i in range(2, -1, -1):
        B[i][0] = MA[i][3]
        for j in range(2, -1, -1):
            if i == j:
                break

            B[i][0] -= MA[i][j] * B[j][0]
    return B


"""
Descripcion del problema 3: 

Hugo, Paco y Luis tienen diferentes cantidades de dinero.
Paco tiene tres veces lo que tiene Hugo más $100.00,
Luis tiene el doble de lo que tiene Paco quitándole $200.00
a dicha cantidad, y entre todos reúnen $1,100.00. 
¿Cuánto dinero tiene cada uno?

Hugo = x
Paco = y
Luis = z
"""
# y = 3x + 100
# z = 2y - 200
# - 3x +  y + 0 =  100
#    0 + 2y - z =  200
#    x +  y + z = 1100

MA = create_matrix(3, 4, 0)
MA[0] = [-3, 1,  0, 100]
MA[1] = [0,  2, -1, 200]
MA[2] = [1,  1,  1, 1100]

print("\nEjercicio 3:")
MA = gaussian_elimination(MA)
print("Hugo:", MA[0][0].__round__(3))
print("Paco:", MA[1][0].__round__(3))
print("Luis:", MA[2][0].__round__(3))


# --------------------------------Problema numero 4 -------------------------------------------
"""
Obtener los valores de los coeficientes a , b, y c, de tal forma que los puntos dados 
en la tabla pertenezcan a la gráfica del polinomio.
x = 1.0  -->  p(x) = 16
x = 1.5  -->  p(x) = 16.5
x = 2.0  -->  p(x) = 16
"""
# ax^2 + bx + c
#     a +    b + c = 16
# 2.25a + 1.5b + c = 16.5
#    4a +   2b + c = 16


print("\nEjercicio 4:")
print("No se puede utilizar el método Gauss-Seidel, porque"
      " los valores de la diagonal no son correctos.\n"
      "Se intentara utilizar el método de matriz inversa")

A = create_matrix(3, 3, 0)
A[0] = [1, 1, 1]
A[1] = [2.25, 1.5, 1]
A[2] = [4, 2, 1]

B = create_matrix(3, 1, 0)
B[0] = [16]
B[1] = [16.5]
B[2] = [16]

values = direct(A, B)
print("a:", values[0][0])
print("b:", values[1][0])
print("c:", values[2][0])


# --------------------------------Problema numero 5 -------------------------------------------
"""
Gabriela (la panadera) vendió 120 piezas de pan entre pan de muerto, panqués y cocoles, 
la suma de los panes de muerto más los panqués es el doble que los cocoles; 
los panes de muerto y los cocoles cuestan 3 pesos y los panqués 5 pesos. 
Si lo que se juntó fueron 420 pesos, 
¿cuántos panes fueron de cada uno?
x: pan de muerto
y: panques
z: cocoles
"""
# 3x + 5y + 3z = 420
#  x +  y - 2z = 0
#  x +  y +  z = 120

panes = create_matrix(3, 4, 0)
panes[0] = [3, 5, 3, 420]
panes[1] = [1, 1, -2, 0]
panes[2] = [1, 1, 1, 120]

print("\nEjercicio 5:")
panes = gaussian_elimination(panes)
print("Pan de muerto:", panes[0][0].__round__(3))
print("Panqués:      ", panes[1][0].__round__(3))
print("Cocoles:      ", panes[2][0].__round__(3))


# --------------------------------Problema numero 6 -------------------------------------------
"""
Se va a determinar la edad de tres niños, Antonio, Brenda y Cinthia.
Considerando que la suma de las edades de Antonio y Brenda es igual a la edad de Cinthia más tres años,
que la suma de las edades de Antonio y Cinthia es 17 años, y 
que la suma del doble de la edad de Brenda más la edad de Cinthia es igual a 22 años, 
¿qué edad tiene cada niño? 
x: Antonio
y: Brenda
z: Cinthia
"""
# x + y = z + 3
# x + z = 17
# 2y + z = 22

# x +  y - z = 3
# x +  0 + z = 17
# 0 + 2y + z = 22

ages = create_matrix(3, 3, 0)
ages[0] = [1,  1, -1]
ages[1] = [1,  0,  1]
ages[2] = [0,  2,  1]

results = create_matrix(3, 1, 0)
results[0] = [3]
results[1] = [17]
results[2] = [22]

print("\nEjercicio 6:")
kids_ages = direct(ages, results)
print("Antonio: ", kids_ages[0][0].__round__())
print("Brenda : ", kids_ages[1][0].__round__())
print("Cinthia: ", kids_ages[2][0].__round__())


# --------------------------------Problema numero 7 -------------------------------------------
"""
Rebeca vende cosméticos. Entre lunes, martes y miércoles vendió 20 productos.
El lunes vendió 5 productos más que el martes.
El miércoles vendió 4 productos más que el lunes.
¿Cuántos productos vendió cada día Rebeca?
x: lunes
y: martes
z: miercoles
"""
# x + y + z = 20
# x = y + 5
# z = x + 4

# x + y + z = 20
# x - y + 0 = 5
# -x + 0 + z = 4

A = create_matrix(3, 3, 0)
A[0] = [1,  1,  1]
A[1] = [1, -1,  0]
A[2] = [-1,  0, 1]

C = create_matrix(3, 1, 0)
C[0] = [20]
C[1] = [5]
C[2] = [4]

print("\nEjercicio 7:")
results = direct(A, C)
print("Lunes:     ", results[0][0].__round__())
print("Martes :   ", results[1][0].__round__())
print("Miercoles: ", results[2][0].__round__())

# --------------------------------Problema numero 8 -------------------------------------------
"""
Luis necesita componentes electrónicos para su proyecto escolar.
El capacitor cuesta 15 pesos, el diodo 20 pesos y la resistencia 5 pesos. 

El número de resistencias que necesita es el doble del número de los capacitores.
El número de diodos que requiere es el triple que el número de las resistencias menos el doble 
    del número de los capacitores. 
En total gastó 210 pesos. 
Determinar ¿cuántos componentes de cada tipo compró? 
x: capacitor
y: diodo
z: resistencia
"""
# z = 2x
# y = 3z - 2x
# 15x + 20y + 5z = 210

#  2x +   0 -  z = 0
# 15x + 20y + 5z = 210
# -2x -   y + 3z = 0


def get_x(y, z):
    return z / 2


def get_y(x, z):
    return (210 - 15*x - 5*z) / 20


def get_z(x, y):
    return (y + 2*x) / 3


def err(real, new):
    return (real - new) / real


def gauss_seidel():
    x = 1
    y = 1
    z = 1
    error_x = 0.00001
    error_y = 0.00001
    error_z = 0.00001
    error = 0.0000000000000001

    for i in range(100):
        x = get_x(y, z)
        y = get_y(x, z)
        z = get_z(x, y)

        #Errores
        if abs(err(error_x, x)) < error and abs(err(error_y, y)) < error and abs(err(error_z, z) < error):
            return [x, y, z]
        error_x = x
        error_y = y
        error_z = z
    return [x, y, z]


print("\nEjercicio 8:")
cant_components = gauss_seidel()
print("Capacitores: ", cant_components[0])
print("Diodos:      ", cant_components[1])
print("Resistencias:", cant_components[2])

# --------------------------------Problema numero 9 -------------------------------------------
"""
Un rectángulo tiene 40 cm2 de área y su diagonal es de 10 cm. 
Halla las dimensiones del rectángulo.
"""
# x*y = 40
# x^2 + y^2 = 100


def subtraction_matrix(matrix_a, matrix_b):
    am, an = get_dimension(matrix_a)
    bm, bn = get_dimension(matrix_b)
    if am != bm or an != bn:
        print("Error las dimensiones deben ser iguales")
        return []
    c = create_matrix(am, an, 0)
    for i in range(am):
        for j in range(an):
            c[i][j] = matrix_a[i][j] - matrix_b[i][j]
    return c


def u(x, y):
    return x*y - 40


def v(x, y):
    return (x**2 + y**2)**(1/2) - 10


def du_dx(x, y):
    return y


def du_dy(x, y):
    return x


def dv_dx(x, y):
    return (2*x) / (2 * (x**2 + y**2)**(1/2))


def dv_dy(x, y):
    return (2 * y) / (2 * (x ** 2 + y ** 2) ** (1 / 2))


def newton_raphson():
    jacobi = [[du_dx, du_dy], [dv_dx, dv_dy]]
    function_evaluated = [[u], [v]]
    values = [[5], [8]]
    error = 0.0001
    for i in range(100):
        Ji = create_matrix(2, 2, 0)
        Jin, Jim = get_dimension(Ji)
        for k in range(Jin):
            for j in range(Jim):
                Ji[k][j] = jacobi[k][j](values[0][0], values[1][0])
        Jinv = get_inverse(Ji)
        Fi = create_matrix(2, 1, 0)
        for k in range(2):
            Fi[k][0] = function_evaluated[k][0](values[0][0], values[1][0])
        Bi = subtraction_matrix(values, matrix_multiplication(Jinv, Fi))
        Be = subtraction_matrix(values, Bi)
        if abs(Be[0][0]) < error and abs(Be[1][0] < error):
            values = Bi
            return values
        values = Bi


print("\nEjercicio 9:")
x_y = newton_raphson()
print("x:", x_y[0][0])
print("y:", x_y[1][0])


# --------------------------------Problema numero 9 -------------------------------------------
"""
Calcular el vector x(k) de la iteración k-ésima cuando k=4 si se utiliza el método de Newton-Raphson 
en la resolución del sistema no lineal: 
 x1   −  x2   +  x3   − x1*x4 = 0, 
−x1   + 3x2   − 2x3   − x2*x4 = 0, 
 x1   − 2x2   + 3x3   − x3*x4 = 0, 
 x1^2 +  x2^2 +  x3^2 +     0 = 1, 
tomando x(0) = [1,1,1,1]. 
Calcular en cada iteración k el valor de la estimación del error absoluto ||e(k)|| = || x(k-1) − x(k) ||
"""


def da_dx1(x1, x2, x3, x4):
    return 1 - x4


def da_dx2(x1, x2, x3, x4):
    return -1


def da_dx3(x1, x2, x3, x4):
    return 1


def da_dx4(x1, x2, x3, x4):
    return -x1


def db_dx1(x1, x2, x3, x4):
    return -1


def db_dx2(x1, x2, x3, x4):
    return 3 - x4


def db_dx3(x1, x2, x3, x4):
    return -2


def db_dx4(x1, x2, x3, x4):
    return -x2


def dc_dx1(x1, x2, x3, x4):
    return 1


def dc_dx2(x1, x2, x3, x4):
    return -2


def dc_dx3(x1, x2, x3, x4):
    return 3 - x4


def dc_dx4(x1, x2, x3, x4):
    return -x3


def dd_dx1(x1, x2, x3, x4):
    return 2*x1


def dd_dx2(x1, x2, x3, x4):
    return 2*x2


def dd_dx3(x1, x2, x3, x4):
    return 2*x3


def dd_dx4(x1, x2, x3, x4):
    return 0


def func_a(x1, x2, x3, x4):
    return x1 - x2 + x3 - x1 * x4


def func_b(x1, x2, x3, x4):
    return -x1 + 3*x2 - 2*x3 - x2 * x4


def func_c(x1, x2, x3, x4):
    return x1 - x2 + x2 - x3 * x4


def func_d(x1, x2, x3, x4):
    return x1**2 + x2**2 + x3**2 - 1


def newton_raphson_2():
    jacobi = [[da_dx1, da_dx2, da_dx3, da_dx4],
              [db_dx1, db_dx2, db_dx3, db_dx4],
              [dc_dx1, dc_dx2, dc_dx3, dc_dx4],
              [dd_dx1, dd_dx2, dd_dx3, dd_dx4]]
    function_evaluated = [[func_a], [func_b], [func_c], [func_d]]
    B = [[1], [1], [1], [1]]
    error = 0.01

    for i in range(5):
        Ji = create_matrix(4, 4, 0)
        Jin, Jim = get_dimension(Ji)
        for k in range(Jin):
            for j in range(Jim):
                Ji[k][j] = jacobi[k][j](B[0][0], B[1][0], B[2][0], B[3][0])
        Jinv = get_inverse(Ji)
        Fi = create_matrix(4, 1, 0)
        for k in range(4):
            Fi[k][0] = function_evaluated[k][0](B[0][0], B[1][0], B[2][0], B[3][0])
        Bi = subtraction_matrix(B, matrix_multiplication(Jinv, Fi))
        Be = subtraction_matrix(B, Bi)
        print("Error k = %d" % i, err(B[3][0], Be[3][0]))
        if abs(Be[0][0]) < error and abs(Be[1][0]) < error and abs(Be[2][0]) < error and abs(Be[3][0]) < error:
            B = Bi
            break
        B = Bi


print("\nEjercicio 10:")
newton_raphson_2()