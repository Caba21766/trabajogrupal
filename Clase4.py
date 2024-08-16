def impresion_con_args_kwargs(a,b,*args,c,d,**kwargs):
     print(f'a = {a}')
     print(f'b = {b}')
     print(f'args = {args}')
     print(f'c = {c}')
     print(f'd = {d}')
     print(f'kwargs = {kwargs}')
    
impresion_con_args_kwargs(1,2,3,4,c=5,d=6,e=7,f=8)