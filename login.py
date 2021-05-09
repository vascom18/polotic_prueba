salir=0
usser=""
contras=""
contrase="a"
valido= False
main=0
usuarios={"admin":"admin"}
volver_menu=0

while salir==0:
    main= int(input("----------bienvenido--------------- \n Iniciar sesion:1 \n Registrarse:2 \n Salir:3 \n imprimir usuarios y contraseñas: 4\n Ingrese la opcion deseada: "))
    volver_menu=0
    while volver_menu==0:
        if main==1:
            while volver_menu==0:
                print("--------inicio de sesion---------")
                ingreso_user= input("ingrese su usuario: ")
                ingreso_contras= input("ingrese contraseña: ")
                valido= usuarios[ingreso_user]==ingreso_contras
                if valido:
                    print("bienvenido ",usser)
                    volver_menu=1
                        
                else:
                
                    print("usuario o contraseña no validos, por favor vuelva a intentarlo")
        elif main==2:
            while volver_menu==0:
                print("--------registro de usuario----------")
                usser=input("ingrese un usuario:")
                contras= input("ingrese una contraseña:")
                contrase=input("ingrese nuevamente la contraseña")
                if contras==contrase:
                    usuarios[usser]=contras
                    print("nuevo usuario registrado correctamente")
                    volver_menu=int(input("desea regresar al menu? no:0 si:1    :"))
                else:
                    print("las contraseñas no son iguales, intente nuevamente")
                    volver_menu=int(input("desea regresar al menu? no:0 si:1    :"))
        elif main==3:
            salir=1
            volver_menu=1
        elif main==4:
            print("impresion de usuarios y claves")
            print(usuarios)
            volver_menu=1    
        else: 
            print("la opcion no es valida, vuelva a intentarlo")
            
            

                
          
