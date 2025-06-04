#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
payment_processor.py

Copyright UADER-FCyT-IS2©2024 todos los derechos reservados.

Versión 1.2

Descripción:
    Automatiza la selección de cuenta para pagos usando JSON como fuente de tokens.
    Utiliza patrones Singleton, Chain of Responsibility e Iterator.
"""

import json
import os
import sys
from typing import List, Optional


class BaseJsonKeyFetcher:
    """Clase base para acceder a valores por clave desde un archivo JSON."""

    def get_key_value(self, key: str) -> str:
        raise NotImplementedError


class LegacyJsonKeyFetcher(BaseJsonKeyFetcher):
    """Implementación concreta que obtiene claves desde un archivo JSON."""

    def __init__(self, json_file: str):
        self.json_file = json_file
        self._data = {}
        self._load_data()

    def _load_data(self) -> None:
        try:
            with open(self.json_file, 'r', encoding='utf-8') as file:
                self._data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self._data = {}

    def get_key_value(self, key: str) -> str:
        return self._data.get(key, "Clave no encontrada")


class SingletonJsonFetcher:
    """Implementación Singleton para acceso único al fetcher."""

    _instance = None

    def __new__(cls, json_file: str) -> LegacyJsonKeyFetcher:
        if cls._instance is None:
            cls._instance = LegacyJsonKeyFetcher(json_file)
        return cls._instance


class Payment:
    """Clase que representa un pago realizado."""

    def __init__(self, order_number: int, token: str, amount: float):
        self.order_number = order_number
        self.token = token
        self.amount = amount

    def __str__(self) -> str:
        return f"Pedido #{self.order_number} | Token: {self.token} | Monto: ${self.amount:.2f}"


class PaymentIterator:
    """Iterador sobre la lista de pagos realizados."""

    def __init__(self, payments: List[Payment]):
        self._payments = payments
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self) -> Payment:
        if self._index < len(self._payments):
            pago = self._payments[self._index]
            self._index += 1
            return pago
        raise StopIteration


class AccountHandler:
    """Clase base para manejar pagos como parte de una cadena."""

    def __init__(self, token: str, initial_balance: float):
        self.token = token
        self.balance = initial_balance
        self.next_handler: Optional['AccountHandler'] = None

    def set_next(self, handler: 'AccountHandler') -> 'AccountHandler':
        self.next_handler = handler
        return handler

    def handle_payment(self, order_number: int, amount: float, processor: 'PaymentProcessor') -> bool:
        if self.balance >= amount:
            self.balance -= amount
            processor.register_payment(order_number, self.token, amount)
            return True
        if self.next_handler:
            return self.next_handler.handle_payment(order_number, amount, processor)
        return False


class PaymentProcessor:
    """Procesador principal de pagos."""

    def __init__(self, json_file: str):
        self.fetcher = SingletonJsonFetcher(json_file)
        self.payments: List[Payment] = []
        self.counter = 0

        # Setup de las cuentas con cadena de responsabilidad
        self.token1 = AccountHandler("token1", 1000.0)
        self.token2 = AccountHandler("token2", 2000.0)
        self.token1.set_next(self.token2)
        self.token2.set_next(self.token1)  # Para que sea una cadena circular

        self.next_handler = self.token1  # Inicio balanceado

    def make_payment(self, amount: float) -> None:
        """Realiza un pago de monto fijo si alguna cuenta tiene saldo."""
        self.counter += 1
        success = self.next_handler.handle_payment(self.counter, amount, self)
        if not success:
            print(f"Pedido #{self.counter}: Error - Fondos insuficientes.")
        else:
            # Alternamos entre cuentas para balancear
            self.next_handler = self.next_handler.next_handler

    def register_payment(self, order_number: int, token: str, amount: float) -> None:
        """Registra un pago exitoso."""
        payment = Payment(order_number, token, amount)
        print(payment)
        self.payments.append(payment)

    def listar_pagos(self) -> None:
        """Lista todos los pagos realizados en orden cronológico."""
        print("\nListado de pagos realizados:")
        for pago in PaymentIterator(self.payments):
            print(pago)


def mostrar_version() -> None:
    """Muestra la versión del programa."""
    print("payment_processor.py versión 1.2")


def main():
    """Ejecuta una simulación de pagos de $500 desde un archivo JSON."""
    if len(sys.argv) < 2:
        print("Uso: python payment_processor.py <sitedata.json> [-v]")
        return

    if sys.argv[1] == "-v":
        mostrar_version()
        return

    json_file = sys.argv[1]

    if not os.path.isfile(json_file):
        print("Archivo JSON no encontrado.")
        return

    processor = PaymentProcessor(json_file)

    # Simulación de 6 pagos de $500
    for _ in range(6):
        processor.make_payment(500)

    processor.listar_pagos()


if __name__ == '__main__':
    main()
