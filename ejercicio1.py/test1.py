from ej1 import NodoHuffman

# Definir la tabla de frecuencias
tabla_frecuencias = {
    'A': 11,
    'B': 2,
    'C': 4,
    'D': 3,
    'E': 14,
    'G': 3,
    'I': 6,
    'L': 6,
    'M': 3,
    'N': 6,
    'O': 7,
    'P': 4,
    'Q': 1,
    'R': 10,
    'S': 4,
    'T': 3,
    'U': 4,
    'V': 2,
    ' ': 17,
    ',': 2
}

# Crear una instancia del árbol de Huffman
arbol_huffman = NodoHuffman()

# Generar el árbol de Huffman a partir de la tabla de frecuencias
arbol_huffman.generar_arbol(tabla_frecuencias)

# Imprimir el árbol de Huffman
print("Árbol de Huffman:")
arbol_huffman.imprimir_arbol()

# Mensaje 1 a descomprimir
mensaje_1 = "100010111010110000101110100011100000110110000001111001111010010110" \
            "000110100111001101000101110101111111010000111100111111001111010001100" \
            "011000000101101011110111111101110101101101110011101101111001111111001" \
            "010010100101000001011010110001011001101000111001001011000011001000110" \
            "101101010111111111110110111011100100001001010110001111111000100011101" \
            "100110010110100011011111010110100011011100000001110010010101000111111" \
            "00001100101101011100110011110100011000110000001011010111110011100"

# Mensaje 2 a descomprimir
mensaje_2 = "01101010110111001010001111010111001101110101101101000010001110101001" \
            "011110100111111101110010100011110101110011011101011000011000100110100" \
            "01110010010001100010110011001110010010000111101111010"

# Descomprimir los mensajes utilizando el árbol de Huffman
mensaje_descomprimido_1 = arbol_huffman.descomprimir(mensaje_1)
mensaje_descomprimido_2 = arbol_huffman.descomprimir(mensaje_2)

# Imprimir los mensajes descomprimidos
print("\nMensaje 1 descomprimido:")
print(mensaje_descomprimido_1)

print("\nMensaje 2 descomprimido:")
print(mensaje_descomprimido_2)
