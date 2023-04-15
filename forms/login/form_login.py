import tkinter
from tkinter import messagebox
import util.encodig_decoding as utl
from forms.master.form_master import MasterPanel
from forms.registration.form_registro import FormRegistro
from forms.login.form_login_designer import FormLoginDesigner
from persistence.repository.tbookletRepository import TbookletRepository

class FormLogin(FormLoginDesigner):

    def __init__(self):
        self.managebd = TbookletRepository()
        super().__init__()

    def verificar(self):
        usu = self.campo_usuario.get()
        password = self.campo_contrasena.get()
        usuario = self.managebd.obtenerUsuarioPorNombre(usu)
        print(usuario)
        if not usuario or not utl.desencriptar_y_comparar(password, usuario[1]):
            messagebox.showerror(message="El usuario o la contraseña son incorrectos. Vuelva a intentarlo o regístrese.", title="Mensaje")
            self.campo_usuario.delete(0, tkinter.END)
            self.campo_contrasena.delete(0, tkinter.END)
        else:
            self.ventana.destroy()
            MasterPanel(usuario)

    def userRegister(self):
        FormRegistro()

