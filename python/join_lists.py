# Mostrar en consola el nombre del alumno con su correspondiente calificación.

# Al alumno número uno le corresponde la calificación número uno, al alumno número dos le corresponde la calificación número dos, y así sucesivamente.

# Eduardo posee una calificación de: 10
# Fernando posee una calificación de: 10
# Mariana posee una calificación de: 8
# Raquel posee una calificación de: 7
# Santiago posee una calificación de: 9

# Restricciones:

#    - El programa debe contar con por lo menos un ciclo for.
#    - El programa NO puede hacer uso de los indices de las listas.


if __name__ == '__main__':
    calificaciones = [10, 10, 8, 7, 9]
    alumnos = ['Eduardo', 'Fernando', 'Mariana', 'Raquel', 'Santiago']

    for alumno, calificacion in zip(alumnos,calificaciones):
        print(f'{alumno} posee una calificacion de: {calificacion}')