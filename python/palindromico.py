# Definir una función la cual permita conocer si un string es un palíndromo o no. Un palíndromo es una palabra, o frase que se lee igual de izquierda a derecha que de derecha a izquierda

#     La función debe tener por nombre palíndromo.
#     La función debe poseer un parámetro llamado sentencia.
#     La función debe retornar verdadero o falso dependiendo si el parámetro es, o no un palíndromo.

# Ejemplos

# >>> palindromo('Anita lava la tina')
# True

# >>> palindromo('Sometamos o matemos')
# True

# >>> palindromo('Super palindromo')
# False

def palindromico(sentence):
    sentence = sentence.lower().replace(' ', '')
    origin = list(sentence)

    rever = list(sentence)
    rever.reverse()

    return (origin == rever)

if __name__ == '__main__':
    print(palindromico('Anita lava la tina'))