# Modelos Matemáticos en Finanzas Cuantitativas - Trabajo Práctico 2: Simulación por Monte Carlo y Opciones americanas

## Introducción
---------------
Este trabajo consiste en obtener la prima de una _opción put americana_ adaptando el _método de Montecarlo_ visto anteriormente a este dominio. Además, se compararán los resultados obtenidos para opciones americanas con aquellos para opciones europeas obtenidos mediante la _fórmula de Black-Scholes_ y se dará un ejemplo detallado de su ejecución.

## Métodos utilizados
---------------------
### Método de Montecarlo
Consiste en generar caminos aleatorios de los precios a través de períodos de tiempo determinados utilizando la fórmula con la que se calculan los precios actuales en base al precio anterior. Luego se construye una matriz con los valores intrínsecos de las opciones e, iteradamente, se decide desde el período n - 1 hasta el 1 si conviene ejercer la opción en base a la relación funcional dada por __Vt = a + b*St + c* (St ** 2)__ y los valores de __a__, __b__ y __c__ que la minimizan. Por último, se aproxima el valor de la prima de la opción por el máximo entre el valor intrínseco de la opción en __t = 0__ y el promedio descontado de los payoffs del período __t = 1__. 

## Resultados
-------------
Considerando __S0 = 36__, __r = 0,06__, __σ = 0,2__, __T = 1 año__, __n = 50__ y __N = 20000__, y utilizando para calcular las primas de las put europeas que __p = K * (e ** (-r*T)) * Φ(-d2) - S0 * Φ(-d1)__, se obtuvieron los siguientes resultados:

| K        | Put europea | Put americana |
| ---------|:-----------:| -------------:|
| 36      | 1.6713364162377387 | 0.36998907192097624 |
| 38      | 2.5346602787878787      |   2 |
| 40      | 3.1664015342188474 |    4 |
| 42      | 4.014957657980567 | 6 |
| 44      | 6.303428913689132 | 8 |

## Ejemplo de ejecución
-----------------------
Veremos un ejemplo detallado de la ejecución del algoritmo para el caso __n = 3__,  __N = 8__ y __K = 36__, con __S0__, __r__ y __σ__ iguales a los del ejercicio anterior, para el ejemplo se muestran los estados de la matriz de valores de la acción en los N caminos y la matriz de los payoffs/valores de la acción en cada iteración.
El proceso es el siguiente:

1) Generamos dos matrices (una para los __precios__ de la acción y otra para los __payoffs__) __N x n__, en este caso 8 x 3:
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]
 [0. 0. 0.]]

    [[0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]
     [0. 0. 0.]]

2) Llenamos la matriz de precios utilizando la fórmula mencionada anteriormente y en la matriz de payoffs llenamos la última columna con __máx(K − Sn, 0)__:
[[36.         33.54442432 30.78057599]
 [36.         37.00116061 34.69801106]
 [36.         34.76722164 38.2646558 ]
 [36.         38.56905836 43.12814706]
 [36.         30.69842914 32.73518983]
 [36.         37.5563584  45.49049488]
 [36.         38.69860488 45.77864242]
 [36.         35.28754414 34.63565538]]

    [[36.         33.54442432  5.21942401]
     [36.         37.00116061  1.30198894]
     [36.         34.76722164  0.        ]
     [36.         38.56905836  0.        ]
     [36.         30.69842914  3.26481017]
     [36.         37.5563584   0.        ]
     [36.         38.69860488  0.        ]
     [36.         35.28754414  1.36434462]]

3) Llenamos las columnas n - 1, n - 2, ..., 1 (en nuestro caso __n - 2, ..., 0__) de la matriz de payoffs con los valores de __máx(K - St, a + bSt + cSt²)__, siendo a, b y c los valores que minimizan la relación funcional __Vt =  a + bSt + cSt²__ para cada período y, en caso ser el máximo __K - St__ para algún camino (se ejerce la opción), todos los valores hacia la derecha en el camino se vuelven __0__:
__Iteracion 1:__
[[0.         2.45557568 0.        ]
 [0.         0.         0.        ]
 [0.         1.23277836 0.        ]
 [0.         0.         0.        ]
 [0.         5.30157086 0.        ]
 [0.         0.         0.        ]
 [0.         0.         0.        ]
 [0.         0.71245586 0.        ]]
 
 4) Definimos a __X__ como la media descontada de los valores en la columna 1. Luego, definimos a la prima de la opción put como __máx(K - S0, X) = máx(0, 1.142169761715984) = 1.142169761715984__





