import streamlit as st
import pandas as pd
import re
import io

def extraer_datos(uploaded_file):
    """Extrae datos de un archivo CSV y los organiza en un DataFrame.

    Args:
        uploaded_file: The uploaded file object.

    Returns:
        pd.DataFrame: DataFrame con los datos extraídos.
    """

    file_contents = io.BytesIO(uploaded_file.read()).getvalue().decode('utf-8')

    datos = []
    for linea in file_contents.splitlines():
        numero_serie, nombre_producto, valor, fecha, contacto = linea.strip().split(',')

        # Validación y extracción de datos
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

    df = pd.DataFrame(datos, columns=["Número de serie", "Nombre del producto", "Valor", "Día", "Mes", "Año", "Teléfono", "Email"])
    return df

def generar_excel(df, nombre_archivo):
    """Genera un archivo Excel a partir de un DataFrame.

    Args:
        df (pd.DataFrame): DataFrame con los datos.
        nombre_archivo (str): Nombre del archivo Excel a generar.
    """

    df.to_excel(nombre_archivo, index=False)

if __name__ == "__main__":
    st.title("Generador de Excel a partir de CSV")

    # Cargar el archivo CSV
    uploaded_file = st.file_uploader("Selecciona el archivo CSV", type="csv")
    if uploaded_file is not None:
        df = extraer_datos(uploaded_file)

        # Mostrar un preview del DataFrame
        st.dataframe(df)

        # Generar el archivo Excel
        if st.button("Generar Excel"):
            nombre_archivo = "productos.xlsx"
            generar_excel(df, nombre_archivo)
            st.success(f"Archivo Excel generado: {nombre_archivo}")
