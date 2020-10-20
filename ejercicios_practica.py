#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.4

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Laureano_Cejas"
__email__ = "laurecejas2510@gmail.com"
__version__ = "1.4"

def ej1():
    # Ejercicios de práctica numérica
    
    numero_1 = 5
    numero_2 = 7
    suma = numero_1 + numero_2
    print ("El resultado de la suma es", suma)
    resta = numero_1 - numero_2
    print ("El resultado de restar", numero_1, "y", numero_2, "es", resta)

def ej2():
    
    print('Ingrese el primer número decimal a operar:')
    numero_1 = float(input())
    print("El numero ingresado es", numero_1)

    print('Ingrese el segundo número decimal a operar:')
    numero_2 = float(input())
    print ("El numero ingresado es", numero_2)
    suma = numero_1 + numero_2
    restar = numero_1 - numero_2
    multiplicación = numero_1 * numero_2
    division = numero_1 / numero_2
    print("el resultado de sumar", numero_1,"y", numero_2,"es", suma) 
    print("el resultado de restar", numero_1,"y", numero_2,"es", restar)
    print("el resultado de multiplicar", numero_1,"y", numero_2,"es", multiplicación) 
    print("el resultado de dividir", numero_1,"y", numero_2,"es", division)
 

def ej3():
    
    print('Ingrese su nombre/s:')
    nombre = str(input())
    print('Ingrese su apellido/s:')
    apellido = str(input())
    nombre_completo = nombre
    Nombre_len = len (nombre_completo)
    print (nombre+" "+apellido)
    print(nombre_completo,"tiene un total de", Nombre_len, "caracteres")

def ej4():
    # Ejemplos variables de texto

    # Ingrese tres palabras y arme un acrónimo con ellas
    # Si desea puede modificar el código para ingresar más palabras
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    print('Ingrese palabra 3:')
    palabra_3 = str(input())

    caracter_inicial = palabra_1 [0]
    caracter_inicial2 = palabra_2 [0]
    caracter_inicial3 = palabra_3 [0]
    print (caracter_inicial + caracter_inicial2 +  caracter_inicial3)


    


def ej5():
    # Ejemplos variables de texto
    # Ingrese dos palabras y arme combinaciones con ella
    print('Ingrese palabra 1:')
    palabra_1 = str(input())

    print('Ingrese palabra 2:')
    palabra_2 = str(input())

    sub_text = palabra_1 [:3]
    sub_text2 = palabra_2 [2:]

    print (sub_text + sub_text2)

    #me quede con duda coo se hace la variable 2 tomar las ultimas 3 letras de cualquier palabra como se hace?

    # De la primera palabra tome las primeras tres letras, utilice el operador :
    # De la segunda palabra tome las últimas tres letras, utilice el operador :
    # Formar una nueva palabra con los recortes solicitados
    # Imprima en pantalla los resultados


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
