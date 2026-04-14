# main.py

# Importamos las funciones que hemos creado en functions.py
from functions import read_data, split, reduce, silhouette


def main():
    """
    Función principal del programa.
    Va ejecutando por orden las funciones del examen
    y controla las excepciones.
    """

    # --------------------------------------------------
    # 1. Leer los datos del fichero CSV
    # --------------------------------------------------
    try:
        # Llamamos a read_data para leer el archivo
        datos = read_data("winequality.csv")

        print("read_data ejecutada correctamente")
        print("Número de muestras válidas:", len(datos))

    except Exception as e:
        # Si ocurre cualquier error, mostramos el tipo de excepción
        print(f"Ha ocurrido la excepción {type(e).__name__}")
        return

    # --------------------------------------------------
    # 2. Separar los vinos en white y red
    # --------------------------------------------------
    try:
        # Llamamos a split para dividir el diccionario
        white, red = split(datos)

        print("split ejecutada correctamente")
        print("Número de vinos white:", len(white))
        print("Número de vinos red:", len(red))

    except Exception as e:
        print(f"Ha ocurrido la excepción {type(e).__name__}")
        return

    # --------------------------------------------------
    # 3. Extraer un atributo en forma de lista
    #    Vamos a usar 'alcohol' como ejemplo
    # --------------------------------------------------
    try:
        # Obtenemos la lista de alcohol de los vinos blancos
        alcohol_white = reduce(white, "alcohol")

        # Obtenemos la lista de alcohol de los vinos tintos
        alcohol_red = reduce(red, "alcohol")

        print("reduce ejecutada correctamente")
        print("Primeros valores de alcohol en white:", alcohol_white[:5])
        print("Primeros valores de alcohol en red:", alcohol_red[:5])

    except Exception as e:
        print(f"Ha ocurrido la excepción {type(e).__name__}")
        return

    # --------------------------------------------------
    # 4. Calcular el coeficiente silhouette
    # --------------------------------------------------
    try:
        # Calculamos la silhouette de la lista white respecto a red
        resultado = silhouette(alcohol_white, alcohol_red)

        print("silhouette ejecutada correctamente")
        print("Coeficiente silhouette:", resultado)

    except Exception as e:
        print(f"Ha ocurrido la excepción {type(e).__name__}")
        return


# Esta línea hace que la función main() se ejecute
# solo si lanzamos este archivo directamente
if __name__ == "__main__":
    main()