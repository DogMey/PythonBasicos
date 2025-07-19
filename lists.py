my_list = list()
my_other_list = []

print(len(my_list))  # Imprime la longitud de la lista

my_list = [22, 33, 44, 35, 26]  # Lista de edades

my_other_list = [22, 1.62, "Kevin", "DogMey"]  # Lista con diferentes tipos de datos

print(my_other_list[0])  # Imprime el primer elemento de la lista
print(my_other_list[-1]) # Imprime el último elemento de la lista

print(my_other_list.count(22))  # Cuenta cuántas veces aparece el número 22 en la lista
print(my_other_list.index("Kevin"))  # Encuentra el índice del elemento "Kevin"

age, height, name, nickname = my_other_list  # Desempaquetado de la lista
print(name)  # Imprime "Kevin"

new_list = my_list + my_other_list  # Concatenación de listas
print(new_list)  # Imprime la lista concatenada

my_other_list.append(12000000)  # Agrega salario al final de la lista
my_other_list.insert(1, "Programador")  # Inserta "Programador" en la posición 1
my_other_list.remove("DogMey")  # Elimina "DogMey" de la lista
my_other_list.pop(2)  # Elimina el elemento en la posición 2
del my_other_list[2]  # Elimina el elemento en la posición 2
my_list.clear()  # Limpia la lista, dejándola vacía


print(my_other_list)  # Imprime la lista actualizada