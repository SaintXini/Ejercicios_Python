import tkinter as tk
from tkinter import ttk

ven = tk.Tk()
ven.geometry("600x400")
ven.title("Ingreso del sistema")
ven.configure(background="#1d2d44")

# Creamos un nuevo estilo
estilos = ttk.Style()
estilos.theme_use("clam")
estilos.configure(ven, background = "#1d2d44", foreground = "white", fieldbackground = "gray")

ven.columnconfigure(0, weight=1)
ven.rowconfigure(0, weight=1)

# agregamos un frame "un componente dentro de la ventana"
frame = ttk.Frame(ven)
# le damos las medidas a las columnas que queremos
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

# agregamos el titulo
etiqueta = ttk.Label(frame, text="Login", font=("Arial", 20))
# columnspan "nos ayuda a expandir una columna máss"
etiqueta.grid(row=0, column=0, columnspan=2)

# Agregar el usuairo
usuario_etiqueta = ttk.Label(frame, text="Usuario: ")
usuario_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=20)

usuario_caja =ttk.Entry(frame)
usuario_caja.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

# Agregamos la contradseña
password_etiqueta = ttk.Label(frame, text="Password")
password_etiqueta.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

password_caja_txt = ttk.Entry(frame, show="*")
password_caja_txt.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

# Agregamos el boton
login_boton = ttk.Button(frame, text="Enviar")
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

frame.grid(row=0, column=0)

ven.mainloop()

