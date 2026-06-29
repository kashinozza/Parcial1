lista_superheros = [ "Spider-Man", "Batman", "Superman","Iron Man","Thor","Hulk","Capitan America","Black Widow","Doctor Strange","Wolverine","Flash", "Wonder Woman","Aquaman","Green Lantern","Black Panther"]

def buscar_heroe (lista, hero_buscar):
    if len(lista)<=0:
        return False
    else:
        heroe = lista[0]
        if heroe == hero_buscar:
            return True
        else:
            return buscar_heroe(lista[1:], hero_buscar)
        
hero = "Capitan America"

busqueda = buscar_heroe(lista_superheros, hero)

if busqueda == True:
    print("El personaje está en la lista.")
else:
    print("El personaje no está en la lista.")

def listar (lista):
    if len(lista)==0:
        return 
    else:
        print(lista[0])
        listar(lista[1:])

listar(lista_superheros)