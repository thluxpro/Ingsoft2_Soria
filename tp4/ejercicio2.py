from abc import ABC, abstractmethod

# Implementor
class TrenLaminador(ABC):
    @abstractmethod
    def producir(self, lamina_id):
        pass

# ConcreteImplementor A
class Tren5m(TrenLaminador):
    def producir(self, lamina_id):
        print(f"Lámina {lamina_id}: producida en tren de 5 metros")

# ConcreteImplementor B
class Tren10m(TrenLaminador):
    def producir(self, lamina_id):
        print(f"Lámina {lamina_id}: producida en tren de 10 metros")

# Abstraction
class Lamina:
    def __init__(self, id_lamina, tren: TrenLaminador):
        self.id = id_lamina
        self.tren = tren

    def producir(self):
        self.tren.producir(self.id)

# ---------- Pruebas ----------
if __name__ == "__main__":
    # Crear trenes
    tren_corto = Tren5m()
    tren_largo = Tren10m()

    # Crear láminas y asignar trenes
    lamina1 = Lamina("A001", tren_corto)
    lamina2 = Lamina("A002", tren_largo)

    # Producir láminas
    lamina1.producir()  # Usará el tren de 5 metros
    lamina2.producir()  # Usará el tren de 10 metros