# ****** CLASE NODO ******
class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.carnet})"


# ****** CLASE LISTA DOBLEMENTE ENLAZADA ******
from graphviz import Digraph

class ListaDoble:
    def __init__(self):
        self.inicio = None
        self.fin = None

    # Insertar al principio
    def agregar_inicio(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)
        if self.inicio is None:
            self.inicio = self.fin = nuevo
        else:
            nuevo.siguiente = self.inicio
            self.inicio.anterior = nuevo
            self.inicio = nuevo
        print("Nodo agregado al inicio.")
        self.graficar()

    # Insertar al final
    def agregar_final(self, nombre, apellido, carnet):
        nuevo = Nodo(nombre, apellido, carnet)
        if self.fin is None:
            self.inicio = self.fin = nuevo
        else:
            self.fin.siguiente = nuevo
            nuevo.anterior = self.fin
            self.fin = nuevo
        print("Nodo agregado al final.")
        self.graficar()

    # Eliminar por carnet
    def eliminar(self, carnet):
        actual = self.inicio
        while actual:
            if actual.carnet == carnet:
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                else:
                    self.inicio = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                else:
                    self.fin = actual.anterior
                print(f"Nodo con carnet {carnet} eliminado.")
                self.graficar()
                return
            actual = actual.siguiente
        print("No se encontró un nodo con ese carnet.")

    # Mostrar lista hacia adelante
    def mostrar(self):
        actual = self.inicio
        resultado = "None <- "
        while actual:
            resultado += f"[{actual}] <-> "
            actual = actual.siguiente
        resultado += "None"
        print(resultado)

    # Graficar con Graphviz
    def graficar(self, nombre="lista_doble"):
        dot = Digraph(comment="Lista doblemente enlazada")
        actual = self.inicio
        while actual:
            dot.node(str(id(actual)), str(actual))
            if actual.siguiente:
                dot.edge(str(id(actual)), str(id(actual.siguiente)), dir="both")
            actual = actual.siguiente
        dot.render(nombre, format="png", cleanup=True)
        print(f"Gráfico actualizado: {nombre}.png")


# ****** MENÚ PRINCIPAL ******
def menu():
    lista = ListaDoble()
    while True:
        print("\n========= MENÚ =========")
        print("1. Insertar al principio")
        print("2. Insertar al final")
        print("3. Eliminar por carnet")
        print("4. Mostrar lista")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.agregar_inicio(nombre, apellido, carnet)

        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            carnet = input("Carnet: ")
            lista.agregar_final(nombre, apellido, carnet)

        elif opcion == "3":
            carnet = input("Carnet a eliminar: ")
            lista.eliminar(carnet)

        elif opcion == "4":
            lista.mostrar()

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


# ****** EJECUCIÓN ******
if __name__ == "__main__":
    menu()
