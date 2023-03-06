libros=dict()

def RegistrarNuevoEjempar():
    while True:
        global identificador
        print("")
        print("****Registrar Libro*****")
        #Generacion de llaves de diccionario; si ya hay llaves en el diccionario añade 1 mas al conteo, si no, asigna la primera lista primero con el numero 1
        if libros.keys():
            identificador=max(libros.keys())+1
        else:
            identificador=1
        print()
        
        #Entrada de datos para el registro de libro
        titulo=input("Ingresa el titulo: ")
        titulo=titulo.upper()
        
        autor=input("Ingresa el autor: ")
        autor=autor.upper()
        
        genero=input("Ingresa el genero: ")
        genero=genero.upper()
        
        
        añoPublic=input("Ingresa el año de publicacion: ")
        
        isbn=input("Ingresa el ISBN: ")
        isbn=isbn.upper()

        fechAdqui=input("Ingresa el año de adquisicion: ")
        
        #Datos ingresados almacenados en la lista "ejemplar"
        ejemplar=(titulo,autor,genero,añoPublic,isbn,fechAdqui)
        
        #Lista ejemplar guardada en el diccionario de "libros"
        libros[identificador]=ejemplar
        
        
        agregar=input("Desea agregar otro libro? [S/N]: ")
        agregar=agregar.upper()
        
        if agregar=="S":
            pass
        elif agregar=="N":
            break
        else:
            print("opcion no valida")