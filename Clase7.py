usuarios = [{"nombre" : "Juan", "pin":"1234", "saldo":1000},
            {"nombre" : "Luca", "pin":"5678", "saldo":1500}]

#Función para encontrar un usuario mediante su nombre
def encontrar_usuario(nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            return usuario
    return None

#Función para consultar el saldo
def consultar_saldo(usuario):
    return usuario["saldo"]

#Función para depositar
def depositar(usuario,monto):
    usuario["saldo"] += monto
    return usuario['saldo']


def cajero():
    nombre =input("Ingrese su nombre: ")
    usuario = encontrar_usuario(nombre)

    if usuario is None:
        print("usuario no encontrado")
        return
    
    pin = input("Ingrese su pin: ")

    if pin != usuario["pin"]:
        print("Pin incorrecto")
        return
    
    while True:
        print("\nOpciones:")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Salir")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print(f"Saldo actual: {consultar_saldo(usuario)}")
        elif opcion == "2":
            monto = int(input("Ingrese la cantidad que deseaa depositar: "))
            nuevo_saldo = depositar(usuario, monto)
            print("Su nuevo saldo es", nuevo_saldo)
        elif opcion == "3":
            print("Gracias por utilizar el cajero!")
            break
        else:
            print("Opcion invalida")
cajero()