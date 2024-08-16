def Gato():
    return "Michi"
print(Gato())

def Nombre():
    return "Gustavo Caballero"
print(Nombre())

def Casa():
    return "Informatica"
print(Casa())

def sumar (a, b):
    return a + b
resultado = sumar( 3, 4)
print(f"el resultado es:{resultado}") 

def sumar(a, b, c, d, e, f):
    return a + b + c + d + e + f

resultado = sumar (10 , 10 , 10 , 10 , 10 , 40)
print(f"la suma es:{resultado}")


def multiplicar (a, b):
    return a * b
print(f"Mostra el Resultado de mi Trabajo")

assert multiplicar(2,4) > 6, "resultado"


# CAJERO

usuarios = [{"nombre" : "Juan", "pin":"1234", "saldo":1000},
            {"nombre" : "Luca", "pin":"5678", "saldo":1500}]

def encontrar_usuario(nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            return usuario
    return None

def cajero():
    nombre =input("Ingrese su nombre: ")
    usuario = encontrar_usuario(nombre)

    if usuario is None:
        print("usuario no encontrado")
        return

cajero()



      
