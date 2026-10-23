# type: ignore

class Vagon:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None

vagon1 = Vagon(1)
vagon2 = Vagon(2)
vagon3 = Vagon(3)
vagon4 = Vagon(4)

locomotora = vagon1
vagon1.siguiente = vagon2
vagon2.siguiente = vagon3
vagon3.siguiente = vagon4

actual = locomotora
while actual is not None:
    print(actual.numero, end="->")
    actual = actual.siguiente

print("None")