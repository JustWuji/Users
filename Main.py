import tkinter as tk
from Formularios import Formulario

#Creacion de la ventana
root = tk.Tk()
root.title("Gestion de Usuarios")
root.geometry("1280x720")

# Adjuntamos el formulario
formulario = Formulario(root)
formulario.pack()

# Ejecucion de la aplicacion
root.mainloop()