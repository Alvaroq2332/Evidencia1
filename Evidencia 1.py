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
def MostrarCatalagoCompleto():
    print()
    print("**Catálogo completo***")
    print(f"{'Titulo':15}|{'Autor':20}|{'Genero':10}|{'Año Publicacion':<18}|{'ISBN':13}|{'AÑO Adquisicion'}")
    for libro in libros.values(): #Busqueda de los datos por medio de posiciones en la lista
        print(f"{libro[0]:15}|{libro[1]:<20}|{libro[2]:<10}|{libro[3]:<18}|{libro[4]:<13}|{libro[5]} ")
#Funcion debusqueda por autor
def ReportePorAutor():
    autores=list()
    print()
    print("**Reporte por autor***")
    
    #Muestra todos los autores de libros sin repetirlos
    autores=list()
    for libro in libros.values():
        autores.append(libro[1])
        for autor in autores:
            if autores.count(autor)>1:
                autores.remove(autor)
    print("---AUTORES DISPONIBLES----")
    for autor in autores:
        print(f"-{autor}")
    
    #Consulta
    autor=input("Ingrese el nombre del autor: ")
    autorBuscado=autor.upper()
    try:
        print()
        print(f"{'Titulo':15}|{'Autor':20}|{'Genero':10}|{'Año Publicacion':<18}|{'ISBN':13}|{'AÑO Adquisicion'}")
        for libro in libros.values():
            if libro[1]==autorBuscado:
                print(f"{libro[0]:15}|{libro[1]:<20}|{libro[2]:<10}|{libro[3]:<18}|{libro[4]:<13}|{libro[5]} ")
    except:
        pass

#Funcion busqueda por genero
def ReportePorGenero():
    print()
    print("**Reporte por genero***")
    
    #Muestra todos los autores de libros sin repetirlos
    generos=list()
    for libro in libros.values():
        generos.append(libro[2])
        for genero in generos:
            if generos.count(genero)>1:
                generos.remove(genero)
    print("---GENEROS DISPONIBLES----")
    for genero in generos:
        print(f"-{genero}")
    
    #Consulta
    genero=input("Ingrese el genero: ")
    generoBuscado=genero.upper()
    try:
        print()
        print(f"{'Titulo':15}|{'Autor':20}|{'Genero':10}|{'Año Publicacion':<18}|{'ISBN':13}|{'AÑO Adquisicion'}")
        for libro in libros.values():
            if libro[2]==generoBuscado:
                print(f"{libro[0]:15}|{libro[1]:<20}|{libro[2]:<10}|{libro[3]:<18}|{libro[4]:<13}|{libro[5]} ")
    except:
        pass

#Funcion busqueda por año
def ReportePorAño():
    print()
    print("**Reporte por año de publicacion***")
    
    #Muestra todos los autores de libros sin repetirlos
    años=list()
    for libro in libros.values():
        años.append(libro[3])
        for año in años:
            if años.count(año)>1:
                años.remove(año)
    print("---GENEROS DISPONIBLES----")
    for año in años:
        print(f"-{año}")

    #Consulta
    año=input("Ingrese el año: ")
    añoBuscado=año.upper()
    try:
        print()
        print(f"{'Titulo':15}|{'Autor':20}|{'Genero':10}|{'Año Publicacion':<18}|{'ISBN':13}|{'AÑO Adquisicion'}")
        for libro in libros.values():
            if libro[3]==añoBuscado:
                print(f"{libro[0]:15}|{libro[1]:<20}|{libro[2]:<10}|{libro[3]:<18}|{libro[4]:<13}|{libro[5]} ")
    except:
        pass

# Sub menu de Reportes
def Reportes():
    while True:
        print()
        print("**Reportes**")
        print("1 Catalago completo")
        print("2 Reporte por autor")
        print('3 Reporte por genero')
        print('4 Reporte por año de publicación')
        print('5 Regresar al menu anterior')
        eleccion=int(input("Selecciona una opcion: "))
        if eleccion==1:
            MostrarCatalagoCompleto()
        if eleccion==2:
            ReportePorAutor()
        if eleccion==3:
            ReportePorGenero()
        if eleccion==4:
            ReportePorAño()
        if eleccion==5:
            break



def BusquedaPorTitulo():
    print()
    print("**Busqueda por titulo***")
    titulos=list()
    for libro in libros.values():
        titulos.append(libro[0])
        for titulo in titulos:
            if titulos.count(titulo)>1:
                titulos.remove(titulo)
    print("-----TITULOS DISPONIBLES-----")
    for titulo in titulos:
        print(f"-{titulo}")
    #Consulta
    titulo=input("Ingrese el titulo del libro: ")
    tituloBuscado=titulo.upper()
    try:
        print()
       print(f"{'Titulo':15}|{'Autor':20}|{'Genero':10}|{'Año Publicacion':<18}|{'ISBN':13}|{'AÑO Adquisicion'}")
        for libro in libros.values():
            if libro[0]==tituloBuscado:
                print(f"{libro[0]:15}|{libro[1]:<20}|{libro[2]:<10}|{libro[3]:<18}|{libro[4]:<13}|{libro[5]} ")
    except:
        pass
    
def BusquedaPorISBN(): 

    print() 

    print("**Búsqueda por ISBN***") 

 

    #Consulta 

    isbn=input("Ingrese el ISBN del libro: ") 

    try: 

        print() 

        print(f"{'Titulo':15}|{'Autor':20}|{'Genero':10}|{'Año Publicacion':<18}|{'ISBN':13}|{'AÑO Adquisicion'}") 

        for libro in libros.values(): 

            if libro[4]==isbn: 

                print(f"{libro[0]:15}|{libro[1]:<20}|{libro[2]:<10}|{libro[3]:<18}|{libro[4]:<13}|{libro[5]} ") 

    except: 

        pass 

 

#Sub menu para la busqueda por título y ISBN 

def TituloYIsbn(): 

    while True: 

        print() 

        print("***Consulta por título y ISBN*") 

        print() 

        print("1 busqueda por Título") 

        print("2 Busqueda por ISBN") 

        print("3 Volver al menú principal") 

        eleccion=int(input("Elige una opción: ")) 

        if eleccion==1: 

            BusquedaPorTitulo() 

        if eleccion==2: 

            BusquedaPorISBN() 

        if eleccion==3: 

            break 

 

#Submenu de consultas y reportes  

def ConsultaYReportes(): 

    while True: 

        print() 

        print("****CONSULTA Y REPORTES*****") 

         

        print("1 Consulta de título y ISBN") 

        print("2 Reportes") 

        print("3 Volver al menú principal") 

        eleccion=int(input("Elige una opción: ")) 

        if eleccion==1: 

            TituloYIsbn() 

        if eleccion==2: 

            Reportes() 

        if eleccion==3: 

            Break 
