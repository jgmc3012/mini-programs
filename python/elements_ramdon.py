""" 
Dada la siguiente lista de usuarios.

['Eduardo', 'Raquel', 'Roberto', 'Marines', 'Isabel']

Definir un order, aleatorio, para cada usuario.

Ejemplos.

1 - Roberto
2 - Raquel
3 - Isabel
4 - Eduardo
5 - Marines

1 - Marines
2 - Roberto
3 - Eduardo
4 - Raquel
5 - Isabel

Sol del profesor: 
    import random

    if __name__ == '__main__':
        usuarios = ['Eduardo', 'Raquel', 'Roberto', 'Marines', 'Isabel']

        random.shuffle(usuarios)

        for posicion, usuario in enumerate(usuarios):
            print(f'{posicion + 1} - {usuario}')

"""

import random

if __name__ == "__main__":

    new_list = []
    list = ['Eduardo', 'Raquel', 'Roberto', 'Marines', 'Isabel']
    
    while len(list) > 0:
        new_list.append(list.pop(random.randint(0,len(list))))
