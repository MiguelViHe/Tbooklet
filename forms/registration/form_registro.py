from tkinter import messagebox
import util.encodig_decoding as enc_dec
from forms.registration.form_register_designer import FormRegisterDesigner
from persistence.repository.tbookletRepository import TbookletRepository
import tkinter as tk

class FormRegistro(FormRegisterDesigner):

    def __init__(self):
        self.managedb = TbookletRepository()
        super().__init__()

    def passwordCoincide(self):
        status: bool = True
        if self.campo_contrasena.get() != self.campo_rep_contrasena.get():
            status = False
            messagebox.showerror(message="Las contraseñas no coinciden. Por favor vuelve a intentarlo.", title="Mensaje")
            self.campo_contrasena.delete(0, tk.END)
            self.campo_rep_contrasena.delete(0, tk.END)
        return status

    def existeUsuario(self, usuario):
        status: bool = False
        if usuario != None:
            status = True
            messagebox.showerror(message="El usuario ya existe. Prueba otro nombre", title="Mensaje")
        return status

    def registrar(self):
        if self.campo_usuario.get() != "":
            usuario = self.managedb.obtenerUsuarioPorNombre(self.campo_usuario.get())
            if not self.existeUsuario(usuario):
                if self.passwordCoincide():
                    self.managedb.registrarUsuario(self.campo_usuario.get(), enc_dec.encriptar(self.campo_contrasena.get()))
                    messagebox.showinfo(message="Usuario registrado correctamente.", title="Mensaje")
                    self.ventana.destroy()
        else:
            messagebox.showinfo(message="Debes introducir un nombre de usuario", title="¡Atención!")