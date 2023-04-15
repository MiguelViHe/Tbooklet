import sqlite3

class TbookletRepository():

    def __init__(self):
        self.conexion = sqlite3.connect('BBDD/translation_booklet.db')

    def obtenerUsuarioPorNombre(self, nombre_usuario):
        cursor = self.conexion.cursor()
        cursor.execute('SELECT nombre_usu, pass_usu, puntuacion, guardado FROM Usuarios WHERE nombre_usu=?', (nombre_usuario,))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario

    def registrarUsuario(self, usuario, contraseña):
        cursor = self.conexion.cursor()
        cursor.execute('INSERT INTO Usuarios (nombre_usu, pass_usu) VALUES (?, ?)', (usuario, contraseña))
        self.conexion.commit()
        cursor.close()

    def guardar_partida(self, nom_usu, points, voypor):
        cursor = self.conexion.cursor()
        cursor.execute('UPDATE Usuarios SET puntuacion = ?, guardado = ? WHERE nombre_usu = ?', (points, voypor, nom_usu))
        self. conexion.commit()
        cursor.close()

    def partida_nueva(self):
        cursor = self.conexion.cursor()
        cursor.execute('SELECT tbooklet.id_frase, tbooklet.libro, tbooklet.lista, tbooklet.par, tbooklet.castellano, tbooklet.inglés, tbooklet.alt_ingles, dificultad.dificultad,'
                       ' dificultad.color_fondo, dificultad.color_texto FROM tbooklet INNER JOIN dificultad'
                       ' ON tbooklet.libro = dificultad.id')
        listafrases = cursor.fetchall()
        cursor.close()
        return listafrases

    def cargar_partida(self, id_frase):
        cursor = self.conexion.cursor()
        cursor.execute('SELECT tbooklet.id_frase, tbooklet.libro, tbooklet.lista, tbooklet.par,  tbooklet.castellano, tbooklet.inglés, tbooklet.alt_ingles, dificultad.dificultad,'
                       ' dificultad.color_fondo, dificultad.color_texto FROM tbooklet INNER JOIN dificultad'
                       ' ON tbooklet.libro = dificultad.id WHERE id_frase >= ? ORDER BY id_frase', (id_frase,))
        listafrases = cursor.fetchall()
        cursor.close()
        return listafrases

    def __del__(self):
        self.conexion.close()
