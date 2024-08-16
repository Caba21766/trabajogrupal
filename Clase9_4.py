class Calculadora:

    @staticmethod
    def sumar(a,b):
        return a + b
    
    @staticmethod
    def restar(a,b):
        return a - b
    
resultado_suma = Calculadora.sumar(8,5)
resultado_resta = Calculadora.restar(10,5)

print(f'El resultado de la suma es {resultado_suma}\nEl resultado de la resta es {resultado_resta}')