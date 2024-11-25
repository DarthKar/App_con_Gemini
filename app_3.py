import streamlit as st
import pandas as pd
import csv
import io

def extraer_datos(uploaded_file):
    """Extrae datos de un archivo CSV y los organiza en un DataFrame.

    Args:
        uploaded_file: El archivo CSV subido.

    Returns:
        pd.DataFrame: DataFrame con los datos extraídos.
    """

    file_contents = io.BytesIO(uploaded_file.read()).getvalue().decode('utf-8')

    datos = []
    with csv.reader(file_contents.splitlines(), delimiter=csv.Sniffer().sniff(file_contents).delimiter) as reader:
        for row in reader:
            # Asegurarse de que haya al menos 5 campos
            if len(row) >= 5:
                numero_serie, nombre_producto, valor, fecha, contacto = row[:5]

                # Validación y extracción de datos
                try:
                    valor = float(valor)
                    match_fecha = re.match(r"(\d{2})/(\d{2})/(\d{2})", fecha)
                    dia, mes, anio = match_fecha.groups()

                    # Separar el contacto en número de teléfono o correo electrónico
                    if "+" in contacto:
                        telefono = contacto
                        email = None
                    else:
                        telefono = None
                        email = contacto

                    datos.append([numero_serie, nombre_producto, valor, dia, mes, anio, telefono, email])
                except ValueError:
                    print(f"Error al procesar la línea: {row}")

    df = pd.DataFrame(datos, columns=["Número de serie", "Nombre del producto", "Valor", "Día", "Mes", "Año", "Teléfono", "Email"])
    return df

if __name__ == "__main__":
    st.title("Visualizador de Datos CSV")

    # Cargar el archivo CSV
    uploaded_file = st.file_uploader("Selecciona el archivo CSV", type="csv")
    if uploaded_file is not None:
        df = extraer_datos(uploaded_file)

        # Mostrar el DataFrame en una tabla interactiva
        st.dataframe(df)
