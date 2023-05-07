import math

class MetodoBiseccion:
    def __init__(self, funcion, tolerancia=1e-6, max_iteraciones=100):
        self.funcion = funcion
        self.tolerancia = tolerancia
        self.max_iteraciones = max_iteraciones

    def calcular_raiz(self, a, b):
        iteraciones = 0
        while abs(b - a) > self.tolerancia and iteraciones < self.max_iteraciones:
            c = (a + b) / 2
            if self.funcion(a) * self.funcion(c) < 0:
                b = c
            else:
                a = c
            iteraciones += 1
        return c, iteraciones


class MetodoSecante:
    def __init__(self, funcion, tolerancia=1e-6, max_iteraciones=100):
        self.funcion = funcion
        self.tolerancia = tolerancia
        self.max_iteraciones = max_iteraciones

    def calcular_raiz(self, x0, x1):
        iteraciones = 0
        while abs(x1 - x0) > self.tolerancia and iteraciones < self.max_iteraciones:
            f_x0 = self.funcion(x0)
            f_x1 = self.funcion(x1)
            x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
            x0 = x1
            x1 = x2
            iteraciones += 1
        return x2, iteraciones


class MetodoNewtonRaphson:
    def __init__(self, funcion, derivada, tolerancia=1e-6, max_iteraciones=100):
        self.funcion = funcion
        self.derivada = derivada
        self.tolerancia = tolerancia
        self.max_iteraciones = max_iteraciones

    def calcular_raiz(self, x0):
        iteraciones = 0
        while abs(self.funcion(x0)) > self.tolerancia and iteraciones < self.max_iteraciones:
            x1 = x0 - self.funcion(x0) / self.derivada(x0)
            x0 = x1
            iteraciones += 1
        return x1, iteraciones


# Definir la función, su derivada y crear instancias de los métodos
def funcion(x):
    return x**3 + x + 16

def derivada(x):
    return 3*x**2 + 1

metodo_biseccion = MetodoBiseccion(funcion)
metodo_secante = MetodoSecante(funcion)
metodo_newton_raphson = MetodoNewtonRaphson(funcion, derivada)

# Calcular las soluciones y la cantidad de iteraciones para cada método
solucion_biseccion, iteraciones_biseccion = metodo_biseccion.calcular_raiz(-10, 10)
solucion_secante, iteraciones_secante = metodo_secante.calcular_raiz(-10, 10)
solucion_newton_raphson, iteraciones_newton_raphson = metodo_newton_raphson.calcular_raiz(10)

# Mostrar los resultados
print("Método de la Bisección:")
print("Solución:", solucion_biseccion)
print("Cantidad de iteraciones:", iteraciones_biseccion)