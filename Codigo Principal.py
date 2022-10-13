from ast import Break
from Funciones import mostrarLetra, intervalo, modificar, almacenar, buscarPorTexto, eliminar

## Lista Principal [Titulo, Autor, Letra]
lista = [["Flaca", "Andres Calamaro", "Flaca no me claves \n Tus puñales \n Por la espalda \n Tan profundo \n No me duelen \n No me hacen mal \n Lejos \n En el centro \n De la tierra \n Las raíces \n Del amor \n Donde estaban \n Quedarán \n Entre el no me olvides \n Me dejes nuestros abriles olvidados \n En el fondo del placard \n Del cuarto de invitados \n Eran tiempos dorados \n De un pasado mejor \n Aunque casi me equivoco \n Y te digo poco a poco \n No me mientas \n No me digas la verdad \n No te quedes callada \n No levantes la voz \n Ni me pidas perdón \n Aunque casi te confieso \n Que también he sido un perro compañero \n Un perro ideal que aprendió a nadar \n Y a volver al hogar \n Para poder comer \n"], ["Oye Mi Amor", "Mana", "No sabes cómo te deseo \n No sabes cómo te he soñado \n Si tú supieras que me muero \n Por tu amor y por tus labios \n Si tú supieras que soy sincero \n Yo soy derecho y no te fallo \n Si tú supieras lo que te quiero \n Podría darte todo hasta mis ojos, eh \n Pero tú ya tienes otro \n Un tipo frío y aburrido \n Un tonto que es un reprimido \n Eso no te pega a ti \n No te va \n Oye mi amor, no me digas que no \n Y vamos juntando las almas \n Oye mi amor, no me digas que no \n Y vamos juntando los cuerpos \n Conmigo tú alucinarías, cómo no \n Conmigo tú hasta el fin del mundo \n Contigo yo me perdería \n Contigo yo quiero todo y nada a medias"], ["Por Mil Noches", "Airbag", "Yo sé que algunas veces \n  Me equivoco demasiado \n Yo sé que estás cansada \n De mirarme de costado \n Estoy arrepentido \n Y me gana la nostalgia \n Será que lo divino \n No mezcló muy bien las cartas \n Será cuestión de suerte \n Que sigamos separados \n Quisiera encerrarte \n Por mil noches, por mil años \n Sigo sin saber nada de vos \n En este \n Incendio \n Cada vez que estás cerca de mí \n Es un infierno \n Desde el día en que te conocí"], ["Jijiji", "Los Redondos de Ricota", "En este film velado en blanca noche \n El hijo tenaz de tu enemigo \n El muy verdugo cena distinguido \n Una noche de cristal que se hace añicos \n ¡No lo soñé! \n Ibas corriendo a la deriva \n ¡No lo soñé! \n Los ojos ciegos bien abiertos \n No mires, por favor \n Y no prendas la luz \n La imagen te desfiguró \n Este espejo da una imagen exquisita \n Esos pibes son como bombas pequeñitas \n El peor camino a la cueva del perico \n Para pibes que no duermen por la noche \n ¡No lo soñé! \n Se enderezó y brindó a tu suerte \n ¡No lo soñé! \n Y se ofreció mejor que nunca"], ["Cae el Sol", "Airbag", "Cae el sol en tu balcón \n Y el ritual se terminó \n La verdad es que no ha sido fácil, ah-ah \n La verdad es que no ha sido fácil para los dos \n Sigo aquí esperando por ti \n Yo quiero ir a algún lugar en donde pueda despertar \n Yo quiero verte sonreír y que no tengas que mentir \n Nos ves que estoy, estoy aquí dejando toda mi verdad \n No queda nadie en la ciudad pero por vos me quedo acá \n Esperando por ti \n Y no sé que fue de más \n Yo no sé que estuvo mal \n Y la luz me cegó en tu camino, ah-ah \n Descubrí, entendí el infinito entre los dos \n Sigo aquí esperando por ti"]]

## Funcion Principal (Eleccion segun el usuario)
def elecciones():
    try: 
        eleccion = int(input("\n Selecciona una opcion para continuar: \n 1- Ver letra de una cancion \n 2- Almacenar una cancion \n 3- Modificar una cancion existente \n 4- Eliminar una cancion del listado \n 5- Realizar una busqueda con texto \n 6- Salir del programa \n"))
        if eleccion == 1:
            mostrarLetra(lista)
            intervalo()
            listadoTotal(lista)
        elif eleccion == 2:
            almacenar(lista)
            intervalo()
            listadoTotal(lista)
        elif eleccion == 3:
            modificar(lista)
            intervalo()
            listadoTotal(lista)
        elif eleccion == 4:
            eliminar(lista)
            intervalo()
            listadoTotal(lista)
        elif eleccion == 5:
            buscarPorTexto(lista)
            intervalo()
            listadoTotal(lista)
        elif eleccion == 6:
            Break
        else:
            print("Error, La opcion debe ser un numero de la lista. \n Intentalo Nuevamente..")
            elecciones()
    except:
        print("Error, La opcion debe ser un numero de la lista. \n Intentalo Nuevamente..")
        elecciones()

## Funcion para mostrar el listado de Canciones [Titulo, Autor]
def listadoTotal(lista):
    print("\n Este es el listado total: \n Titulo, Autor:  \n")
    for i in lista: 
        print(lista.index(i)+1 , "-" , i[0] + ", " + i[1] )
    elecciones()
    
listadoTotal(lista)
