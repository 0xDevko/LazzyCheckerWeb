import argparse
import requests
from requests.exceptions import RequestException
import time
import os

def cargar_menu_diccionario(wordlist_path):
    try:
        with open(wordlist_path, "r") as archivo:
            rutas = archivo.readlines()
            rutas = [ruta.strip() for ruta in rutas if ruta.strip()] 
            return rutas
    except FileNotFoundError:
        print(f"The file '{wordlist_path}' not found.")
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


def main():
    parser = argparse.ArgumentParser(
        description="🔗 LazzyCheckerWeb: Brute-force endpoint checker for websites"
    )
    parser.add_argument(
        "-u", "--url", required=True,
        help="Base URL of the target website (e.g., https://example.com)"
    )
    parser.add_argument(
        "-w", "--wordlist", required=True,
        help="Path to the wordlist file containing endpoint candidates"
    )

    args = parser.parse_args()
    list_rutas = cargar_menu_diccionario(args.wordlist)
    os.system("clear")
    print(f"Throwing checks at: {args.url}")
    execute(args.url, list_rutas)

if __name__ == "__main__":
    main()