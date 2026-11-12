# aca utilizare una lista para almacenar los snacks disponibles en la maquina,en un diccionario se almacenara el nombre del snack y su precio, y en la lista se almacenara el diccionario de cada snack
snacks = [{"id": 1, "nombre": "Chocolatina", "precio": 1.5}, 
          {"id": 2, "nombre": "Galletas", "precio": 2.0}, 
          {"id": 3, "nombre": "Papas fritas", "precio": 1.0}, 
          {"id": 4, "nombre": "Refresco", "precio": 1.5}]

# Lista de productos, utilizando una lista vacia
productos = []

print("Bienvenido a la máquina de snacks")
print("Estos son los snacks disponibles:")
for snack in snacks:
    # aca se mostrara el id, nombre y precio de cada snack
    print(f"- {snack['id']}: {snack['nombre']}: Q {snack['precio']:.2f}")