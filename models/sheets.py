import os
import random
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from dotenv import load_dotenv

load_dotenv()

scope = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


# Obtener la ruta del directorio principal del proyecto
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Construir la ruta completa al archivo JSON de credenciales en el directorio principal
credentials_path = os.path.join(project_dir, "gs_credentials.json")

credenciales = ServiceAccountCredentials.from_json_keyfile_name(
    credentials_path, scope
)

cliente = gspread.authorize(credenciales)
sheets_key = str(os.getenv("KEY_SHEETS"))


def ConectarGoogleSheets():
    libro_lectura = cliente.open_by_key(sheets_key)
    # Informacion Formato
    hoja_lectura = libro_lectura.worksheet("DATA")
    datos = hoja_lectura.get_all_values()[1:]
    return datos


def convertir_archivo_pandas():
    archivo = ConectarGoogleSheets()
    data = pd.DataFrame(archivo)
    data.rename(
        columns={
            0: "DNI",
            1: "TELEFONO",
            2: "TITULAR",
            3: "DIRECCION",
            4: "DEPARTAMENTO",
            5: "PROVINCIA",
            6: "DISTRITO",
            7: "ZONAL",
            8: "ENVIAR",
            9: "ESTADO",
        },
        inplace=True,
    )

    # Filtro de Enviados
    dataset_filtrada = data["ENVIAR"] == "SI"
    dataset_final = data[dataset_filtrada]
    return dataset_final


def ConectarSheetMensaje():
    libro_lectura = cliente.open_by_key(sheets_key)
    hoja_lectura = libro_lectura.worksheet("MENSAJE")
    
    # Definir las celdas a seleccionar
    celdas_a_seleccionar = [
        ["C6", "C8", "C10", "C12", "C14", "C16", "C18"],
        ["E6", "E8", "E10", "E12", "E14", "E16", "E18"],
        ["G6", "G8", "G10", "G12", "G14", "G16", "G18"]
    ]
    
    # Inicializar la lista para almacenar los párrafos
    parrafos = []

    # Iterar sobre las sublistas
    for sublist in celdas_a_seleccionar:
        # Seleccionar las celdas de la sublista actual
        celdas_seleccionadas = hoja_lectura.batch_get(sublist)
        
        # Convertir las listas de valores en cadenas
        celdas_seleccionadas_str = ["\n".join(map(str, celda)) for celda in celdas_seleccionadas if celda]
        
        # Unificar los valores con un salto de línea y agregar a la lista de párrafos
        parrafo = " ".join(celdas_seleccionadas_str)
        parrafos.append(parrafo)

    return parrafos


indice = random.randint(0, 2)

if __name__ == "__main__":

    parrafo = ConectarSheetMensaje()
    print(parrafo[indice])

