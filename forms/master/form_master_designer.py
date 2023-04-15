import tkinter as tk
from tkinter.font import BOLD

import util.generic as utl



class FormMasterDesigner:

    def inicializar_juego(self, nueva_guardada):
        pass

    def comprobar(self, soluciones, respuesta):
        pass


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('TBooklet - El juego')
        w, h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        #self.ventana.geometry(f"{w}x{h}+0+0")
        self.ventana.geometry("%dx%d+0+0" % (w, h-50))
        #utl.centrar_ventana(self.ventana, w, h-50)
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=False, height=False)

        logo = utl.leer_imagen("./imagenes/guybrushentero.ico", (100, 200))

        # frame_from_top

        self.frame_from_top = tk.Frame(self.ventana, height=h/3, padx=10, pady=10, bg='#3a7ff6')
        self.frame_from_top.pack(side="top", expand=tk.YES, fill=tk.X)

        self.frame_top_left = tk.Frame(self.frame_from_top, height=h/3, padx=10, pady=10)
        self.frame_top_left.pack(side="left", expand=tk.YES, fill=tk.X)

        self.label_libro = tk.Label(self.frame_top_left, text="Libro ", font=('Times', 25), fg="#666a88", bg="#fcfcfc")
        self.label_libro.place(relx=0, rely=0, relwidth=0.5, relheight=0.33)
        self.label_lista = tk.Label(self.frame_top_left, text="Lista ", font=('Times', 25), fg="#666a88", bg="#fcfcfc")
        self.label_lista.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.33)
        self.label_dificultad = tk.Label(self.frame_top_left, text="Dificultad: ", font=('Times', 25), fg="#666a88", bg="#fcfcfc")
        self.label_dificultad.place(relx=0, rely=0.33, relwidth=1, relheight=0.33)
        self.label_par = tk.Label(self.frame_top_left, font=('Times', 25), fg="#666a88", bg="#fcfcfc")
        self.label_par.place(relx=0, rely=0.66, relwidth=1, relheight=0.33)

        self.frame_top_center = tk.Frame(self.frame_from_top, height=h/3)
        self.frame_top_center.pack(side="left", expand=tk.YES, fill=tk.X)

        self.label_logo = tk.Label(self.frame_top_center, image=logo, bg='#3a7ff6')
        self.label_logo.place(x=0, y=0, relwidth=1, relheight=1)

        self.frame_top_right = tk.Frame(self.frame_from_top, height=h/3,  padx=10, pady=10)
        self.frame_top_right.pack(side="right", expand=tk.YES, fill=tk.X)

        self.label_aciertos = tk.Label(self.frame_top_right, text="Aciertos: ", font=('Times', 25), fg="#666a88", bg="#CDF5E2")
        self.label_aciertos.place(relx=0, rely=0, relwidth=1, relheight=0.33)
        self.label_fallos = tk.Label(self.frame_top_right, text="Fallos: ", font=('Times', 25), fg="#666a88", bg="#F9B8B8")
        self.label_fallos.place(relx=0, rely=0.33, relwidth=1, relheight=0.33)
        self.label_media = tk.Label(self.frame_top_right, text="Media aciertos: ", font=('Times', 25), fg="#666a88", bg="#fcfcfc")
        self.label_media.place(relx=0, rely=0.66, relwidth=1, relheight=0.33)

        # frame_from_bottom

        self.frame_from_bottom = tk.Frame(self.ventana, height=int((h/3)*2), padx=20, pady=30, bg='#3a7ff6')
        self.frame_from_bottom.pack(expand=tk.YES, fill=tk.BOTH)

        self.label_panel_info = tk.Label(self.frame_from_bottom, text="Bienvenido a tu inglés más fluido con", font=('Times', 35), fg="#666a88", bg="#fcfcfc")
        self.label_panel_info.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        self.label_castellano = tk.Label(self.frame_from_bottom, text= "Translation Booklet", font=('Times', 35), fg="#666a88", bg="#fcfcfc")
        self.label_castellano.place(relx=0, rely=0.15, relwidth=1, relheight=0.25)
        self.label_correcto_incorrecto = tk.Label(self.frame_from_bottom, padx=20, pady=20, text="¿Selecciona con los botones qué deseas hacer?", font=('Times', 40), fg="#666a88", bg="#fcfcfc")
        self.label_correcto_incorrecto.place(relx=0, rely=0.45, relwidth=1, relheight=0.20)
        self.entry_respuesta = tk.Entry(self.frame_from_bottom, bg="white", fg="grey", borderwidth=3, font=("Times", 25, "bold"), justify=tk.CENTER)
        self.entry_respuesta.bind("<Return>", (lambda event: self.comprobar(self.label_castellano.cget("textvariable"), self.entry_respuesta.get())))

        self.boton_nueva_salir = tk.Button(self.frame_from_bottom, text="Nueva partida", font=('Times', 15), bg="#fcfcfc", bd=0, fg="#3a7ff6", command=lambda :self.inicializar_juego('nueva'))
        self.boton_nueva_salir.place(relx=0.635, rely=0.85, relwidth=0.25, relheight=0.1)
        #boton_registrar.bind("<Return>", (lambda event: self.userRegister()))  # Para que funcione pulsando el enter. hay que ponerse encima con el tabulador primero

        self.boton_cargar_guardar = tk.Button(self.frame_from_bottom, text="Cargar partida", font=('Times', 15), bg="#fcfcfc", bd=0, fg="#3a7ff6", command=lambda :self.inicializar_juego('cargar'))
        self.boton_cargar_guardar.place(relx=0.135, rely=0.85, relwidth=0.25, relheight=0.1)

        self.ventana.mainloop()




