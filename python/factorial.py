def factorial(valor):
    if (valor < 1) :
        return 1
    return valor * factorial(valor-1)

if __name__ == '__main__':
    numero = input('Ingrese un numero para calcular su factorial: ')        
    nFactorial = factorial(numero)
    print('Factorial de '+ str(numero) + ' : ' + str(nFactorial))