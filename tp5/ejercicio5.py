import os

#*--------------------------------------------------------------------
#* Design pattern memento, TP5 modificado
#*--------------------------------------------------------------------

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content


class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content


class FileWriterCaretaker:
    def __init__(self):
        self.mementos = []

    def save(self, writer):
        if len(self.mementos) == 4:
            self.mementos.pop()  # Quita el más viejo (al final)
        self.mementos.insert(0, writer.save())  # Inserta el nuevo al inicio

    def undo(self, writer, index=0):
        if 0 <= index < len(self.mementos):
            writer.undo(self.mementos[index])
        else:
            print(f"No hay estado guardado para index {index}")


if __name__ == '__main__':
    os.system("clear")
    caretaker = FileWriterCaretaker()
    writer = FileWriterUtility("GFG.txt")

    print("→ Escribiendo versión 1")
    writer.write("Clase de IS2 en UADER\n")
    caretaker.save(writer)
    print(writer.content)

    print("\n→ Escribiendo versión 2")
    writer.write("Material adicional de la clase de patrones\n")
    caretaker.save(writer)
    print(writer.content)

    print("\n→ Escribiendo versión 3")
    writer.write("Más material\n")
    caretaker.save(writer)
    print(writer.content)

    print("\n→ Escribiendo versión 4")
    writer.write("Y más todavía\n")
    caretaker.save(writer)
    print(writer.content)

    print("\n→ Escribiendo versión 5 (ya excede 4 guardados)")
    writer.write("Esto reemplazará al más viejo\n")
    caretaker.save(writer)
    print(writer.content)

    print("\n→ Undo al estado anterior inmediato (index 0)")
    caretaker.undo(writer, 0)
    print(writer.content)

    print("\n→ Undo al segundo estado anterior (index 1)")
    caretaker.undo(writer, 1)
    print(writer.content)

    print("\n→ Undo al tercer estado anterior (index 2)")
    caretaker.undo(writer, 2)
    print(writer.content)

    print("\n→ Undo al cuarto estado anterior (index 3)")
    caretaker.undo(writer, 3)
    print(writer.content)

    print("\n→ Intento de undo fuera de rango")
    caretaker.undo(writer, 4)
