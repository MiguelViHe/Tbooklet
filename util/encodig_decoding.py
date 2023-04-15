import bcrypt

def encriptar(pw):
    pw = pw.encode()
    sal = bcrypt.gensalt()
    return bcrypt.hashpw(pw, sal)

def desencriptar_y_comparar(pw, pwh): # Desencripa la contraseña del usuario y compara para devolver si es igual o no
    pw = pw.encode()
    if bcrypt.checkpw(pw, pwh):
        return True
    else:
        return False