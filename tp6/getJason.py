import json
import sys

def main():
    if len(sys.argv) < 2:
        print("Uso: python getJason.py <archivo_json> [clave]")
        sys.exit(1)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2] if len(sys.argv) > 2 else 'token1'

    try:
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)

        if jsonkey in obj:
            print(obj[jsonkey])
        else:
            print(f"Clave '{jsonkey}' no encontrada en el archivo JSON.")
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo: {jsonfile}")
    except json.JSONDecodeError:
        print("Error al analizar el archivo JSON.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
