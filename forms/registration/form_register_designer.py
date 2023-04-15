import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl


class FormRegisterDesigner:

    def registrar(self):
        pass

    def __init__(self):
        self.ventana = tk.Toplevel()
        self.ventana.title('TBooklet - Registro de usuario')
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=False, height=False)
        utl.centrar_ventana(self.ventana, 600, 480)

        logo = utl.leer_imagen("./imagenes/guybrushentero.ico", (134, 267))

        # frame_logo
        frame_logo = tk.Frame(self.ventana, bd=0, width=200, relief=tk.SOLID, padx=10, pady=10, bg='aquamarine')
        frame_logo.pack(side="left", expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_logo, image=logo, bg='aquamarine', bd=0, relief=tk.SOLID)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # frame_form
        frame_form = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        # frame_from_top
        frame_from_top = tk.Frame(frame_form, height=50, bd=0, relief=tk.SOLID, bg='black')
        frame_from_top.pack(side="top", fill=tk.X)
        titulo = tk.Label(frame_from_top, text="Registro de usuario", font=('Times', 30), fg="#666a88", bg="#fcfcfc", pady=50)
        titulo.pack(expand=tk.YES, fill=tk.BOTH)

        # frame_from_fill
        frame_from_fill = tk.Frame(frame_form, height=50, bd=0, bg="#fcfcfc")
        frame_from_fill.pack(side="bottom", expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_from_fill, text="Usuario", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20, pady=5)
        self.campo_usuario = ttk.Entry(frame_from_fill, font=('Times', 14))
        self.campo_usuario.pack(fill=tk.X, padx=20, pady=10)

        etiqueta_password = tk.Label(frame_from_fill, text="Contraseña", font=('Times', 14), fg="#666a88", bg="#fcfcfc",anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20, pady=5)
        self.campo_contrasena = ttk.Entry(frame_from_fill, font=('Times', 14))
        self.campo_contrasena.pack(fill=tk.X, padx=20, pady=10)
        self.campo_contrasena.config(show="*")

        etiqueta_rep_password = tk.Label(frame_from_fill, text="Repite contraseña", font=('Times', 14), fg="#666a88", bg="#fcfcfc", anchor="w")
        etiqueta_rep_password.pack(fill=tk.X, padx=20, pady=5)
        self.campo_rep_contrasena = ttk.Entry(frame_from_fill, font=('Times', 14))
        self.campo_rep_contrasena.pack(fill=tk.X, padx=20, pady=10)
        self.campo_rep_contrasena.config(show="*")

        boton_registrar = tk.Button(frame_from_fill, text="Registrar", font=('Times', 15, BOLD), bg="aquamarine", bd=0, fg="black", command=self.registrar)
        boton_registrar.pack(fill=tk.X, padx=20, pady=20)
        boton_registrar.bind("<Return>", (lambda event: self.registrar()))  # Para que funcione pulsando el enter. hay que ponerse encima con el tabulador primero

        # End frame_form_fill

        self.ventana.mainloop()