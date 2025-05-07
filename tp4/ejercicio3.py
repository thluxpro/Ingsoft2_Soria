class Componente:
    def mostrar(self, nivel=0):
        pass

class Pieza(Componente):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, nivel=0):
        print("  " * nivel + f"Pieza: {self.nombre}")

class SubConjunto(Componente):
    def __init__(self, nombre):
        self.nombre = nombre
        self.componentes = []

    def agregar(self, componente):
        self.componentes.append(componente)

    def mostrar(self, nivel=0):
        print("  " * nivel + f"SubConjunto: {self.nombre}")
        for componente in self.componentes:
            componente.mostrar(nivel + 1)

# Ensamblado principal
producto_principal = SubConjunto("Producto Principal")

for i in range(1, 4):
    subconjunto = SubConjunto(f"SubConjunto {i}")
    for j in range(1, 5):
        subconjunto.agregar(Pieza(f"Pieza {i}.{j}"))
    producto_principal.agregar(subconjunto)

# Agregar subconjunto opcional
sub_opcional = SubConjunto("SubConjunto Opcional")
for j in range(1, 5):
    sub_opcional.agregar(Pieza(f"Pieza O.{j}"))
producto_principal.agregar(sub_opcional)

# Mostrar estructura
producto_principal.mostrar()