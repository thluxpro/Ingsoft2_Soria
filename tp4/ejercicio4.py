class Numero:
    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):
        print(f"Valor: {self.valor}")
        return self.valor

class DecoradorNumero:
    def __init__(self, numero):
        self.numero = numero

    def mostrar(self):
        return self.numero.mostrar()

class Sumar2(DecoradorNumero):
    def mostrar(self):
        val = super().mostrar()
        val += 2
        print(f" +2 = {val}")
        return val

class Multiplicar2(DecoradorNumero):
    def mostrar(self):
        val = super().mostrar()
        val *= 2
        print(f" *2 = {val}")
        return val

class Dividir3(DecoradorNumero):
    def mostrar(self):
        val = super().mostrar()
        val /= 3
        print(f" /3 = {val}")
        return val

# prueba
num = Numero(6)
print("Sin decorador:")
num.mostrar()

print("\nCon decoradores anidados:")
decorado = Dividir3(Multiplicar2(Sumar2(num)))
decorado.mostrar()