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


def CRUD_Profesores():
    print('----------------MENU PROFESORES----------------')
    opciones = {
        "1": crear_profesor,
        "2": leer_profesor,
        "3": actualizar_profesor,
        "4": eliminar_profesor,
        "5": regresar,
    }

    while True:
        opcion = input("Seleccione una opción: \n 1. CRUD de Profesores\n 2. CRUD de Estudiantes\n 3. Salir\n")
        
        if opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


def CRUD_Estudiantes():
    print('Crud Estudiantes')

def Salir():
    exit()

def crear_profesor():
    print('creando')
def leer_profesor():
    print('leyendo')
def actualizar_profesor():
    print('actualizando')
def eliminar_profesor():
    print('actualizando')
def regresar():
    print('actualizando')

if __name__ == "__main__":    
    menu_inicial()