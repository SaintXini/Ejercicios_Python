import tkinter as tk
from cliente import Cliente

from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter.messagebox import showerror

from cliente_dao import ClienteDAO

class App(tk.Tk):
    COLOR_VENTANA = "#1d2d44"

    def __init__(self):
        super().__init__()
        self.id_cliente = None
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_titulo()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botons()

    def configurar_ventana(self):
        # Tamaño y titulo
        self.geometry("900x600")
        self.title("Zona Fit APP")
        #  fijarse siempre en la escritura que ahora no me sale el autocomepletado de palabras
        self.configure(background=App.COLOR_VENTANA)

        # Aplicamos el estilo
        self.estilos = ttk.Style()
        self.estilos.theme_use("clam")
        self.estilos.configure(self, background = App.COLOR_VENTANA, foreground = "white")

    def configurar_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def mostrar_titulo(self):
       etiqueta = ttk.Label(self, text = "Zona Fit(GYM)", font=("Arial", 30), background=App.COLOR_VENTANA, foreground="white") 
       etiqueta.grid(row=0, column=0, columnspan=2, pady=30)

    def mostrar_formulario(self):
        self.frame_f = ttk.Frame()
        # NOmbre
        nombre_label = ttk.Label(self.frame_f, text="Nombre: ")
        nombre_label.grid(row=0, column=0, sticky=tk.W, pady=30, padx=5)
        self.nombre_t = ttk.Entry(self.frame_f, foreground="black")
        self.nombre_t.grid(row=0, column=1)

        # Apellido
        apellido_label = ttk.Label(self.frame_f, text="Apellido: ")
        apellido_label.grid(row=1, column=0, sticky=tk.W, pady=30, padx=5)
        self.apellido_t = ttk.Entry(self.frame_f, foreground="black")
        self.apellido_t.grid(row=1, column=1)

        # Membresia
        membresia_label = ttk.Label(self.frame_f, text="Membresia: ")
        membresia_label.grid(row=2, column=0, sticky=tk.W, pady=30, padx=5)
        self.membresia_t = ttk.Entry(self.frame_f, foreground="black")
        self.membresia_t.grid(row=2, column=1)     

        # Publicamos el frame
        self.frame_f.grid(row=1, column=0)

    def cargar_tabla(self):
        # creamos un frame para poder mostrar la tabla que ira del lado izq
        self.frame_tabla = ttk.Frame(self)
        # Definimos los estilos de la tabla
        self.estilos.configure("Treeview", background="gray", foreground="black", fieldbackground="gray", rowheight=30)
        columnas = ("Id", "Nombre", "Apellido", "Membresia")
        # esto hace que los cambios que se realizen solo afecte a la tabla y no a todo lo demas que se encuentra en dicha area
        self.tabla = ttk.Treeview(self.frame_tabla, columns=columnas, show="headings")

        # agregamos los acabeceros ot itulos
        # y aca definimos donde se mostrara y en que posición se encontrara de la columna
        self.tabla.heading("Id", text="ID", anchor=tk.CENTER)
        self.tabla.heading("Nombre", text="NOMBRE", anchor=tk.W)
        self.tabla.heading("Apellido", text="APELLIDO", anchor=tk.W)
        self.tabla.heading("Membresia", text="MEMBRESIA", anchor=tk.W)

        # definimos las columnas
        self.tabla.column("Id", anchor=tk.CENTER, width=80)
        self.tabla.column("Nombre", anchor=tk.W, width=120)
        self.tabla.column("Apellido", anchor=tk.W, width=120)
        self.tabla.column("Membresia", anchor=tk.W, width=120)

        # Cargar los datos de los clientes de la BD
        clientes = ClienteDAO.seleccionar()
        # en la variable c tenemos el objeto cliente que esta recorriendo, pór cada uno de los datos que tenemos
        for c in clientes:
            self.tabla.insert(parent="",
                              index=tk.END,
                              values=(c.id, c.nombre, c.apellido, c.membresia))


        # agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # mostrar la tabla
        self.tabla.grid(row=0, column=0)

        # Esto funcionara al momento de seleccionar algun cliente nos lo mostrara del lado del formulario
        self.tabla.bind('<<TreeviewSelect>>', self.cargar_cliente)


        # mostramos el frame
        self.frame_tabla.grid(row=1, column=1, padx=30)

    def mostrar_botons(self):
        self.frame_b = ttk.Frame()
        # Creamos los botonoes
        # Agregar
        agregar_b = ttk.Button(self.frame_b, text="Guardar", command=self.validar_cliente)
        agregar_b.grid(row=0, column=0, padx=30)
        
        # Eliminar
        eliminar_b = ttk.Button(self.frame_b, text="Eliminar", command=self.eliminar_cliente)
        eliminar_b.grid(row=0, column=1, padx=30)
        
        # limpiar la información
        limpiar_b = ttk.Button(self.frame_b, text="Limpiar", command=self.limpiar_datos)
        limpiar_b.grid(row=0, column=2, padx=30)
        
        # aplicamos un estilo al estar pocisionados sobre el boton
        # ojo tengo que utilizar comilla simple áca, debido a que no se si ingrese mal algo o es por las comillas, pero no me aparecía hasta que cambie
        self.estilos.configure('TButton', background='#005f73')
        self.estilos.map('TButton', background=[('active', '#0a9396')])

        # que se pueda ver
        self.frame_b.grid(row=2, column=0, columnspan=2, pady=40)

    def validar_cliente(self):
        # VAldidamos que los campos tenga inforamción
        if (self.nombre_t.get() and self.apellido_t.get() and self.membresia_t.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title="Atencion", message="el valor de membresia no es numerico")
                # aca le pedimos que nos borre desde el inicio de la cadena hasta el final
                self.membresia_t.delete(0, tk.END)
                # que el cursor pueda hacer la modificación
                self.membresia_t.focus_set()
            # si el usuario no proporciono información para los campos
        else:
            showerror(title="Atención", message="Debe completar el formulario")
            self.nombre_t.focus_set()

    # si el valor es verdadero se guarda el cliente
    def validar_membresia(self):
        try:
            int(self.membresia_t.get())
            return True
        except:
            return False

    def guardar_cliente(self):
        # Recuperar los valores de los txt
        nombre = self.nombre_t.get()
        apellido = self.apellido_t.get()
        membresia = self.membresia_t.get()

        # Validamos el valor de id_cliente
        if self.id_cliente is None: # si no esta registrado o es un nuevo registro
            # aca importamos la clase Cliente, y posteriormente a ello los insertamos a la base de datos y mostramos el mensaje
            cliente = Cliente(nombre = nombre, apellido = apellido, membresia = membresia)
            ClienteDAO.insertar(cliente)
            showinfo(title="Agregado correctamente", message="Cliente agregado correctamente.....:D")
        else: # actualizar los cuadros de texto, si reconoce que ya posee un id
            cliente = Cliente(self.id_cliente, nombre, apellido, membresia)
            ClienteDAO.actualizar(cliente)
            showinfo(title='Actualizar', message="La información del cliente a sido actualizada... :D")

        # Volvemos a mostrar los datos de la tabla de la derecha 
        self.recargar_datos()

    # se define tambien con event, debido a que el parametro es llamado a traves de un eventos
    def cargar_cliente(self, event):
        # esto hara que nos muestre solo el elemento seleccionado por ende se marca con 0, porque puede llegar a mostrar todos los elelmentos aunque hayamos seleccionado uno
        elemento_seleccionado = self.tabla.selection()[0]
        # con esto nos meustra el elemento seleccionado de la tabla
        elemento = self.tabla.item(elemento_seleccionado)
        cliente_t = elemento['values'] # tupla con valores
        # recuperamos los valores del cliente
        self.id_cliente = cliente_t[0]
        nombre = cliente_t[1]
        apellido = cliente_t[2]
        membresia = cliente_t[3]

        # antes de cargar limpiamos el formulario
        self.limpiar_formulario()
        # Cargamos los valores en el formulario
        self.nombre_t.insert(0, nombre)
        self.apellido_t.insert(0, apellido)
        self.membresia_t.insert(0, membresia)

    # esta funcion ayudara a recargar la tabla del lado derecho y limpiar lo que ya habiamos agregado
    def recargar_datos(self):
        # volvemos a cargar la tabla
        self.cargar_tabla()
        # Limpiamos los datos de los text
        self.limpiar_datos()

    def limpiar_datos(self):
        self.limpiar_formulario()
        self.id_cliente = None

    def limpiar_formulario(self):
        # esto limpiara desde el inicio hasta el final de cualquier cadena que sea escrita se eliminara
        self.nombre_t.delete(0, tk.END)
        self.apellido_t.delete(0, tk.END)
        self.membresia_t.delete(0, tk.END)

    def eliminar_cliente(self):
        pass

# para inicializar la pantalla

if __name__ == "__main__":
    app = App()
    app.mainloop()