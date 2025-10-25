def verify_password(password):
   
    if not password:
        return False, "La contraseña no puede estar vacía."

    if not 8 <= len(password) <= 20:
        return False, "La contraseña debe tener entre 8 y 20 caracteres."

    return True, "La contraseña es válida."

if __name__ == '__main__':
    print("Verificando 'password123':", verify_password("password123"))
    print("Verificando 'corto':", verify_password("corto"))
    print("Verificando '':", verify_password(""))