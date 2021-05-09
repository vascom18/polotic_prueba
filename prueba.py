anio= int(input("ingrese año: "))
"""mes= (input("ingrese mes: "))
dia= int(input("ingrese dia: "))"""


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

def primerdia():
    global dias_totales 
    dias_totales= 0

    for i in range(1753,anio+1):
    
        if bisiesto(i)==True:
            dias_totales+=366
        else:
            dias_totales+=365
      
primerdia()
             
primer_dia=dias_totales%7

if bisiesto(anio)==True:
        primer_dia-=1    

print(semana[primer_dia])
meses={"enero":31, "febrero":28, "marzo":31, "abril":30, "mayo":31, "junio":30, "julio":31, "agosto":31, "septiembre":30, "octubre":31, "noviembre":30, "diciembre":31}
if bisiesto(anio)==True:
    meses={"enero":31, "febrero":29, "marzo":31, "abril":30, "mayo":31, "junio":30, "julio":31, "agosto":31, "septiembre":30, "octubre":31, "noviembre":30, "diciembre":31}
    
#-------------impresion-----------------   







    