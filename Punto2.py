from super_lista import Superhero
from super_heroes_data import superheroes
from lista import List
from cola import Queue

lista_super = List()

for superhero in superheroes:
    hero = Superhero(
        name=superhero["name"],
        alias=superhero["alias"],
        real_name=superhero["real_name"],
        short_bio=superhero["short_bio"],
        first_appearance=superhero["first_appearance"],
        is_villain=superhero["is_villain"],
    )
    lista_super.append(hero)

# Listado ordenado de manera ascendente por nombre de los personajes.

def super_nombre (item):
    return item.name

lista_super.add_criterion("supnombre",super_nombre)

lista_super.sort_by_criterion("supnombre")

for hero in lista_super:
    print(hero)

print()

# Determinar en que posicion esta The Thing y Rocket Raccoon.

def buscar_posicion (lista = List(), personaje = str):
    lista.sort_by_criterion("supnombre")
    posicion = lista.search(personaje, "supnombre")
    return posicion

personaje = "The Thing"
buscar_personaje = buscar_posicion(lista_super, personaje)

print(f"{personaje} se encuentra en la posición: {buscar_personaje}")

personaje = "Rocket Raccoon"
buscar_personaje = buscar_posicion(lista_super, personaje)

print(f"{personaje} se encuentra en la posición: {buscar_personaje}")
print()

# Listar todos los villanos de la lista.

def listar_villanos (lista = List()):
    lista_aux = List()
    for hero in lista:
        if hero.is_villain == True:
            lista_aux.append(hero)
    if len(lista_aux)>0:
        return lista_aux
    else:
        return 0

lista_villanos = listar_villanos(lista_super)

for villano in lista_villanos:
    print(villano)

print()

# Poner todos los villanos en una cola para determinar luego cuales aparecieron antes de 1980.
cola_villanos = Queue()

for villano in lista_villanos:
    cola_villanos.arrive(villano)
    
print()

# EListar los superheores que comienzan con  Bl, G, My, y W.

def buscar_antes_año (cola = Queue(), año = int):
    cola_aux = Queue()
    for i in range (cola.size()):
        on_front = cola.on_front()
        if on_front.first_appearance<= año:
            cola_aux.arrive(on_front)
            cola.move_to_end()
    if cola_aux.size()>0:
        return cola_aux
    else:
        return 0
    
busqueda_año = buscar_antes_año(cola_villanos, 1980)
print("busqueda por año:")
busqueda_año.show()
    
def buscar_por_letra_nombre(lista, inicial):
    lista_aux = List()
    for hero in lista:
        if hero.name.startswith(inicial):
            lista_aux.append(hero)
    return(lista_aux)

buscar_inicial = buscar_por_letra_nombre(lista_super, "Bl")

for hero in buscar_inicial:
    print (hero)

print()

buscar_inicial = buscar_por_letra_nombre(lista_super, "G")

for hero in buscar_inicial:
    print (hero)

print()

buscar_inicial = buscar_por_letra_nombre(lista_super, "My")

for hero in buscar_inicial:
    print (hero)

print()

buscar_inicial = buscar_por_letra_nombre(lista_super, "W")

for hero in buscar_inicial:
    print (hero)

print()

# Listado de personajes ordenado por nombre real de manera ascendente de los personajes.

def sort_by_realname(item):
    return item.real_name if item.real_name is not None else ""

lista_super.add_criterion("realnombre", sort_by_realname)
lista_super.sort_by_criterion("realnombre")
lista_super.show()
print()

# Listado de superheroes ordenados por fecha de aparación.

def ordenar_por_fecha(item):
    return item.first_appearance

lista_super.add_criterion("porfecha", ordenar_por_fecha)
lista_super.sort_by_criterion("porfecha")
lista_super.show()
print()

# Modificar el nombre real de Ant Man a Scott Lang.

def modificar_nombre(lista = List, nombre_super = str, nombre_cambiar = str):
    for hero in lista:
       
        if hero.name == nombre_super:
            print(hero)
            hero.real_name = nombre_cambiar
            return hero
    print("No se encontró el héroe.")

    
cambiar_nombre = modificar_nombre(lista_super, "Ant Man", "Scott Lang")

print(cambiar_nombre)

#I Mostrar los personajes que en su biografia incluyan la palabra time-traveling o suit.

def buscar_por_bio (lista, inicial):
    lista_aux = List()
    for hero in lista:
        if inicial in hero.short_bio:
            lista_aux.append(hero)
    if len(lista_aux) > 0:
        return lista_aux
    else:
        return "0"
    
busqueda_bio = buscar_por_bio(lista_super, "time-traveling")

for hero in busqueda_bio:
    print(hero)

print()

busqueda_bio = buscar_por_bio(lista_super, "suit")

for hero in busqueda_bio:
    print(hero)

print()

# Eliminar a Electro y Baron Zemo de la lista y mostrar su información si estaba en la lista.

hero = lista_super.delete_value("Electro", "supnombre")

if hero is not None:
    print(hero)

hero = lista_super.delete_value("Baron Zemo", "supnombre")

if hero is not None:
    print(hero)