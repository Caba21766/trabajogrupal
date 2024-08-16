def sumar(**kwargs):
     resultado=0

     for clave, valor in kwargs.items():
         print(clave, '=', valor)
         resultado += valor
    
     return resultado

print(sumar(a=3,b=10,c=5))