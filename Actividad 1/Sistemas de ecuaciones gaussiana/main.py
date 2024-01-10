from sistema import Ecuacion
from operacion import gaussiana
from user import user

def main():
    user_n = user()
    ecuacion = Ecuacion(user_n)
    matriz, vector = ecuacion.generar_sistema()
    gaussiana(matriz, vector)

if __name__ == '__main__':
    main()
