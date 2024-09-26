# Ejemplo de uso de listas en Python
print(" ")

# Creamos una lista de animales
animales = ["perro", "gato", "elefante"]
print(animales)

# Usamos len() para obtener el número de elementos en la lista
print("Número de elementos en la lista de animales:", len(animales))

# Espacio para mayor claridad
print(" ")

# Creamos varias listas con diferentes tipos de elementos
lista_animales = ["perro", "gato", "elefante"]
lista_edades = [2, 5, 10, 3]
lista_respuestas = [True, False, True]
lista_variedad = ["rojo", 42, False, 3.14, "femenino"]

# Mostramos el contenido de cada lista
print("Lista de animales:", lista_animales)
print("Lista de edades:", lista_edades)
print("Lista de respuestas:", lista_respuestas)
print("Lista variada:", lista_variedad)

print(" ")

# Accedemos a un elemento específico de la lista de animales
# Recordemos que la indexación comienza en 0
print("Segundo elemento de la lista de animales:", lista_animales[1])

# Accedemos al último elemento de la lista
print("Último elemento de la lista de animales:", lista_animales[-1])

# Accedemos a un rango de elementos de la lista
# El rango 1:4 incluye los elementos en las posiciones 1, 2 y 3
lista_animales_completa = ["perro", "gato", "elefante", "jirafa", "león", "tigre", "osos"]
print("Elemento en la posición -5:", lista_animales_completa[-5])

# Espacio final para separar la salida
print(" ")
