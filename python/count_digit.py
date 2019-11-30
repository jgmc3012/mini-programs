# Definir una función la cual nos permita conocer cuantos dígitos posee un número.

#    - La función debe tener por nombre cantidad_digitos.
#    - La función debe poseer el parámetro numero.
#    - La función debe retornar la cantidad de dígitos del parámetro.
#    - No es posible utilizar la función str.


from math import log10, trunc

def count_digit(number):
    number = abs(number)

    return trunc( log10(number) ) + 1

if __name__ == '__main__':
    number =  int(input('Ingrese el numero al cual desea calcularle su cantidad de digitos: '))
    print(f'{ number } contine {count_digit(number)} digitos')