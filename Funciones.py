## Funcion de intervalo para dejar una pausa antes de correr denuevo el Menu Principal
def intervalo():
    input("\n Ingrese cualquier caracter para volver al Menu Principal \n")

## Funcion para mostrar la letra de alguna cancion
def mostrarLetra(lista):
    seleccion=int(input("Selecciona el titulo, artista deseado "))
    print("\n " + lista[seleccion-1][2] + "\n")
    
## Funcion para modificar algun elemento de la Lista
def modificar(lista):
    for i in lista: 
        print(lista.index(i)+1 , "-" , i[0] + ", " + i[1] )
        eleccion = int(input("Seleccione que cancion desea modificar: "))
        print("\n Selecciono: ", lista[eleccion-1][0], "-",  lista[eleccion-1][1])
        opcion = int(input("\n Selecciona que categoria: \n 1- Titulo \n 2- Autor \n 3- Letra "))
        cambio = input("Ingrese la modificacion: ")
        lista[eleccion-1][opcion-1] = cambio

## Funcion para almacenar algun elemento en la Lista
def almacenar(lista):
    estructura = ["Titulo", "Autor", "Letra"]
    nuevaCancion = []
    for i in estructura:
        i = input("Ingrese " + i)
        nuevaCancion.append(i)
    lista.append(nuevaCancion)

## Funcion para eliminar algun elemento de la Lista
def eliminar(lista):
    opcion=int(input("\n Seleccione la cancion que desea eliminar: "))
    eliminado = lista.pop(opcion-1)
    print("\n Se elimino la cancion: " , eliminado[0], " del autor: ", eliminado[1] , " exitosamente.")

## Funcion para buscar por texto
def buscarPorTexto(lista):
    texto = str(input("\n Ingrese el nombre de la cancion: \n"))
    encontrado = False
    for i in lista:
        if (texto in i[0]):
            encontrado = True
            indice = i
    if encontrado == True:
        print("\n Su cancion es la numero", lista.index(indice)+1 , "-", indice[0])
    else:
        print("\n No se encontro la cancion")