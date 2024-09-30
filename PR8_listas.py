# Practica 8: Uso de listas en Python
print("Mejia Suarez Emmanuel Alexander:Ejemplo de uso de listas en Python")
# Imprimir una línea en blanco para mejorar la legibilidad
print(" ")

# Creamos una lista de animales
lista_animales = ["perro", "gato", "elefante"]
print("Lista de animales:", lista_animales)

# Usamos len() para obtener el número de elementos en la lista
print("Número de elementos en la lista de animales:", len(lista_animales))

# Espacio para mayor claridad
print(" ")

# Creamos varias listas con diferentes tipos de elementos relacionados con animales
lista_nombres = ["perro", "gato", "elefante"]
lista_edades = [5, 3, 10]
lista_tamaños = ["grande", "pequeño", "grande"]
lista_colores = ["marrón", "blanco", "gris"]

# Mostramos el contenido de cada lista
print("Lista de nombres de animales:", lista_nombres)
print("Lista de edades de animales:", lista_edades)
print("Lista de tamaños de animales:", lista_tamaños)
print("Lista de colores de animales:", lista_colores)

print(" ")

# Accedemos a un elemento específico de la lista de nombres
print("Segundo animal de la lista:", lista_nombres[1])

# Accedemos al último elemento de la lista
print("Último animal de la lista:", lista_nombres[-1])

# Accedemos a un rango de elementos de la lista
print("Animales del índice 0 al 2:", lista_nombres[0:3])

# Agregando un nuevo animal a la lista
lista_nombres.append("jirafa")
print("Lista de animales después de agregar una jirafa:", lista_nombres)

# Agregando un animal en la segunda posición
lista_nombres.insert(1, "tigre")
print("Lista de animales después de insertar un tigre:", lista_nombres)

# Quitando un animal de la lista
lista_nombres.remove("gato")
print("Lista de animales después de quitar el gato:", lista_nombres)

# Borrando el segundo animal
lista_nombres.pop(1)
print("Lista de animales después de borrar el segundo animal:", lista_nombres)

# Borrando el último animal
lista_nombres.pop()
print("Lista de animales después de borrar el último animal:", lista_nombres)

# Agregando elementos de una lista de animales salvajes
animales_salvajes = ["león", "tigre", "oso"]
lista_nombres.extend(animales_salvajes)
print("Lista de animales después de agregar animales salvajes:", lista_nombres)

# Agregando una tupla de animales domésticos
animales_domesticos = ("conejo", "hamster")
lista_nombres.extend(animales_domesticos)
print("Lista de animales después de agregar animales domésticos:", lista_nombres)
