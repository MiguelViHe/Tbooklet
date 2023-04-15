from forms.master.form_master_designer import FormMasterDesigner
import tkinter as tk
from tkinter import messagebox
import util.gestion_juego as gestJu
from persistence.repository.tbookletRepository import TbookletRepository


class MasterPanel(FormMasterDesigner):
    def __init__(self, usuario_logueado):
        self.usuario = usuario_logueado
        self.managedb = TbookletRepository()
        self.aciertos = None
        self.fallos = None
        self.pregunta_actual = None
        self.lista_frases = None
        self.guardado_reciente = False
        super().__init__()


    def guardar_partida(self):
        self.managedb.guardar_partida(self.usuario[0], self.aciertos, self.lista_frases[self.pregunta_actual][0])
        self.guardado_reciente = True
        messagebox.showinfo(title="Mensaje", message="Partida guardada correctamente")


    def salir_juego(self):
        if not self.guardado_reciente:
            saliendo = messagebox.askquestion(title="¡Atención!", message="No has guardado la partida, ¿Deseas guardar antes de salir?")
            if saliendo == "yes":
                self.guardar_partida()
        self.ventana.destroy()


    def comprobar(self, soluciones, respuesta):
        correcto = gestJu.comparar_respuesta(soluciones, respuesta)
        if correcto:
            print(correcto)
            self.aciertos += 1
            self.label_aciertos.config(text=f"Aciertos: {self.aciertos}")
            if correcto != True:
                self.label_correcto_incorrecto.config(text=f"¡Correcto! También valdría '{correcto}'", fg="green")
            else:
                self.label_correcto_incorrecto.config(text="¡Correcto, sigue así!", fg="green")
        else:
            print(correcto)
            self.fallos += 1
            self.label_fallos.config(text=f"Fallos: {self.fallos}")
            if correcto != False:
                self.label_correcto_incorrecto.config(text=f"¡Incorrecto! Lo correcto sería : '{self.lista_frases[self.pregunta_actual][5]}' o '{self.lista_frases[self.pregunta_actual][6]}'", fg="red")
            else:
                self.label_correcto_incorrecto.config(text=f"¡Incorrecto! Lo correcto sería : '{self.lista_frases[self.pregunta_actual][5]}'", fg="red")
        self.label_media.config(text=f"Media aciertos: {round(gestJu.calcular_media(self), 2)}%")
        self.pregunta_actual += 1
        self.ventana.update()
        self.ventana.after(3000)
        if self.pregunta_actual == len(self.lista_frases):
            self.label_correcto_incorrecto.config(text=f'Fin del juego. Puntos: {self.aciertos} de {self.aciertos + self.fallos}')
            self.label_castellano.config(text="¡Enhorabuena! Has terminado todas las preguntas", textvariable="")
            self.label_panel_info.place_forget()
            self.entry_respuesta.place_forget()
            self.boton_cargar_guardar.config(text='Volver a jugar', command=lambda :self.inicializar_juego("volver"))
        else:
            self.label_correcto_incorrecto.config(text="")
            self.entry_respuesta.delete(0, tk.END)
            self.label_castellano.config(text=self.lista_frases[self.pregunta_actual][4], textvariable=f"{self.lista_frases[self.pregunta_actual][5]}/{self.lista_frases[self.pregunta_actual][6]}")
            gestJu.inicializar_frame_from_top(self)
            if self.lista_frases[self.pregunta_actual][1] != self.lista_frases[self.pregunta_actual - 1][1]:
                gestJu.configurar_color_dificultad(self)


    def inicializar_juego(self, eleccion):
        if eleccion in ["nueva", "volver"]:
            self.aciertos = 0
            self.fallos = 0
            self.pregunta_actual = 0
            self.lista_frases = self.managedb.partida_nueva()
            self.label_panel_info.config(text="Comencemos por el principio...")
            if eleccion == "volver":
                self.label_media.config(text="Media aciertos: ")
                self.label_panel_info.place(relx=0, rely=0, relwidth=1, relheight=0.1)
                self.entry_respuesta.place(relx=0, rely=0.70, relwidth=1, relheight=0.1)
                self.entry_respuesta.delete(0, tk.END)
        else:
            self.aciertos = self.usuario[2]
            self.fallos = (self.usuario[3]-1) - self.usuario[2]
            self.pregunta_actual = 0
            self.lista_frases = self.managedb.cargar_partida(self.usuario[3])
            self.label_media.config(text=f"Media aciertos: {round(gestJu.calcular_media(self), 2)}%")
            self.label_panel_info.config(text="Continuemos por donde lo habías dejado...")
        print(self.lista_frases)
        print(len(self.lista_frases))
        gestJu.inicializar_frame_from_top(self)
        gestJu.configurar_color_dificultad(self)
        self.label_castellano.config(text=self.lista_frases[self.pregunta_actual][4], textvariable=f"{self.lista_frases[self.pregunta_actual][5]}/{self.lista_frases[self.pregunta_actual][6]}")
        self.label_aciertos.config(text=f"Aciertos: {self.aciertos}")
        self.label_fallos.config(text=f"Fallos: {self.fallos}")
        self.label_correcto_incorrecto.config(text="")
        self.entry_respuesta.place(relx=0, rely=0.70, relwidth=1, relheight=0.1)
        self.boton_cargar_guardar.config(text='Guardar partida', command=self.guardar_partida)
        self.boton_nueva_salir.config(text='Salir', command=self.salir_juego)
