# Dado el siguiente endpoint.

# https://pokeapi.co/api/v2/pokemon/1/

# Mostrar en consola el nombre del Pokemon.

# Ejemplo

# El nombre del pokemon es: bulbasaur

# Ayuda:

#    - Una muy buena idea es utilizar la función requests para realizar peticiones HTTP.
#    - JSONView es una extensión de Chrome que nos permite visualizar los objetos JSON de una manera mucho más legible.


import requests, json

if __name__ == "__main__":

    PATH = 'https://pokeapi.co/api/v2/pokemon/1/'
    response = requests.get(PATH)

    if response.status_code == 200:
        data = response.json()
       #print( json.dumps(response.json(), indent=4, sort_keys=True) )
        print( data['name'] )