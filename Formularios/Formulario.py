import tkinter as tk
from Clases.usuarios import Usuarios

class FormularioUsuarios(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.usuarios_obj = Usuarios()
        self.pack()
        self.crear_widgets()

    def crear_widgets(self):
        tk.Label(self, text="Nombre").pack()
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack()

        tk.Label(self, text = "Nickname").pack()
        self.entry_nickname = tk.Entry(self)
        self.entry_nickname.pack()

        tk.Label(self, text = "Clave").pack()
        self.entry_clave = tk.Entry(self, show="*")
        self.entry_clave.pack()

        # Botones
        self.btn_guardar = tk.Button(self, text="Guardar Usuario", command=self.guardar)
        self.btn_guardar.pack()

        self.btn_listar = tk.Button(self, text="Listar Usuarios", command=self.listar)
        self.btn_listar.pack()

        # Panel de los usuarios
        self.panel_usuarios = tk.Text(self, height=10, width=50, state=tk.DISABLED)
        self.panel_usuarios.pack()

    def guardar(self):
        nombre = self.entry_nombre.get()
        nickname = self.entry_nickname.get()
        clave = self.entry_clave.get()
        self.usuarios_obj.guardarUsuario(nombre, nickname, clave)
        self.entry_nombre.delete(0, tk.END)
        self.entry_nickname.delete(0, tk.END)
        self.entry_clave.delete(0, tk.END)

    def listar(self):
        self.panel_usuarios.config(state=tk.NORMAL)
        self.panel_usuarios.delete(1.0, tk.END)
        usuarios = self.usuarios_obj.listarUsuarios()
        for usuario in usuarios:
            self.panel_usuarios.insert(tk.END, f"Nombre: {usuario['nombre']}, Nickname: {usuario['nickname']}, Clave: {usuario['clave']}\n")
