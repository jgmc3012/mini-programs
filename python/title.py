""" 
Definir una función la cual nos permita convertir un string a un formato título.
Es entiende por formato título un string con su primera letra en mayúscula.

    La función debe tener por nombre to_title.
    La función debe poser el parámetro message.
    El parámetro debe ser obligatorio.
    La función debe retornar el parámetro en su formato título.

Ejemplos.

print(to_title('eduardo'))
>>> Eduardo

print(to_title('hola mundo'))
>>> Hola mundo
"""


def to_title(message):
    message = message.strip()
    return message[0].upper() + message[1:].lower()

if __name__ == "__main__":
    msg = input('Introduce el texto del titulo: ')
    print(to_title(msg))