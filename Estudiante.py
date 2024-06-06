from Usuarios import Usuarios

class Estudiante (Usuarios):
    def __init__(self, nombre, curso, carnet, carrera):
        super().__init__(nombre, curso, carnet, carrera)