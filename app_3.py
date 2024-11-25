import streamlit as st
import pandas as pd
import re
from io import BytesIO

# Función para procesar el contenido del archivo CSV
def procesar_csv(data):
    # Patrones regex para extraer la información
    patron_numero_serie = r'\b\d{6}\b'  # Número de serie: 6 dígitos
    patron_nombre = r'[A-Z][a-z]+\s[A-Z][a-z]+'  # Nombres completos
    patron_valor = r'\b\d+\.\d{2}\b'  # Valores con dos decimales
    patron_fecha = r'\b\d{2}/\d{2}/\d{2}\b'  # Fechas en formato DD/MM/YY
    patron_contacto = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'  # Correos electrónicos
    patron_telefono = r'\+\d{2}\s\d{9}'  # Teléfonos en formato internacional

    # Dividir los datos en líneas
    lineas = data.split("\n")

    # Listas para almacenar resultados
    numeros_serie = []
    nombres_productor = []
    valores = []
    fechas = []
    contactos = []

    for linea in lineas:
        numero_serie = re.search(patron_numero_serie, linea)
        nombre_productor = re.search(patron_nombre, linea)
        valor = re.search(patron_valor, linea)
        fecha = re.search(patron_fecha, linea)
        contacto_email = re.search(patron_contacto, linea)
        contacto_telefono = re.search(patron_telefono, linea)

        # Agregar datos procesados
        numeros_serie.append(numero_serie.group(0) if numero_serie else None)
        nombres_productor.append(nombre_productor.group(0) if nombre_productor else None)
        valores.append(valor.group(0) if valor else None)
        fechas.append(fecha.group(0) if fecha else None)
        contactos.append({
            "Email": contacto_email.group(0) if contacto_email else None,
            "Teléfono": contacto_telefono.group(0) if contacto_telefono else None
        })

    # Crear DataFrame
    df = pd.DataFrame({
        "Número de serie del producto": numeros_serie,
        "Nombre del productor": nombres_productor,
        "Valor": valores,
        "Fecha de compra (DD/MM/YY)": fechas,
        "Contacto": [str(c) for c in contactos]
    })

    return df

# Configuración de Streamlit
st.title("Procesador de Productos con Regex")

# Subir archivo CSV
archivo_subido = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if archivo_subido:
    # Leer contenido del archivo subido
    contenido = archivo_subido.read().decode("utf-8")
    
    # Procesar el archivo con la función
    df_procesado = procesar_csv(contenido)
    
    # Mostrar el DataFrame procesado
    st.write("Datos procesados:")
    st.dataframe(df_procesado)
    
    # Función para convertir el DataFrame a Excel
    def convertir_a_excel(df):
        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            df.to_excel(writer, index=False, sheet_name="Productos")
        return output.getvalue()

    # Descargar archivo Excel
    archivo_excel = convertir_a_excel(df_procesado)
    st.download_button(
        label="Descargar archivo procesado en Excel",
        data=archivo_excel,
        file_name="productos_procesados.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
