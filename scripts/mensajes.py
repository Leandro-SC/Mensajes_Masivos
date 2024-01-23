import time
import random
import webbrowser
import pyautogui



def enviar_mensajes(base_info,parrafos):

    #Variable de dataframe
    dataset = base_info

    # Verificamos si la columna TELEFONO está vacía
    if dataset["TELEFONO"].empty:
        print("No hay números de teléfono en el DataFrame.")
        exit()

    for fila in dataset["TELEFONO"]:

        num_celular = "51" + str(fila)

        indice = random.randint(0, 2)
        nuevos_parrafos = []

        # Resultado
        for i, parrafo in enumerate(parrafos):
            # Reemplazar los corchetes y comillas por espacios vacíos en cada párrafo
            parrafo_con_formato = parrafo.replace("[", " ").replace("]", "\n \n").replace("'", " ")
            nuevos_parrafos.append(parrafo_con_formato)

        mensaje = nuevos_parrafos[indice]
        # Abrimos la URL en el navegador web (esto abrirá el navegador predeterminado)
        webbrowser.open(
            "https://web.whatsapp.com/send?phone=%" + str(num_celular) + "&text=" + mensaje
        )

        time.sleep(18)  # Tiempo de espera

        # Usamos pyautogui para enviar la tecla Enter
        pyautogui.typewrite('\n')


        time.sleep(3)  # Ajusta el tiempo de espera según sea necesario

        # Simulamos la pulsación de Ctrl + W para cerrar la pestaña
        pyautogui.hotkey("ctrl", "w")

        time.sleep(7)  # Ajusta el tiempo de espera según sea necesario

    print("Proceso culminado")    

