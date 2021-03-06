#!/usr/bin/env python
'''
Numpy [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import numpy as np
import time
import random

top = 5000000


def metodos_numpy_vs_list():
    print('Ejemplos de implementaciones con numpy vs list')
    print('Método SUM')
    v1 = np.arange(top)
    l1 = list(range(top))

    time1 = time.time()
    np.sum(v1)
    time2 = time.time()
    numpy_time_ms = (time2-time1)*1000
    print('Numpy time: {:.2f}ms'.format(numpy_time_ms))

    time1 = time.time()
    sum(l1)
    time2 = time.time()
    list_time_ms = (time2-time1)*1000
    print('List time: {:.2f}ms'.format(list_time_ms))
    print('SUM: Numpy vs List x{:.2f}'.format(list_time_ms/numpy_time_ms))

    print('Método mean')
    v1 = np.arange(top)
    l1 = list(range(top))

    time1 = time.time()
    np.mean(v1)
    time2 = time.time()
    numpy_time_ms = (time2-time1)*1000
    print('Numpy time: {:.2f}ms'.format(numpy_time_ms))

    time1 = time.time()
    sum(l1) / len(l1)
    time2 = time.time()
    list_time_ms = (time2-time1)*1000
    print('List time: {:.2f}ms'.format(list_time_ms))
    print('MEAN: Numpy vs List x{:.2f}'.format(list_time_ms/numpy_time_ms))

    print('Método sort')
    v1 = np.arange(top)
    l1 = list(range(top))

    time1 = time.time()
    np.sort(v1)
    time2 = time.time()
    numpy_time_ms = (time2-time1)*1000
    print('Numpy time: {:.2f}ms'.format(numpy_time_ms))

    time1 = time.time()
    l1.sort()
    time2 = time.time()
    list_time_ms = (time2-time1)*1000
    print('List time: {:.2f}ms'.format(list_time_ms))
    print('SORT: Numpy vs List x{:.2f}'.format(list_time_ms/numpy_time_ms))


def numpy_where_diff():
    # Ejemplos de uso del método where y diff
    print('Método Where')
    l1 = list(range(top))
    v1 = np.asanyarray(l1)

    where_v1 = np.where(v1 % 2, v1, 0)
    # [0 2 0 4 0 6 0 7 0 8]

    time1 = time.time()
    np.where(v1 % 2, v1, 0)
    time2 = time.time()
    numpy_time_ms = (time2-time1)*1000
    print('Numpy time: {:.2f}ms'.format(numpy_time_ms))

    time1 = time.time()
    [x if x % 2 else 0 for x in l1]
    time2 = time.time()
    list_time_ms = (time2-time1)*1000
    print('List time: {:.2f}ms'.format(list_time_ms))
    print('WHERE: Numpy vs List x{:.2f}'.format(list_time_ms/numpy_time_ms))

    print('Método Diff')
    v1 = np.array([1, 2, 4, 7])
    v1_diff = np.diff(v1)
    # [2-1, 4-2, 7-4]
    # [1 2 3]
    print(v1_diff)

    m = np.array([
                 [1, 5],
                 [3, 1],
                 [5, 10]
                 ])

    m_diff_por_fila = np.diff(m)
    # [[ 4]
    #  [-2]
    #  [ 5]]
    print(m_diff_por_fila)

    m_diff_por_columna = np.diff(m, axis=0)
    # [[ 2 -4]
    #  [ 2  9]]
    print(m_diff_por_columna)


def expresion_map_lambda():
    print('Lambda expression y map')
    # Crear una funcion lambda que multiplique por 2
    # el valor pasado a la función
    mult_by_2 = lambda x: 2*x
    print(mult_by_2(3))  # resultado = 6

    # Utilizar "map" para aplicar una función
    # a toda una lista de forma iterativa
    # En este caso se utilizará la función
    # "abs()"
    numeros = [1, -5, -6, 4]
    numeros_abs = list(map(abs, numeros))
    print(numeros_abs)
    # [1, 5, 6, 4]

    # Ahora utilizar map para mapear nuestra función
    # lambda y aplicarla a toda la lista (iterar)
    numeros = [1, -5, -6, 4]
    numeros_abs = list(map(mult_by_2, numeros))
    print(numeros_abs)
    # [2, -10, -12, 8]

    # El potencial de la lambda expression es poderla
    # definirla dentro del map (in line)
    numeros = [1, -5, -6, 4]
    numeros_lambda = list(map(lambda x: 2*x, numeros))
    print(numeros_abs)
    # [2, -10, -12, 8]


def lambda_vs_bucle():
    print('lambda vs bucles')
    # Deseamos crear una lista de números pares
    # que contenga todos los números del 0 al 1000000 inclusive
    rango = range(500001)

    time1 = time.time()
    # ----------------------------
    # Método tradicional con bucle
    lista_pares_bucle = []
    for i in rango:
        valor = 2*i
        lista_pares_bucle.append(valor)
    # ----------------------------
    time2 = time.time()
    bucle_time_ms = (time2-time1)*1000
    print('Bucle time: {:.2f}ms'.format(bucle_time_ms))

    numeros = list(rango)
    time1 = time.time()
    # ----------------------------
    # Método con map + lambda expression
    lista_pares_lambda = list(map(lambda x: 2*x, numeros))
    # ----------------------------
    time2 = time.time()
    list_time_ms = (time2-time1)*1000
    print('List time: {:.2f}ms'.format(list_time_ms))
    print('Lambda vs Bucle x{:.2f}'.format(bucle_time_ms/list_time_ms))


def compresion_listas():
    print('Práctica con compresión de listas')

    # Generar una lista a partir de
    # multiplicar por "2" todos los valores
    # de "numeros"
    numeros = [1, -5, -6, 4]
    numeros_cmp = [2*x for x in numeros]
    print(numeros)
    # numeros_cmp= [2, -10, 12, 8]

    print('Generador de listas')
    # Generar una nueva lista utilizando los datos
    # del rango para generar nuevos
    lista = [x**2 for x in range(10)]
    print(lista)

    # Generar una nueva lista, utilizar el rango para
    # iterar cierta cantidad de veces (definir el tamaño)
    # de la lista, y generar datos en cada iteración.
    lista = [random.randint(1, 6) for x in range(5)]
    print(lista)

    print('Filtro')
    # Generar una lista que tome los números pares
    # y reemplace los números impares por "0"
    numeros = [1, 2, 4, 6, 8, 3, 5]
    lista = [x if(x % 2) == 0 else 0 for x in numeros]
    # lista [0, 2, 4, 6, 8, 0, 0]
    print(lista)

    # Generar una lista que solo tome los números pares
    # y descarte los números impares por "0"
    numeros = [1, 2, 4, 6, 8, 3, 5]
    lista = [x for x in numeros if(x % 2) == 0]
    # lista [2, 4, 6, 8]
    print(lista)


def compresion_listas_vs_bucle():
    print('Compresion de listas vs bucles')
    # Deseamos crear una lista de números pares
    # que contenga todos los números del 0 al 1000000 inclusive
    rango = range(500001)

    time1 = time.time()
    # ----------------------------
    # Método tradicional con bucle
    lista_pares_bucle = []
    for i in rango:
        valor = 2*i
        lista_pares_bucle.append(valor)
    # ----------------------------
    time2 = time.time()
    bucle_time_ms = (time2-time1)*1000
    print('Bucle time: {:.2f}ms'.format(bucle_time_ms))

    time1 = time.time()
    # ----------------------------
    # Método con compresion
    lista_pares_comp = [2*x for x in rango]
    # ----------------------------
    time2 = time.time()
    list_time_ms = (time2-time1)*1000
    print('Compresión time: {:.2f}ms'.format(list_time_ms))
    print('Compresion vs Bucle x{:.2f}'.format(bucle_time_ms/list_time_ms))


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ----------------------------
    # Uso de Numpy vs bucles vs listas
    # queda para que el alumno chusmee
    metodos_numpy_vs_list()
    numpy_where_diff()
    # ----------------------------
    expresion_map_lambda()
    lambda_vs_bucle()
    compresion_listas()
    compresion_listas_vs_bucle()
