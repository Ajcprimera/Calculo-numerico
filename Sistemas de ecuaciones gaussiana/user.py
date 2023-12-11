def user():
    while True:    
        try:
            user = int(input('Ingrese el numero de columnas y filas: '))
            if isinstance(user, int):
                return user
        except ValueError as error:
            print(error)