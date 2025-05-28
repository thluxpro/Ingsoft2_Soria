
"""
get_jason.py

Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.

Descripción:
    Recupera el valor de una clave desde un archivo JSON.
    Aplica POO, patrón Singleton y manejo robusto de errores.
    Versión: 1.1
"""

import json
import sys
import os


class BaseJsonKeyFetcher:
    """Clase base abstracta para recuperar claves desde un archivo JSON."""

    def get_key_value(self, key: str) -> str:
        """Devuelve el valor de la clave si existe, o un mensaje de error."""
        raise NotImplementedError


# pylint: disable=too-few-public-methods
class LegacyJsonKeyFetcher(BaseJsonKeyFetcher):
    """Implementación legada que lee un JSON y devuelve el valor asociado a una clave."""

    def __init__(self, json_file: str):
        """Inicializa con el nombre del archivo y carga el contenido."""
        self.json_file = json_file
        self._data = None
        self._load_data()

    def _load_data(self) -> None:
        """Carga los datos del archivo JSON."""
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                self._data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self._data = None

    def get_key_value(self, key: str) -> str:
        """Devuelve el valor de la clave o un mensaje si no se encuentra."""
        if not self._data:
            return "Error: No se pudo cargar el archivo JSON."
        return self._data.get(key, f"Clave '{key}' no encontrada en el archivo.")


# pylint: disable=too-few-public-methods
class SingletonJsonFetcher:
    """Clase Singleton que devuelve una única instancia de LegacyJsonKeyFetcher."""

    _instance = None

    def __new__(cls, json_file: str) -> LegacyJsonKeyFetcher:
        """Crea una única instancia de LegacyJsonKeyFetcher."""
        if cls._instance is None:
            cls._instance = LegacyJsonKeyFetcher(json_file)
        return cls._instance


def mostrar_version() -> None:
    """Muestra la versión del programa."""
    print("getJason.py versión 1.1")


def mostrar_uso() -> None:
    """Muestra instrucciones de uso del programa."""
    print("Uso:")
    print("  python get_jason.py <archivo_json> [clave]")
    print("  python get_jason.py -v")


def main() -> None:
    """Punto de entrada principal del programa."""
    args = sys.argv[1:]

    if not args:
        mostrar_uso()
        return

    if args[0] == '-v':
        mostrar_version()
        return

    if len(args) > 2 or not os.path.isfile(args[0]):
        print("Error: Argumentos inválidos o archivo no encontrado.")
        mostrar_uso()
        return

    json_file = args[0]
    key = args[1] if len(args) == 2 else 'token1'

    fetcher: LegacyJsonKeyFetcher = SingletonJsonFetcher(json_file)
    resultado = fetcher.get_key_value(key)
    print(resultado)


if __name__ == '__main__':
    main()
