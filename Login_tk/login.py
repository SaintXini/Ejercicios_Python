import tkinter as tk
from tkinter import ttk

ven = tk.Tk()
ven.geometry("600x400")
ven.title("Ingreso del sistema")
ven.configure(background="#1d2d44")

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

frame.grid(row=0, column=0)

ven.mainloop()

