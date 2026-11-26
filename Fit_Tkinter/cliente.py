class Cliente:
    # Creación de la clase identidad para cliente DAO
    # None se utiliza para solo agregar los atributos que deseamos utilizar y al momento de solicitarlos no tengamos que ingresar todos
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia

    def __str__(self):
        return (f"Id: {self.id}, Nombre: {self.nombre}, "
                f"Apellido: {self.apellido}, Membresia: {self.membresia} ")


## Que no se te olvida
# un patrón de diseño son soluciones ya conocidas que nos encontramos al crear apps
# Son planos que podemos utilizar

# Patrón Dao, data acces object
# se utiliza para acceder a una identidad de nuestra app, en este caso el cliente
# se encargara de administrar la info de la identidad de cliente o la clase cliente
