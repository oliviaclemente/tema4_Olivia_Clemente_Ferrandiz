import heapq


class Vertice:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.vecinos = []
        self.distancia = float('inf')
        self.visitado = False
        self.anterior = None

    def agregar_vecino(self, vecino, peso):
        self.vecinos.append((vecino, peso))


class Estacion(Vertice):
    def __init__(self, nombre):
        super().__init__(nombre, 'estacion')


class Desvio(Vertice):
    def __init__(self, nombre):
        super().__init__(nombre, 'desvio')


class RedFerrocarriles:
    def __init__(self):
        self.vertices = {}

    def cargar_estaciones(self, nombres_estaciones):
        for nombre in nombres_estaciones:
            estacion = Estacion(nombre)
            self.vertices[nombre] = estacion

    def cargar_desvios(self, cantidad_desvios):
        for i in range(1, cantidad_desvios + 1):
            nombre = str(i)
            desvio = Desvio(nombre)
            self.vertices[nombre] = desvio

    def conectar_vertices(self, nombre_vertice1, nombre_vertice2, peso):
        vertice1 = self.vertices[nombre_vertice1]
        vertice2 = self.vertices[nombre_vertice2]
        vertice1.agregar_vecino(vertice2, peso)
        vertice2.agregar_vecino(vertice1, peso)

    def construir_grafo(self):
        self.conectar_vertices('King\'s Cross', 'Waterloo', 1)
        self.conectar_vertices('Victoria Train Station', 'Liverpool Street Station', 2)
        self.conectar_vertices('St. Pancras', 'King\'s Cross', 3)

        # Conectar estaciones y desvíos
        for nombre, vertice in self.vertices.items():
            if vertice.tipo == 'estacion':
                vecinos = [v for v in self.vertices.values() if v.nombre != nombre and v.tipo != 'estacion']
                for vecino in vecinos:
                    vertice.agregar_vecino(vecino, 1)

    def dijkstra(self, origen, destino):
        heap = [(0, origen)]
        origen.distancia = 0

        while heap:
            distancia_actual, vertice_actual = heapq.heappop(heap)

            if vertice_actual == destino:
                break

            if distancia_actual > vertice_actual.distancia:
                continue

            for vecino, peso in vertice_actual.vecinos:
                distancia = distancia_actual + peso

                if distancia < vecino.distancia:
                    vecino.distancia = distancia
                    vecino.anterior = vertice_actual
                    heapq.heappush(heap, (distancia, vecino))

    def obtener_camino_mas_corto(self, origen, destino):
        self.dijkstra(self.vertices[origen], self.vertices[destino])

       
