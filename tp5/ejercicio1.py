# tp5_punto1_cadena_responsabilidad.py

class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, number):
        raise NotImplementedError("Debe implementarse en subclases")


class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"{number} es par → Consumido por EvenHandler")
        elif self.next_handler:
            self.next_handler.handle(number)


class PrimeHandler(Handler):
    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def handle(self, number):
        if self.is_prime(number):
            print(f"{number} es primo → Consumido por PrimeHandler")
        elif self.next_handler:
            self.next_handler.handle(number)


class DefaultHandler(Handler):
    def handle(self, number):
        print(f"{number} no fue consumido por ningún handler")


if __name__ == "__main__":
    # Creamos la cadena: Par → Primo → Default
    handler_chain = EvenHandler(PrimeHandler(DefaultHandler()))

    # Procesamos del 1 al 100
    for num in range(1, 101):
        handler_chain.handle(num)
