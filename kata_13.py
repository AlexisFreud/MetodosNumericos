# y' = 2xy
# y(1) = 1
# Find y(1.5)

def y_prime(x, y):
    return 2*x*y


def metodo_euler(function_f, x0, y0, x_limit, h):
    y = 0
    limit = (int)((x_limit - x0) / h)
    for i in range(limit):
        y = y0 + h*(function_f(x0, y0))
        y0 = y
        x0 += h
    return y


print("Caso 1: h = 0.1")
result = metodo_euler(y_prime, 1, 1, 1.5, 0.1)
print("Resultado:", result)


print("\nCaso 1: h = 0.1")
result = metodo_euler(y_prime, 1, 1, 1.5, 0.05)
print("Resultado:", result)
