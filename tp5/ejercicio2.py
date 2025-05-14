# tp5_punto2_iterator.py

class StringContainer:
    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return ForwardIterator(self.text)

    def reverse_iter(self):
        return ReverseIterator(self.text)


class ForwardIterator:
    def __init__(self, text):
        self.text = text
        self.index = 0

    def __next__(self):
        if self.index >= len(self.text):
            raise StopIteration
        result = self.text[self.index]
        self.index += 1
        return result

    def __iter__(self):
        return self


class ReverseIterator:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        result = self.text[self.index]
        self.index -= 1
        return result

    def __iter__(self):
        return self


if __name__ == "__main__":
    cadena = StringContainer("Ingeniería")

    print("→ Recorriendo en forma directa:")
    for char in cadena:
        print(char, end=' ')
    
    print("\n\n→ Recorriendo en forma inversa:")
    for char in cadena.reverse_iter():
        print(char, end=' ')
