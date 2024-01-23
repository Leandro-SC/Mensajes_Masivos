from scripts import mensajes
from models import sheets

datos = sheets.convertir_archivo_pandas()
mensaje = sheets.ConectarSheetMensaje()

# Preguntar para ejeuctar script
try:
    pregunta = input("¿Deseas iniciar el envío de mensajes?: s/n \n")
except Exception as e:
    print(e)


def main():
    mensajes.enviar_mensajes(datos, mensaje)


if __name__ == "__main__":
    try:
        if pregunta == "s":
            main()
    except Exception as e:
        print(f"Error: {e}")
        input("Presiona Enter para cerrar...")
