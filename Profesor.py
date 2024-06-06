from Usuarios import Usuarios

class Profesor (Usuarios):
    def __init__(self, nombre, curso, codigo, profesion):
        super().__init__(nombre, curso, codigo, profesion)