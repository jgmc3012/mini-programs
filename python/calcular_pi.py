# π (pi) es sin duda una de las constantes matemáticas más importantes de todos los tiempos. Todos conocemos el valor de π (pi) , bueno, quizás solo sus primeros decimales.

# 3.1415

# Es por ello que en esta ocasión es necesarios que implementes el Problema de Basilea para encontrar el "valor" de π (pi).

# Es obligatorio obtener por lo menos los primeros 6 decimales.

# Pista: Tendrás que multiplicar por 6 y realizar una raíz cuadrada. 🙈

from math import sqrt

def basiela(presicion):
    """
    Retorna el valor de la solucion al problema de Basiela.
    """
    count = 0
    x = 0
    while (True):
        count +=1
        xOld = x
        x += 1/(count**2)
        delta = x - xOld
        if delta < presicion :
            print( 'Iteraciones realizadas: ' + str(count) )
            print( 'Numero de Basiela: ' + str(x) )
            return x

def calculate_pi(numBasiela):
    return sqrt(6*numBasiela)


if __name__ == '__main__':
    numBasiela = basiela(0.0000000000001)
    print('valor de pi: ' + str(calculate_pi(numBasiela)) )
