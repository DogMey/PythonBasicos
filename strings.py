my_string = "Esto es una cadena de texto"
my_string_2 = 'Esto también es una cadena de texto'

print(len(my_string))  # Imprime la longitud de la cadena
print(my_string + " y " + my_string_2)  # Concatenación de cadenas

my_newline_string = "Primera línea\nSegunda línea"  # Cadena con salto de línea
print(my_newline_string)  # Imprime la cadena con salto de línea

my_tabulete_string = "Primera línea\tSegunda línea"  # Cadena con salto de línea
print(my_tabulete_string)  # Imprime la cadena con salto de línea

my_scape_string = "Esto es una comilla simple: \' y esto es una comilla doble: \""
print(my_scape_string)  # Imprime la cadena con comillas escapadas

# Formateo de cadenas
name = "Kevin"
age = 30
print(f"Hola, mi nombre es {name} y tengo {age} años.")  # Usando f-strings
print("Mi nombre es %s y tengo %d años." % (name, age))  # Usando el operador %
print("Mi nombre es %s y tengo %d años.".format(name, age))  # Usando el método format
print("Mi nombre es {} y tengo {} años.".format(name, age))  # Usando el método format

# Desempaquetado de cadenas
palabra = "Python"
a,b,c,d,e,f = palabra
print(a)  # Imprime 'P'
print(b)  # Imprime 'y'

# División de cadenas
lenguaje_slice = palabra[1:5]  # Slicing de la cadena
print(lenguaje_slice)  # Imprime 'ytho'

lenguaje_slice2 = palabra[1:]  # Slicing desde el índice 1 hasta el final
print(lenguaje_slice2)  # Imprime 'ython'

lenguaje_slice3 = palabra[:3]  # Slicing desde el inicio hasta el índice 3
print(lenguaje_slice3)  # Imprime 'Pyt'

# Reversión de cadenas
reversed_string = palabra[::-1]  # Reversión de la cadena
print(reversed_string)  # Imprime 'nohtyP'

# Funciones de cadenas
print(palabra.upper())  # Convierte la cadena a mayúsculas
print(palabra.lower())  # Convierte la cadena a minúsculas
print(palabra.capitalize) # Capitaliza la primera letra de la cadena
print(palabra.count('o'))  # Cuenta cuántas veces aparece 'o' en la cadena
print(palabra.find('t'))  # Encuentra el índice de la primera aparición de
print("123".isnumeric())  # Verifica si la cadena es numérica
print("abc".isalpha())  # Verifica si la cadena contiene solo letras
print("abc123".isalnum())  # Verifica si la cadena es alfanum
print("   Hola   ".strip())  # Elimina espacios al inicio y al final de la cadena
print("   Hola   ".lstrip())  # Elimina espacios al inicio de la cadena
print(palabra.startswith("Py"))  # Verifica si la cadena comienza con "Py"
