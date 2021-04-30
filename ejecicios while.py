x=0
maxpar=0

while x<5:
    numero=int(input("ingrese un numero:"))
    if (numero%2)==0:
        if numero>maxpar:
            maxpar=numero
        if x==0:
            minimpar=numero
    else:
        if x==0:
            minimpar=numero
        if numero<minimpar:
            minimpar=numero
    
    x+=1
        
print("maximo par:",maxpar,"minimo impar: ",minimpar) 
#esto es una prueba
  
    
        
    


