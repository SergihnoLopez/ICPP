import json
import random

def cargar_resultados():
    try:
        with open('resultados_historicos.json', 'r') as archivo:
            print("Datos cargados desde el archivo JSON")
            return json.load(archivo)
    except:
        print("Datos cargados directamente")
        return {"sorteos": [
            {"numero": "5920"},
            {"numero": "0067"},
            {"numero": "7804"},
            {"numero": "9493"},
            {"numero": "1274"},
            {"numero": "3831"},
            {"numero": "1653"},
            {"numero": "6971"},
            {"numero": "9849"},
            {"numero": "9845"},
            {"numero": "2495"},
            {"numero": "8231"},
            {"numero": "1005"},
            {"numero": "7829"},
            {"numero": "4456"},
            {"numero": "8777"},
            {"numero": "9121"},
            {"numero": "3483"},
            {"numero": "5979"},
            {"numero": "1262"}
        ]}


# Función para analizar la frecuencia de los dígitos en cada posición
def obtener_frecuencia_digitos(resultados_historicos):
    frecuencia_posiciones = \
        [
            {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
            {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
            {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0},
            {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        ]

    for sorteo in resultados_historicos["sorteos"]:
        numero = sorteo['numero']
        for i, digito in enumerate(numero.zfill(4)):
            frecuencia_posiciones[i][digito] += 1  # Incrementa la frecuencia del dígito

    return frecuencia_posiciones


# Función para generar un número de la suerte basado en la frecuencia de los dígitos
def generar_numero_de_la_suerte(frecuencia_posiciones):
    numero_suerte = ""
    for posicion in frecuencia_posiciones:
        digitos_ordenados = []

        pares = list(posicion.items())
        for i in range(len(pares)):
            for j in range(i + 1, len(pares)):
                if pares[i][1] < pares[j][1]:
                    pares[i], pares[j] = pares[j], pares[i]

            digitos_ordenados = pares

        digito_mas_frecuente = digitos_ordenados[0][0]
        digito_segundo_mas_frecuente = digitos_ordenados[1][0]
        digito_predicho = random.choice([digito_mas_frecuente, digito_segundo_mas_frecuente])
        numero_suerte += digito_predicho

    return numero_suerte


# Función para guardar el número generado en un archivo JSON
def guardar_resultado_en_archivo(numero_suerte):
    try:
        with open("resultados_generados.json", "a") as archivo:
            json.dump({"numero": numero_suerte}, archivo)
            archivo.write("\n")
        print(f"El número {numero_suerte} ha sido guardado en resultados_generados.json")
    except Exception as e:
        print(f"Error al guardar el resultado: {e}")



def mostrar_menu():
    while True:
        print("********** Menú de Lotería ***********")
        print("*    1. Generar número de la suerte  *")
        print("*    2. Ver resultados históricos    *")
        print("*    3. Salir                        *")
        print("**************************************\n")
        try:
            opcion = int(input("Elige una opción: "))
            if opcion == 1:
                generar_numero()
            elif opcion == 2:
                mostrar_resultados_historicos()
            elif opcion == 3:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, ingresa un número válido.")


# Función para generar el número y mostrarlo
def generar_numero():
    resultados_historicos = cargar_resultados()
    frecuencia_digitos = obtener_frecuencia_digitos(resultados_historicos)

    numero_de_la_suerte = generar_numero_de_la_suerte(frecuencia_digitos)

    print(f'''
    ,---------------------------,
    |  /---------------------\\  |
    | |                       | |
    | |     Numero            | |
    | |      de la suerte     | |
    | |         {numero_de_la_suerte}          | |
    | |                       | |
    |  \\_____________________/  |
    |___________________________|
    ''')

    guardar_resultado_en_archivo(numero_de_la_suerte)


# Función para mostrar los resultados históricos
def mostrar_resultados_historicos():
    resultados_historicos = cargar_resultados()
    print("\n********** Resultados Históricos **********")
    for sorteo in resultados_historicos["sorteos"]:
        print(sorteo["numero"])


# Ejecutar el menú
if __name__ == "__main__":
    mostrar_menu()
