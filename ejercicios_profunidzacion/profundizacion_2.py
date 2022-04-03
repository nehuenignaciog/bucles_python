# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA:
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio

numero_1 = float(input("Ingrese el primer número\n"))
numero_2 = float(input("Ingrese el primer número\n"))

# Muestro menú de operaciones válidas

operador_invalido = True

while operador_invalido:

    print ("\nPor favor ingrese operación deseada:\n")
    print ("- Suma (+)\n- Resta (-)\n- Multiplicación (*)\n- División (/)\n- Exponente/Potencia (**)\n")
    print ("(Ingrese palabra FIN para salir.)")
    operador = str(input())
    if operador == '+':
        print ("\n- Suma (+)= ", numero_1 + numero_2)
    elif operador == '-':
        print ("\n- Resta (-)= ", numero_1 - numero_2)
    elif operador == '*':
        print ("\n- Multiplicación (*)= ", numero_1 * numero_2)
    elif operador == '/':
        print ("\n- División (/): ", numero_1 / numero_2)
    elif operador == '**':
        print ("\n- Exponente/Potencia (*): ", numero_1 ** numero_2)
    elif operador == "FIN":  # Finalizo el programa
        operador_invalido = False
    else:
        print ("Operador inválido.")
