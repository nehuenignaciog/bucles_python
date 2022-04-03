# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos con bucles "for"

# Dado la siguiente lista de colores, utilizar "for"
# para imprimir en pantalla todos los colores
from tkinter import colorchooser


colores = ['rojo', 'naranja', 'verde', 'azul']

# Itere el "for" utilizando la lista como parámero
# y utilizar como elemento del "for" cada color
# for color ...


for color in colores:
    print ("Color: ", color)
# Itere el "for" utilizando el tamaño de la lista
# como parámetro y utilizar el índice para acceder a
# los elementos de la lista
# for i ...

len_colores = len(colores)

for i in range(len_colores):
    print ("Color: ", colores[i])

print("terminamos!")
