def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return 'Error: División por cero'
    else:
        return a / b

def es_numero(numero):
    try:
        float(numero)
        return True
    except ValueError:
        return False

# Funcion principal

def calculadora():
    while True:
        print('Bienvenido a la Calculadora básica:\n')
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('Presione "s" para salir.')
        
        operacion = input('Seleccione una opción para empezar a operar: ')
        
        # Validación para prevenir una opción inválida
        if operacion == 's':
            print('Gracias por utilizar nuestra calculadora.')
            break
        
        elif operacion not in ['1', '2', '3', '4']:
            print(f'Error: la opción {operacion} no es valida. Intene nuevamente.')
            continue
        
        # Solicitamos los numeros al usuario
        num1 = input('Ingrese el primer numero: ')
        num2 = input('Ingrese el segundo numero: ')
        
        # Validamos que los numeros sean correctos
        if not es_numero(num1) or not es_numero(num2):
            print('Entrada invalida. Por favor, ingrese números válidos.')
        
        num1 = float(num1)
        num2 = float(num2)
        
        # Calculamos el resultado de la operación
        if operacion == '1':
            print(f"Resultado: {num1} + {num2} = {suma(num1, num2)}")
        
        elif operacion == '2':
            print(f"Resultado: {num1} - {num2} = {resta(num1, num2)}")
        
        elif operacion == '3':
            print(f"Resultado: {num1} * {num2} = {multiplicacion(num1, num2)}")
        
        elif operacion == '4':
            if num2 == 0:
                print('Error: división por 0') 
            else:
                print(f"Resultado: {num1} / {num2} = {division(num1, num2)}")
        
        # Continuar operando o salir
        continuar = input('¿Desea realizar otra operación? (si/no): ').lower()
        
        if continuar!= 'si':
            print('Gracias por utilizar nuestra calculadora.')
            break


calculadora()