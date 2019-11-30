# Crea una lista la cual almacene 10 calificaciones que el usuario ingrese mediante teclado.

# Mostrar en pantalla el promedio de dichas calificaciones.

def average(numbers):
    count = 0

    for number in numbers:
        count += number/len(numbers)
    
    return '{:.2f}'.format(count)

if __name__ == "__main__":
    numbers = [ int(input(f'Valor de la {x+1}° calificacion: ')) for x in range(10) ]

    print(f'Promedio de calificaciones: {average(numbers)}')