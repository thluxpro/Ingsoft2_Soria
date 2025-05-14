# tp5_punto3_observer.py

class Subject:
    def __init__(self):
        self.observers = []

    def subscribe(self, observer):
        self.observers.append(observer)

    def unsubscribe(self, observer):
        self.observers.remove(observer)

    def emit_id(self, emitted_id):
        print(f"\n→ Emitiendo ID: {emitted_id}")
        for observer in self.observers:
            observer.notify(emitted_id)


class Observer:
    def __init__(self, id_code):
        self.id_code = id_code

    def notify(self, emitted_id):
        if self.id_code == emitted_id:
            print(f"✔ Coincidencia: {self.id_code} recibió su ID.")
        else:
            print(f"✖ {self.id_code} no coincide.")


if __name__ == "__main__":
    # Crear el sujeto
    broadcaster = Subject()

    # Crear observadores con sus IDs
    obs1 = Observer("A123")
    obs2 = Observer("B456")
    obs3 = Observer("C789")
    obs4 = Observer("D000")

    # Suscribir los observadores
    broadcaster.subscribe(obs1)
    broadcaster.subscribe(obs2)
    broadcaster.subscribe(obs3)
    broadcaster.subscribe(obs4)

    # Emitir 8 IDs (4 deben coincidir con los observadores)
    ids_to_emit = ["A123", "ZZZZ", "B456", "Y123", "C789", "X000", "W321", "D000"]

    for id_code in ids_to_emit:
        broadcaster.emit_id(id_code)
