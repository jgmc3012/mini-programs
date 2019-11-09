# Mediante una función implementar el cifrado cesar.

#     La función debe tener por nombre cifrado.
#     La función debe poseer dos parámetros: sentencia de tipo string y llave de tipo entero.
#     El parámetro sentencia será el texto a cifrar.
#     El parámetro llave hará referencia a la cantidad de espacios a desplazar.
#     Por default el parámetro llave tendrá el valor de 10.
#     La función debe retornar el texto cifrado.
#     Los números y espacios dentro de la sentencia deben conservarse.
#     La función debe retornar el cifrado en minúscula (No importa que la entrada haya tenido mayúsculas).
#     Al hacer el llamado de la función es posible omitir un valor para el parámetro llave.

# Ejemplos

# >>> cifrado('Hola Como estas', 23)
# elix zljl bpqxp

# >>> cifrado('supersentencia')
# cezobcoxdoxmsk

# >>> cifrado('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 23)
# cezobcoxdoxmsk

# Ayuda: Puedes apoyarte de la biblioteca string para generar la lista de letras del alfabeto.

from string import ascii_lowercase as alf


def cesar(sentence, key=10):
    response = ''
    sentence = sentence.lower()

    if key >= len(alf):
        key = key % len(alf)

    for char in sentence:

        if (char in alf):
            index = alf.index(char) + key

            if index >= len(alf):
                index -= len(alf)
            
            char = alf[index]

        response += char
    
    return response
        

if __name__ == '__main__':
    
    words = input('Ingresa el mensaje a cifrar: ')
    key = int(input('Ingrese el valor de la llave, presione enter para omitir, por defecto es 10: '))
    if key:
        print(cesar(words, key))
    else:
        print(cesar(words))