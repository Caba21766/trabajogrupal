class Persona:

    def __init__(self,nombre,edad,nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad}\nNacionalidad: {self.nacionalidad}'
    
persona = Persona('José','33','Argentino')

print(persona.mostrar_info())