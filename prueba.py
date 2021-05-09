anio= int(input("ingrese año: "))
"""mes= int(input("ingrese mes: "))
dia= int(input("ingrese dia: "))"""

diafinanio=-1
semana=["domingo","lunes","martes","miercoles","jueves","viernes","sabado"]

#-------------------funcion bisiesto----------------

def bisiesto(verificar):  
    if verificar%4==0:
        if verificar%100==0:
            if verificar%400==0:
                return True
            else:
                return False
        else:
            return True    
            
    else:
        return False
    
for i in range(1950,anio+1):
    
    if bisiesto(i)==True:
        diafinanio+=2
        
    else:
        diafinanio+=1
             
ultimodia=diafinanio%7

print(semana[ultimodia])
meses={"enero":31, "febrero":28, "marzo":31, "abril":30, "mayo":31, "junio":30, "julio":31, "agosto":31, "septiembre":30, "octubre":31, "noviembre":30, "diciembre":31}
if bisiesto(anio)==True:
    meses={"enero":31, "febrero":29, "marzo":31, "abril":30, "mayo":31, "junio":30, "julio":31, "agosto":31, "septiembre":30, "octubre":31, "noviembre":30, "diciembre":31}
    
#-------------impresion-----------------   







    