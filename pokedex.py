import os
import requests
import json

def obtener_datos_pokemon(nombre_pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}" #Se define la variable que estará ligada a la PokeApi
    respuesta = requests.get(url)
    datos = respuesta.json() 
    if 'detail' in datos:
        raise ValueError("El Pokémon especificado no existe.")
    return datos

def mostrar_info_pokemon(datos): #Se buscan en el formato json los datos que queremos saber del Pokemon ingresado
    print(f"Nombre: {datos['name'].capitalize()}")
    print(f"Da click para ver a tu Pokemon: {datos['sprites']['front_default']}")
    print("Estadísticas:")
    for stat in datos['stats']:
        print(f"- {stat['stat']['name'].capitalize()}: {stat['base_stat']}")
    print("Peso:", datos['weight'])
    print("Tamaño:", datos['height'])
    print("Movimientos:")
    for move in datos['moves']:
        print("- " + move['move']['name'].capitalize())
    print("Habilidades:")
    for ability in datos['abilities']:
        print("- " + ability['ability']['name'].capitalize())
    print("Tipos:")
    for type_info in datos['types']:
        print("- " + type_info['type']['name'].capitalize())

def guardar_datos_json(datos): #Utilizamos la libreria OS para manipular la ruta y crear un directorio
    if not os.path.exists("pokedex"):
        os.makedirs("pokedex")
    with open(f"pokedex/{datos['name']}.json", 'w') as json_file:
        json.dump(datos, json_file, indent=4)
    print("Datos guardados en:", f"pokedex/{datos['name']}.json") #Se crea una liga para abrir el archivo json en el mismo editor

def main():
    nombre_pokemon = input("Introduce el nombre de un Pokémon: ")
    try:
        datos = obtener_datos_pokemon(nombre_pokemon)
        mostrar_info_pokemon(datos)
        guardar_datos_json(datos)
    except ValueError:
        print("Error, ingresa un Pokemon existente") #Aqui verificamos que el nombre este bien escrito, de lo contrario arroja un error. 
    except requests.exceptions.RequestException as e:
        print("Error al conectarse a la API:", e)#En este se verifica cualquier otro error y da la descripcion de cual es (Desconexion a internet, servidor etc.)

if __name__ == "__main__":
    main()