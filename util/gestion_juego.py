def comparar_respuesta(opc_ingles, dada):
    print(f"ingles: {opc_ingles}")
    posibilidades = str(opc_ingles).split("/")
    if posibilidades[1] == "None":
        return str(dada).strip().lower() == posibilidades[0].strip().lower()
    else:
        if str(dada).strip().lower() == posibilidades[0].strip().lower():
            return posibilidades[1]
        elif str(dada).strip().lower() == posibilidades[1].strip().lower():
            return posibilidades[0]
        else:
            return None


def calcular_media(self):
    return (self.aciertos * 100) / (self.aciertos + self.fallos)


def inicializar_frame_from_top(self):
    self.label_libro.config(text=f"Libro {self.lista_frases[self.pregunta_actual][1]}")
    self.label_lista.config(text=f"Lista {self.lista_frases[self.pregunta_actual][2]}")
    self.label_dificultad.config(text=f"Dificultad: {self.lista_frases[self.pregunta_actual][7]}",
                                 bg=self.lista_frases[self.pregunta_actual][8],
                                 fg=self.lista_frases[self.pregunta_actual][9])
    self.label_par.config(text=f"{self.lista_frases[self.pregunta_actual][3]} de 25")

def configurar_color_dificultad(self):
    self.frame_from_top.config(bg=self.lista_frases[self.pregunta_actual][8])
    self.label_logo.config(bg=self.lista_frases[self.pregunta_actual][8])
    self.frame_from_bottom.config(bg=self.lista_frases[self.pregunta_actual][8])