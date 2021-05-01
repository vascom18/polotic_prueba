

numero=int(input("ingrese un numero: "))
numero_original=numero
restocero=0
while numero>=1:
    if (numero_original%numero)==0:
        restocero+=1
    numero-=1 
  
if restocero==2:
    print("el numero es primo")
else:
    print("el numero no es primo")