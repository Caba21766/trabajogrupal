class Mascota:
    especie = 'Animal domestico'

    def __init__(self,nombre):
        self.nombre = nombre

mascota1 = Mascota('Valkiria')
mascota2 = Mascota('White')

print(f'{mascota1.nombre} es un {mascota1.especie}\n{mascota2.nombre} es un {mascota2.especie}')