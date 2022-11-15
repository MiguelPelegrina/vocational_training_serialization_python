class Alumno(object):
    def __init__(self, codigo, nombre, apellido):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido

    def __eq__(self, other):
        self.codigo = other.codigo

    def imprimir(self):
        print(f"Codigo: {self.codigo}, Nombre: {self.nombre}, Apellido: {self.apellido}")
