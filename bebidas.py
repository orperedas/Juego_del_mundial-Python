"""
Máquina expendedora de refrescos

Se solicita al usuario Ingrear un monto de billete para realizar la compra. Si el monto es mayor al valor ingresado le devolverá el resto como cambio.

Se solicita al usuario indicar cuál de las marcas de refresco desea comprar.

"""
def ingresar_marca():
	return int(input("Ingresa el número de la marca de refresco que deseas: "))


def refresco():
	print("\n¡Hola, bienbenido a tu expendedora de refrescos favorito!")
	
	billete = int(input("Ingrese un billete de denominación no menor a $100: "))
	valor_refresco = 100

# Este es el while que evalúa que cuando el valor introducido en la variable billete sea menor a valor_refresco solicite ingresar un nuevo valor.
	while billete < valor_refresco:
		print("El valor introducido es incorrecto. Por favor ingresa un nuevo billete.")
		billete = int(input("\nIngrese un billete de denominación no menor a $100: "))

	if billete == valor_refresco:
		print("\nValor exacto")
		marca_refresco()
	else:
		cambio = billete - valor_refresco
		print("\nTu cambio es de: $", cambio)
		marca_refresco()

def marca_refresco():
	marca = ("Coca Cola", "Pepsi Cola", "7UP", "Manaos manzana", "Fanta")
	marca_len = len(marca)
	marca_indice = marca.index(marca[0])

	print("\nElige el refresco: ")

# Modo anterior de imprimir la lista de refrescos. Es una construcción manual por lo que si la tupla tuviese más elementos o se cambian las marcas habría que escribir manualmente esos cambios.
	"""
	print("\nElige el refresco:",
		"\n  1. ", marca[0], 
		"\n  2. ", marca[1], 
		"\n  3. ", marca[2],
		"\n  4. ", marca[3],
		"\n  5. ", marca[4])
	"""

# Modo dinámico de impresión de la lista de refrescos, si la tupla de la marca se definiera con más marcas de refrescos se imprimirían todas.
	for marca_indice in range(marca_len):
		print(marca_indice+1, "-", marca[marca_indice])
		marca_indice+1

	marca_elegida = ingresar_marca()

# Bucle while con el que se comprueba que el número de opción ingresado sea válido, de lo contrario solicita volverlo a ingresar
	while marca_len < marca_elegida:
		print("Has ingresado un número no válido", marca_elegida, ", por favor ingresa uno de los valores de la lista.")
		marca_elegida = ingresar_marca()

	marca_elegida = marca_elegida -1
	print("\nDisfruta de una refrescante ", marca[marca_elegida], "\n*** ¡Gracias por tu compra! ***\n")

refresco()