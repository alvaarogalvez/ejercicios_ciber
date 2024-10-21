import sys

# Comprobamos si se proporcionaron suficientes argumentos
if len(sys.argv) != 4:
    print("Uso: python ejercicio3.py <ancho> <alto> <tipo_de_linea>")
    sys.exit(1)

# Convertir los argumentos a enteros
try:
    width = int(sys.argv[1])
    height = int(sys.argv[2])
except ValueError:
    print("Por favor, asegúrate de que el ancho y la altura son números enteros.")
    sys.exit(1)

# Obtener el tipo de línea
line_type = sys.argv[3]

# Definir caracteres para las cajas simples y dobles
if line_type == "simple":
    chars = "┌┐└┘│─"
elif line_type == "doble":
    chars = "╔╗╚╝║═"
elif len(line_type) == 1:  # Si es un solo carácter
    char = line_type
    chars = char + char + char + char + char + char  # Usar el mismo carácter para todos
else:
    print("El tipo de línea debe ser 'simple', 'doble' o un solo carácter.")
    sys.exit(1)

def createTop(length):
    return chars[0] + chars[5] * (length - 2) + chars[1]

def createBottom(length):
    return chars[2] + chars[5] * (length - 2) + chars[3]

def createMiddle(length):
    return chars[4] + " " * (length - 2) + chars[4]

def createBox(width, height):
    return createTop(width) + "\n" + (createMiddle(width) + "\n") * (height - 2) + createBottom(width)

# Imprimir la caja
print(createBox(width, height))
