def saludar(nombre, mensaje = 'Hola'):
     return f'{mensaje}, {nombre}'

print(saludar('Ceci', 'Chau'))


def impresion_con_args(a,b,*args):
     print(f'a = {a}')
     print(f'b = {b}')
     print(f'args = {args}')


impresion_con_args(1,2,3,4)