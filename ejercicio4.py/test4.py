from ej4 import MetodoBiseccion, MetodoSecante, MetodoNewtonRaphson

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

print("\nMétodo de la Secante:")
print("Solución:", solucion_secante)
print("Cantidad de iteraciones:", iteraciones_secante)

print("\nMétodo de Newton-Raphson:")
print("Solución:", solucion_newton_raphson)
print("Cantidad de iteraciones:", iteraciones_newton_raphson)
