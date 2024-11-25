import csv
import streamlit as st
import pandas as pd
import io

def extraer_datos(uploaded_file):
    """Extrae datos de un archivo CSV y los organiza en un DataFrame.

    Args:
        uploaded_file: El archivo CSV subido.

    Returns:
        pd.DataFrame: DataFrame con los datos extraídos.
    """

    # Lee el contenido del archivo y lo decodifica
    file_contents = uploaded_file.read().decode('utf-8')

    # Crea un lector CSV para procesar las líneas
    reader = csv.reader(file_contents.splitlines(), delimiter=csv.Sniffer().sniff(file_contents))

    datos = []
    for row in reader:
        # Asegúrate de que haya al menos 5 campos
        if len(row) >= 5:
            # Extrae los datos de la fila
            numero_serie, nombre_producto, valor, fecha, contacto = row[:5]

            # Validación y extracción de datos (puedes agregar más validaciones si es necesario)
            try:
                valor = float(valor)
                # ... otras validaciones ...
                datos.append([numero_serie, nombre_producto, valor, fecha, contacto])
            except ValueError:
                print(f"Error al procesar la línea: {row}")

    # Crea un DataFrame con los datos
    df = pd.DataFrame(datos, columns=["Número de serie", "Nombre del producto", "Valor", "Fecha", "Contacto"])
    return df

if __name__ == "__main__":
    st.title("Visualizador de Datos CSV")

    # Cargar el archivo CSV
    uploaded_file = st.file_uploader("Selecciona el archivo CSV", type="csv")
    if uploaded_file is not None:
        df = extraer_datos(uploaded_file)

        # Mostrar el DataFrame en una tabla interactiva
        st.dataframe(df)
