class Nodo:
    def __init__(self, valor=None):
        self.valor = valor  
        self.siguiente = None  
        self.anterior = None  

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None  
        self.cola = None  
        self.cursor = None  

    def insertar_al_inicio(self, valor):
        """Inserta un carácter al principio de la lista."""
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            
            self.cabeza = self.cola = nuevo_nodo
            self.cursor = nuevo_nodo
        else:
            
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            self.cursor = nuevo_nodo

    def insertar_al_final(self, valor):
        """Inserta un carácter al final de la lista."""
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            
            self.cabeza = self.cola = nuevo_nodo
            self.cursor = nuevo_nodo
        else:
          
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def eliminar(self):
        """Elimina el carácter en la posición del cursor."""
        if self.cursor:
            if self.cursor == self.cabeza and self.cursor == self.cola:
               
                self.cabeza = self.cola = self.cursor = None
            elif self.cursor == self.cabeza:
              
                self.cabeza = self.cabeza.siguiente
                self.cabeza.anterior = None
                self.cursor = self.cabeza
            elif self.cursor == self.cola:
               
                self.cola = self.cola.anterior
                self.cola.siguiente = None
                self.cursor = self.cola
            else:
               
                self.cursor.anterior.siguiente = self.cursor.siguiente
                self.cursor.siguiente.anterior = self.cursor.anterior
                self.cursor = self.cursor.siguiente

    def mover_cursor_adelante(self):
        """Mueve el cursor una posición hacia adelante."""
        if self.cursor and self.cursor.siguiente:
            self.cursor = self.cursor.siguiente

    def mover_cursor_atras(self):
        """Mueve el cursor una posición hacia atrás."""
        if self.cursor and self.cursor.anterior:
            self.cursor = self.cursor.anterior

    def mostrar_texto(self):
        """Devuelve el texto completo como una cadena de caracteres."""
        texto = []
        actual = self.cabeza
        while actual:
            texto.append(actual.valor)
            actual = actual.siguiente
        return ''.join(texto)

class EditorDeTexto:
    def __init__(self):
        self.lista = ListaDoblementeEnlazada()

    def insertar(self, valor):
        """Inserta un carácter al final del texto."""
        self.lista.insertar_al_final(valor)

    def eliminar(self):
        """Elimina el carácter en la posición del cursor."""
        self.lista.eliminar()

    def mover_cursor_adelante(self):
        """Mueve el cursor una posición hacia adelante."""
        self.lista.mover_cursor_adelante()

    def mover_cursor_atras(self):
        """Mueve el cursor una posición hacia atrás."""
        self.lista.mover_cursor_atras()

    def mostrar_texto(self):
        """Devuelve el texto completo como una cadena de caracteres."""
        return self.lista.mostrar_texto()

    def ejecutar_comando(self, comando, argumento=None):
        """Ejecuta un comando del editor de texto."""
        if comando == 'i':
            if argumento:
                self.insertar(argumento)
            else:
                print("Por favor, proporcione un carácter para insertar.")
        elif comando == 'e':
            self.eliminar()
        elif comando == 'f':
            self.mover_cursor_adelante()
        elif comando == 'b':
            self.mover_cursor_atras()
        elif comando == 'm':
            print("Texto actual:", self.mostrar_texto())
        elif comando == 'q':
            print("Saliendo del editor de texto.")
            return False
        else:
            print("Comando no reconocido. Usa 'i' para insertar, 'e' para eliminar, 'f' para mover el cursor adelante, 'b' para mover el cursor atrás, 'm' para mostrar el texto, o 'q' para salir.")
        return True


if __name__ == "__main__":
    editor = EditorDeTexto()
    print("Bienvenido al Editor de Texto Simple.")
    print("Comandos disponibles:")
    print("'i <carácter>' - Insertar un carácter al final del texto.")
    print("'e' - Eliminar el carácter en la posición del cursor.")
    print("'f' - Mover el cursor una posición hacia adelante.")
    print("'b' - Mover el cursor una posición hacia atrás.")
    print("'m' - Mostrar el texto actual.")
    print("'q' - Salir del editor de texto.")

    while True:
        comando = input("Ingrese un comando: ").strip().split()
        if len(comando) == 1:
            seguir = editor.ejecutar_comando(comando[0])
        elif len(comando) == 2:
            seguir = editor.ejecutar_comando(comando[0], comando[1])
        else:
            print("Comando inválido. Intenta de nuevo.")
            seguir = True

        if not seguir:
            break
