#!/usr/bin/env python
'''
Numpy [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import numpy as np
import random
import math


def blackjack_module():

    print("Ingrese su nombre!")
    nombre = str(input())
    numeros = [random.randint(1, 10) for x in range(2)]
    while sum(numeros) < 21:
        print("Tus cartas:", numeros, " suman:",
              sum(numeros), " Querés mas? Y/n?\n")
        choice = str(input())
        if choice == 'Y':
            numeros.append(random.randint(1, 10))
        elif choice == 'n':
            break
        else:
            print("ponele voluntad,", nombre, " es Y o n")
    print("Tus cartas:", numeros, " suman:", sum(numeros), "\n")
    if sum(numeros) > 21:
        print("Patinaste como chorizo en fuente de loza")
        resultado = {'puntaje': 0, 'jugador': nombre}
        return resultado
    resultado = {'puntaje': sum(numeros), 'jugador': nombre}
    return resultado


def ej1():
    print('Comenzamos a divertirnos!')

    '''
    Empecemos a jugar con las listas y su métodos, el objetivo
    es realizar el código lo más simple, ordenado y limpio posible,
    no utilizar bucles donde no haga falta, no "re inventar" una función
    que ya dispongamos de Python. El objetivo es:
    1) Generar una lista 3 numéros aleatorios con random (pueden repetirse),
       que estén comprendidos entre 1 y 10 inclusive
       (NOTA: utilizar comprension de listas a pesar de poder hacerlo
        con un método de la librería random)
    2) Luego de generar la lista sumar los números y ver si el resultado
       de la suma es menor o igual a 21
       a) Si el número es menor o igual a 21 se imprime en pantalla
          la suma y los números recoletados
       b) Si el número es mayor a 21 se debe tirar la lista y volver
          a generar una nueva, repetir este proceso hasta cumplir la
        condicion "a"
    Realizar este proceso iterativo hasta cumplir el objetivo
    '''
    while True:
        numeros = [random.randint(1, 10) for x in range(3)]
        if sum(numeros) <= 21:
            print(sum(numeros))
            break


def ej2():
    print('Comenzamos a ponernos serios!')

    '''
    Dado una lista de nombres de personas "nombres" se desea
    obtener una nueva lista filtrada que llamaremos "nombres_filtrados"
    La lista se debe filtrar por comprensión de listas utilizando la
    lista "padron" como parámetro.
    La lista filtrada sodo deberá tener aquellos nombres que empiecen
    con alguna de las letras aceptadas en el "padron".
    '''

    padron = ['A', 'E', 'J', 'T']

    nombres = ['Tamara', 'Marcelo', 'Martin', 'Juan', 'Alberto', 'Exequiel',
               'Alejandro', 'Leonel', 'Antonio', 'Omar', 'Antonia', 'Amalia',
               'Daniela', 'Sofia', 'Celeste', 'Ramon', 'Jorgelina', 'Anabela']

    nombres_filtrados = [x for x in nombres if x[0] in padron]
    print(nombres_filtrados)

    # Se espera obtener:
    # ['Tamara', 'Juan', 'Alberto'......]


def ej3():
    print("Un poco de Numpy!")
    # Ejercicio de funciones
    # Se desea calcular los valores de salida de
    # una función senoidal, dado "X" como el conjunto
    # de valores que deben someter a la función "sin"

    # Conjunto de valores "X" en un array
    x = np.arange(0, 2*np.pi, 0.1)

    # Utilizar la función np.sin para someter cada valor de "X",
    # obtenga el array "y_nump" que tenga los resultados
    # NO utilizar comprensión de listas, solo utilice la
    # funcion de numpy "np.sin"

    y_nump = np.sin(x)
    print(y_nump)

    # Conjunto de valores "X" en una lista
    x = list(np.arange(0, 2*np.pi, 0.1))

    # Utilizar comprensión de listas para obtener la lista
    # "y_list" que tenga todos los valores obtenidos como resultado
    # de someter cada valor de "X" a la función math.sin

    # y_list =
    y_list = [math.sin(x) for x in x]
    print(y_list)
    # Este es un ejemplo práctico de cuando es útil usar numpy,
    # basicamente siempre que deseen utilizar una función matemática
    # que esté definida en numpy NO necesitaran un bucle o comprensión
    # de listas para obtener el resultado de un monton de datos a la vez.


def ej4():
    print("Acercamiento al uso de datos relacionales")
    # Transformar variable numéricas en categóricas
    # Se dispone del siguiente diccionario que traduce el número ID
    # de un producto en su nombre, por ejemplo:
    # NOTA: Esta información bien podría ser una tabla SQL: id | producto
    producto = {
        556070: 'Auto',
        704060: 'Moto',
        42135: 'Celular',
        1264: 'Bicicleta',
        905045: 'Computadora',
    }

    lista_compra_id = [556070, 905045, 42135, 5674, 704060, 1264, 42135, 3654]

    lista_compra_productos = [producto.get(
        x) if x in producto else "NaN" for x in lista_compra_id]
    print(lista_compra_productos)
    
    # InoveTip: Se puede aprovechar el método "get" para que devuelva
    # un resultado deseado en caso de no encontrar la key, como por ejemplo:
    # lista_compra_productos = [producto.get(x, "Nan") for x in lista_compra_id]
    
    # InoveTip: Respecto al salte de linea, siempre el sistema espera que la siguiente
    # linea este a la "altura" del corchete que fue lo que inicio el comando:
    # lista_compra_productos = [producto.get(
    #                           x) if x in producto else "NaN" for x in lista_compra_id]
    
    # Yo en todo caso lo haría así (o un salto de línea menos)
    # lista_compra_productos = [producto.get(x)
    #                           if x in producto else "NaN"
    #                           for x in lista_compra_id
    #                           ]
    

    # Crear una nueva lista "lista_compra_productos" que transforme la lista
    # de realizada por "ID" de producto en lista por "nombre" producto
    # Iterar sobre la lista "lista_compra_id" para generar la nueva
    # En cada iteración acceder al diccionario para traducir el ID.
    # NOTA: Tener en cuenta que puede haber códigos (IDs) que
    # no esten registrados en el sistema, en esos casos se debe
    # almacenar en la lista la palabra 'NaN', para ello puede hacer uso
    # de condicionales PERO recomendamos leer atentamente el método "get"
    # de diccionarios que tiene un parametro configurable respecto
    # que sucede sino encuentra la "key" en el diccionario.


def ej5():
    print("Ahora sí! buena suerte :)")

    '''
    Black jack! [o algo parecido :)]
    El objetivo es realizar una aproximación al juego de black jack,
    el objetivo es generar una lista de 2 números aleatorios
    entre 1 al 10 inclusive, y mostrar los "números" al usuario.
    El usuario debe indicar al sistema si desea sacar más
    números para sumarlo a la lista o no sacar más
    A medida que el usuario vaya sacando números aleatorios que se suman
    a su lista se debe ir mostrando en pantalla la suma total
    de los números hasta el momento.
    Cuando el usuario no desee sacar más números o cuando el usuario
    haya superado los 21 (como la suma de todos) se termina la jugada
    y se presenta el resultado en pantalla
    BONUS Track: Realizar las modificaciones necesarias para que jueguen
    dos jugadores y compitan para ver quien sacá la suma de números
    más cercanos a 21 sin pasarse!
    '''

    print('Ingrese acontinuación la cantidad de jugadores...')
    n_jugadores = int(input())
    # InoveTip: Me encató este uso de comprension de listas ^_^
    # dudo mucho que alguien lo haga tan bien (me incluyo)
    players = [blackjack_module() for x in range(n_jugadores)]
    players.sort(reverse=True, key=lambda x: x['puntaje'])
    # InoveTip: Esta bien generaras otra lista de solo puntajes
    # para odernarla y hacer el ranking, si querias entre otras cosas
    # podias indicarle al "sort" que ordene de mayor a menor (reverse)
    # para así tenes ordenado más acorde a un raking.
    # Lo estuve pensando un poco y no se me ocurre como hacerlo más limpio
    # con las herramientas que tenemos, me refiero a evitar hacer la lista de
    # ranking por separado y luego la lista de winner por separado.
    # Lo ideal sería que pudieras ordenar la lisya players, entonces tenes
    # el nombre y puntaje ordenado. Eso se puede hacer, es un poco más complejo
    # pero te tiro el nombre del "tópico" por si queres investigarlo:

    # sort más allá de recibir parámetros como el de "reverse" podes pasarle
    # una lambda expression o una funcion que le diga como ordenar esa lista.

    # En este caso vos tenes una lista de diccionarios, hay una forma fácil de
    # crear una función o lambda y pasarla como paráemtro que haga algo
    # como lo necesitas. Te dejo un ejemplo que encontré al toque:
    # https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
    # Preguntame cualquier cosa sino entendes el mecanismo o la onda,
    # se usa mucho esto de "sobrecargar" el método de sort para ordenar
    # cosas "especiales", se usa mucho en clases.

    [print ('*' ,end='') for x in range(45)]
    print('')
    print('Ranking!! :D')
    [print ('*' ,end='') for x in range(45)]
    print('')
    [print('jugador >', x.get('jugador'),'puntaje:', x.get('puntaje'))
     for x in players]
    [print ('*' ,end='') for x in range(45)]
    print('')

    ranking = [x.get('puntaje') for x in players]
    
    if n_jugadores > 1:
        if ranking[1] == ranking[0]:
            print('Empate!')
        elif sum(ranking) == 0:
            print('Perdedores!')
        else:
            winner = [x.get("jugador")
                      for x in players if x.get('puntaje') == ranking[0]]
            print('Ganó', winner[0], '!!')
    elif n_jugadores == 0:
        print('Volvé otro día entonces...')
    else:
        if ranking[0] > 0:
           player = [x.get("jugador")
                     for x in players if x.get('puntaje') == ranking[0]]
           print('Ganaste', player[0], '!!')
        else:
           player = [x.get("jugador")
                     for x in players if x.get('puntaje') == ranking[0]]
           print('Perdiste', player[0], '!!')


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()
