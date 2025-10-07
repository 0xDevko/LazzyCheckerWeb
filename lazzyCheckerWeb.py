import requests
from requests.exceptions import RequestException
import time
import os

def cargar_menu_diccionario():
    print("Specify the dictionary path")
    path_dic = input()
    try:
        with open(path_dic, "r") as archivo:
            rutas = archivo.readlines()
            rutas = [ruta.strip() for ruta in rutas if ruta.strip()] 
            return rutas
    except FileNotFoundError:
        print(f"The file '{path_dic}' not found.")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []


def comprobar_ruta(url, timeout=5):
    try:
        respuesta = requests.get(url, timeout=timeout)
        return respuesta.status_code, respuesta.reason
    except RequestException as e:
        return None, str(e)

def execute(path, list_rutes):
    resultados = []
    for url in list_rutes:
        final_path = path + url
        print(f"➡️ Check: {final_path}")
        codigo, mensaje = comprobar_ruta(final_path)
        if codigo != 404:
            estado = f"✅ {codigo} {mensaje}"
        else:
            estado = f"❌ Error: {codigo} {mensaje}"
        resultados.append((final_path, estado))
        time.sleep(0.5)

    print("\n📋 Results:")
    for final_path, estado in resultados:
        print(f"{final_path} → {estado}")



list_rutas = cargar_menu_diccionario()
print("Specify the base URL to check: ")
 
path = input()
os.system("clear")
print(f"Throwing checks at: {path}")
execute(path, list_rutas)
