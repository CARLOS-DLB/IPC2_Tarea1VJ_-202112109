import os
from Profesor import Profesor
from Estudiante import Estudiante

estudiantes = []
profesores = []

def menu_inicial():
    print('----------------MENU PRINCIPAL----------------')
    opciones = {
        "1": CRUD_Profesores,
        "2": CRUD_Estudiantes,
        "3": Salir,
    }

    while True:
        opcion = input("\n 1. CRUD de Profesores\n 2. CRUD de Estudiantes\n 3. Salir\nSeleccione una opción:")
        
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# PROFESORES
def CRUD_Profesores():
    cleanConsole()
    print('----------------MENU PROFESORES----------------')
    opciones = {
        "1": crear_profesor,
        "2": leer_profesor,
        "3": actualizar_profesor,
        "4": eliminar_profesor,
        "5": regresar,
    }

    while True:
        opcion = input("\n 1. Crear Profesor \n 2. Leer Profesor \n 3. Actualizar Profesor\n 4. Eliminar Profesor \n 5. Regresar al menú principal \n Seleccione una opción:  ") 
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def crear_profesor():
    cleanConsole()
    global profesores
    print('----------------CREAR PROFESOR----------------')
    nombre = input('Ingrese el nombre del profesor: ')
    curso = input('Ingrese el curso que imparte: ')
    codigo = input('Ingrese el código del profesor: ')
    profesion = input('Ingrese la profesión del profesor: ')
    profesores.append(Profesor(nombre, curso, codigo, profesion))   
    print('\n Profesor creado con éxito')

def actualizar_profesor():
    cleanConsole()
    global profesores
    codigo = input('Ingrese el código del profesor a actualizar: ')
    nombre = input('Ingrese el nombre del profesor: ')
    curso = input('Ingrese el curso que imparte: ')
    profesion = input('Ingrese la profesión del profesor: ')

    for profesor in profesores:
        if profesor.id == codigo:
            profesor.setNombre(nombre)
            profesor.setCurso(curso)
            profesor.setOcupacion(profesion)
            print('\n Profesor actualizado con éxito')
            break
        else:
            print('\n No se encontró ningun profesor con ese codigo')

def leer_profesor():
    cleanConsole()
    print('----------------PROFESORES ASIGNADOS----------------')
    global profesores

    if len(profesores) == 0:
        print('No hay profesores registrados')
    
    for profesor in profesores:
        print(f'\n Nombre: {profesor.nombre} \n Curso: {profesor.curso} \n Código: {profesor.id} \n Profesión: {profesor.ocupacion}')

def eliminar_profesor():
    cleanConsole()
    global profesores
    codigo = input('Ingrese el código del profesor a eliminar: ')

    for profesor in profesores:
        if profesor.getId() == codigo:
            profesores.remove(profesor)
            print('\n Profesor eliminado con éxito')
            break
        else:
            print('\n No se encontró ningun profesor con ese codigo')

#  ESTUDIANTES
def CRUD_Estudiantes():
    cleanConsole()
    print('----------------MENU ESTUDIANTES----------------')
    opciones = {
        "1": crear_estudiante,
        "2": leer_estudiante,
        "3": actualizar_estudiante,
        "4": eliminar_estudiante,
        "5": regresar,
    }

    while True:
        opcion = input("\n 1. Crear Estudiante \n 2. Leer Estudiante \n 3. Actualizar Estudiante\n 4. Eliminar Estudiante \n 5. Regresar al menú principal \n Seleccione una opción:  ") 
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def crear_estudiante():
    cleanConsole()
    print('----------------CREAR ESTUDIANTE----------------')
    nombre = input('Ingrese el nombre del estudiante: ')
    curso = input('Ingrese el curso que recibe: ')
    carnet = input('Ingrese el carnet del estudiante: ')
    carrera = input('Ingrese la carrera del estudiante: ')
    estudiantes.append(Estudiante(nombre, curso, carnet, carrera))   
    print('\n Estudiante creado con éxito') 

def leer_estudiante():
    cleanConsole()
    print('----------------ESTUDIANTES ASIGNADOS----------------')
    global estudiantes

    if len(estudiantes) == 0:
        print('No hay profesores registrados')
    
    for estudiante in estudiantes:
        print(f'\n Nombre: {estudiante.nombre} \n Curso: {estudiante.curso} \n Carnet: {estudiante.id} \n Carrera: {estudiante.ocupacion}')

def actualizar_estudiante():
    cleanConsole()
    global estudiantes
    carnet = input('Ingrese el carnet del estudiante a actualizar: ')
    nombre = input('Ingrese el nombre del estudiante: ')
    curso = input('Ingrese el curso que recibe: ')
    carrera = input('Ingrese la carrera del estudiante: ')

    for estudiante in estudiantes:
        if estudiante.id == carnet:
            estudiante.setNombre(nombre)
            estudiante.setCurso(curso)
            estudiante.setOcupacion(carrera)
            
            print('\n Estudiante actualizado con éxito')
            break
        else: 
            print('\n No se encontró ningun estudiante con ese carnet')

def eliminar_estudiante():
    cleanConsole()
    global estudiantes
    carnet = input('Ingrese el carnet del estudiante a eliminar: ')

    for estudiante in estudiantes:
        if estudiante.getId() == carnet:
            estudiantes.remove(estudiante)
            print('\n Estudiante eliminado con éxito')
            break
        else:
            print('\n No se encontró ningun estudiante con ese carnet')

#  FUNCIONES COMPARTIDAS
def regresar():
    menu_inicial()

def Salir():
    print('Hsata luego!')
    exit()

def cleanConsole():
    os.system('cls')

if __name__ == "__main__":    
    menu_inicial()

