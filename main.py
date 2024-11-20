def par_impar(numero):
    if numero%2==0:
        print(str(numero)+' es PAR.\nLos numeros pares desde '+str(numero)+' hasta 0 son:')
        for n in range(numero,-1,-2):print(n)
    else:
        print(str(numero) + ' es IMPAR.\nLos numeros impares desde ' +str(numero) + ' hasta 1 son:')
        for n in range(numero, 0, -2): print(n)
def check():
    try:
        numero=int(input('Ingresar un numero entero: '))
        par_impar(numero)
    except ValueError:
        print('No es un numero entero.')
        check()
check()
