import heapq


class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


def generar_arbol_huffman(tabla_frecuencias):
    # Crear una cola de prioridad inicializada con los nodos hoja
    cola_prioridad = []
    for caracter, frecuencia in tabla_frecuencias.items():
        nodo = NodoHuffman(caracter, frecuencia)
        heapq.heappush(cola_prioridad, nodo)

    # Construir el árbol de Huffman combinando los nodos de menor frecuencia
    while len(cola_prioridad) > 1:
        nodo_izq = heapq.heappop(cola_prioridad)
        nodo_der = heapq.heappop(cola_prioridad)
        nodo_combinado = NodoHuffman(None, nodo_izq.frecuencia + nodo_der.frecuencia)
        nodo_combinado.izquierda = nodo_izq
        nodo_combinado.derecha = nodo_der
        heapq.heappush(cola_prioridad, nodo_combinado)

    # Devolver el nodo raíz del árbol de Huffman
    return cola_prioridad[0]


def generar_tabla_codigos(nodo_raiz, codigo_actual='', tabla_codigos={}):
    if nodo_raiz.caracter is not None:
        tabla_codigos[nodo_raiz.caracter] = codigo_actual
    else:
        generar_tabla_codigos(nodo_raiz.izquierda, codigo_actual + '0', tabla_codigos)
        generar_tabla_codigos(nodo_raiz.derecha, codigo_actual + '1', tabla_codigos)
    return tabla_codigos


def descomprimir_mensaje(mensaje_codificado, tabla_codigos):
    mensaje_descomprimido = ''
    codigo_actual = ''
    for bit in mensaje_codificado:
        codigo_actual += bit
        if codigo_actual in tabla_codigos:
            caracter = tabla_codigos[codigo_actual]
            mensaje_descomprimido += caracter
            codigo_actual = ''
    return mensaje_descomprimido


def calcular_tamano_mensaje(mensaje):
    # Utiliza 8 bits para representar cada carácter en el mensaje
    return len(mensaje) * 8


tabla_frecuencias = {
    'A': 11, 'B': 2, 'C': 4, 'D': 3, 'E': 14, 'G': 3, 'I': 6, 'L': 6, 'M': 3, 'N': 6,
    'O': 7, 'P': 4, 'Q': 1, 'R': 10, 'S': 4, 'T': 3, 'U': 4, 'V': 2, ' ': 17, ',': 2
}

# Generar el árbol de Huffman
arbol_huffman = generar_arbol_huffman(tabla_frecuencias)

# Generar la tabla de códigos a partir del árbol de Huffman
tabla_codigos = generar_tabla_codigos(arbol_huffman)
