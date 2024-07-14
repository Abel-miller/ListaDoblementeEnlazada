﻿# Editor de Texto Simple

Una aplicación de edición de texto basada en una lista doblemente enlazada que permite realizar operaciones básicas de edición a través de una interfaz de línea de comandos.

## 1. Estructura General de la Aplicación

La aplicación está compuesta por dos partes principales:

- **`ListaDoblementeEnlazada`**: Maneja la estructura de datos que almacena el texto.
- **`EditorDeTexto`**: Proporciona la interfaz para interactuar con el texto y realizar operaciones de edición.

## 2. Clases y Componentes Principales

### a. Clase `Nodo`

**Propósito**: Representar un carácter en el texto, con referencias al siguiente y al anterior nodo en la lista.

```python
class Nodo:
    def __init__(self, valor=None):
        self.valor = valor  # Valor del nodo, que representa un carácter del texto.
        self.siguiente = None  # Apunta al siguiente nodo en la lista.
        self.anterior = None  # Apunta al nodo anterior en la lista.
Características Importantes:


valor: Almacena el carácter del texto.
siguiente: Referencia al próximo nodo en la lista.
anterior: Referencia al nodo previo en la lista.
b. Clase ListaDoblementeEnlazada
Propósito: Implementar una lista doblemente enlazada que almacene y gestione el texto.

python
Copiar código
class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None  # Nodo al principio de la lista.
        self.cola = None  # Nodo al final de la lista.
        self.cursor = None  # Nodo donde está el cursor actualmente.
```
## Métodos Importantes:

insertar_al_inicio(valor): Inserta un nuevo carácter al inicio de la lista.
insertar_al_final(valor): Inserta un nuevo carácter al final de la lista.
eliminar(): Elimina el carácter en la posición del cursor.
mover_cursor_adelante(): Mueve el cursor una posición hacia adelante en la lista.
mover_cursor_atras(): Mueve el cursor una posición hacia atrás en la lista.
mostrar_texto(): Devuelve el texto completo como una cadena de caracteres.
c. Clase EditorDeTexto
Propósito: Ofrecer una interfaz de usuario para interactuar con el texto utilizando comandos.

python
Copiar código
class EditorDeTexto:
    def __init__(self):
        self.lista = ListaDoblementeEnlazada()
Métodos Importantes:
```
insertar(valor): Llama a insertar_al_final() para agregar un carácter al final del texto.
eliminar(): Llama a eliminar() para borrar el carácter en la posición del cursor.
mover_cursor_adelante(): Llama a mover_cursor_adelante() para mover el cursor una posición hacia adelante.
mover_cursor_atras(): Llama a mover_cursor_atras() para mover el cursor una posición hacia atrás.
mostrar_texto(): Llama a mostrar_texto() para mostrar el contenido del texto.
ejecutar_comando(comando, argumento=None): Interpreta los comandos del usuario y llama al método correspondiente.
3. Interfaz de Línea de Comandos
La interfaz de línea de comandos permite al usuario ejecutar diferentes comandos para interactuar con el editor de texto. Los comandos disponibles son:
```
i <carácter>: Inserta un carácter al final del texto.
e: Elimina el carácter en la posición del cursor.
f: Mueve el cursor una posición hacia adelante.
b: Mueve el cursor una posición hacia atrás.
m: Muestra el texto actual.
q: Sale del editor de texto.
Código de Ejemplo:
```
python
Copiar código
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
```
## 4. Ejemplos de Uso y Resultados
```Ejemplo 1: Insertar y Mostrar Texto
plaintext
Copiar código
Ingrese un comando: i H
Ingrese un comando: i o
Ingrese un comando: i l
Ingrese un comando: i a
Ingrese un comando: m
Texto actual: Hola
Acción: Inserta 'H', 'o', 'l', 'a' en secuencia y muestra el texto.

Ejemplo 2: Mover Cursor y Eliminar Carácter
plaintext
Copiar código
Ingrese un comando: b
Ingrese un comando: e
Ingrese un comando: m
Texto actual: Hol
Acción: Mueve el cursor hacia atrás y elimina el carácter 'a', mostrando el texto resultante.
```
## 5. Posibles Mejoras y Aplicaciones Adicionales
Aquí tienes algunas ideas para expandir la funcionalidad del editor de texto:
```
Deshacer/Rehacer: Implementar una funcionalidad de deshacer y rehacer cambios utilizando una estructura de datos adicional como una pila.
Buscar y Reemplazar: Agregar funciones para buscar un texto específico y reemplazarlo por otro.
Guardar y Cargar Archivos: Implementar funcionalidades para guardar el texto a un archivo y cargar el texto desde un archivo.
Interfaz Gráfica: Desarrollar una interfaz gráfica de usuario (GUI) usando una biblioteca como tkinter para una experiencia más amigable.
