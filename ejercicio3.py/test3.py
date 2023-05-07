from ej3 import RedFerrocarriles

# Crear la red de ferrocarriles
red = RedFerrocarriles()

# Cargar estaciones
estaciones = ['King\'s Cross', 'Waterloo', 'Victoria Train Station', 'Liverpool Street Station', 'St. Pancras']
red.cargar_estaciones(estaciones)

# Cargar desvíos
cantidad_desvios = 12
red.cargar_desvios(cantidad_desvios)

# Construir el grafo
red.construir_grafo()

# Encontrar el camino más corto
origen = 'King\'s Cross'
destino = 'Waterloo'
red.obtener_camino_mas_corto(origen, destino)

# Mostrar el camino más corto
print(f"Camino más corto desde {origen} hasta {destino}:")
vertice_actual = red.vertices[destino]
camino = [vertice_actual.nombre]
while vertice_actual.anterior:
    camino.append(vertice_actual.anterior.nombre)
    vertice_actual = vertice_actual.anterior
camino.reverse()
print(" -> ".join(camino))

# Encontrar el camino más corto
origen = 'Victoria Train Station'
destino = 'Liverpool Street Station'
red.obtener_camino_mas_corto(origen, destino)

# Mostrar el camino más corto
print(f"Camino más corto desde {origen} hasta {destino}:")
vertice_actual = red.vertices[destino]
camino = [vertice_actual.nombre]
while vertice_actual.anterior:
    camino.append(vertice_actual.anterior.nombre)
    vertice_actual = vertice_actual.anterior
camino.reverse()
print(" -> ".join(camino))

# Encontrar el camino más corto
origen = 'St. Pancras'
destino = 'King\'s Cross'
red.obtener_camino_mas_corto(origen, destino)

# Mostrar el camino más corto
print(f"Camino más corto desde {origen} hasta {destino}:")
vertice_actual = red.vertices[destino]
camino = [vertice_actual.nombre]
while vertice_actual.anterior:
    camino.append(vertice_actual.anterior.nombre)
    vertice_actual = vertice_actual.anterior
camino.reverse()
print(" -> ".join(camino))
