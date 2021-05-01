numero = int(input("Ingrese un número para saber se es primo: "))

if numero > 1:
    contador = 0
    i = 2 
    while i < numero and contador == 0:
        resto = numero % i
        print("{} % {} = {}". format(numero,i,resto))
        if resto == 0:
            contador += 1

        i +=1
    if contador == 0:
        print("El {} es un número primo".format(numero))
    else:
        print("El {} no es un número primo".format(numero))

else:
    print("El {} no es un número primo".format(numero))
    
