class Usuarios:
    def __init__(self, nombre, curso, id, ocupacion):
        self.nombre = nombre
        self.curso = curso
        self.id = id
        self.ocupacion = ocupacion

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def getCurso(self):
        return self.curso
    
    def setCurso(self, curso):
        self.curso = curso
    
    def getId (self):
        return self.id
    
    def setId (self, id):
        self.id = id
    
    def getOcupacion(self):
        return self.ocupacion
    
    def setOcupacion(self, ocupacion):
        self.ocupacion = ocupacion