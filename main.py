from nlt import numlet as converter

while(True):
    #Espera un valor de entrada por teclado
    number = input("Ingresa un numero \n")

    #Evalua la entrada para detener el ciclo while
    if(number=="salir" or number=="Salir"):
        break

    #El bloque try es para validar que por ejemplo no sean letras 
    #Cualquier instruccion que falle sera interceptada por 
    #El bloque except
    try:
        #Recibe como parametro el numero y ejecuta el metodo a letras
        #Este regresa el resultado de el numero en palabras
        resultado = converter.Numero(number).a_letras

        #Imprime el resultado
        print("El numero es: " + resultado) 
        print("\n")
    except:
        #Mensaje generico en caso de tener algun error en la ejecucion
        #del bloque que transforma el numero a palabras
        print("El numero no puede ser transformado a letras")
        print("\n")
