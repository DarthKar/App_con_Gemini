import streamlit as st
import pandas as pd
import re
from io import BytesIO

# Función para extraer datos usando regex
def procesar_csv(data):
    # Patrones de regex
    patron_numero_serie = r"Número de serie:\s*(\S+)"
    patron_nombre_productor = r"Productor:\s*([\w\s]+)"
    patron_valor = r"Valor:\s*\$([\d,\.]+)"
    patron_fecha = r"Fecha de compra:\s*(\d{2}/\d{2}/\d{2})"
    patron_contacto = r"Contacto:\s*([\w\s]+),\s*Email:\s*(\S+),\s*Teléfono:\s*(\d+)"
    
    # Convertir datos en líneas
    lineas = data.split("\n")
    
    # Listas para almacenar los datos extraídos
    numeros_serie = []
    nombres_productor = []
    valores = []
    fechas = []
    contactos = []
    
    for linea in lineas:
        numero_serie = re.search(patron_numero_serie, linea)
        nombre_productor = re.search(patron_nombre_productor, linea)
        valor = re.search(patron_valor, linea)
        fecha = re.search(patron_fecha, linea)
        contacto = re.search(patron_contacto, linea)
        
        if numero_serie:
            numeros_serie.append(numero_serie.group(1))
        else:
            numeros_serie.append(None)
        
        if nombre_productor:
            nombres_productor.append(nombre_productor.group(1))
        else:
            nombres_productor.append(None)
        
        if valor:
            valores.append(valor.group(1))
        else:
            valores.append(None)
        
        if fecha:
            fechas.append(fecha.group(1))
        else:
            fechas.append(None)
        
        if contacto:
            contactos.append({
                "Nombre": contacto.group(1),
                "Email": contacto.group(2),
                "Teléfono": contacto.group(3),
            })
        else:
            contactos.append(None)
    
    # Crear un DataFrame
    df = pd.DataFrame({
        "Número de serie del producto": numeros_serie,
        "Nombre del productor": nombres_productor,
        "Valor": valores,
        "Fecha de compra (DD/MM/YY)": fechas,
        "Contacto": contactos
    })
    
    return df

# Configurar Streamlit
st.title("Procesamiento de Productos con Regex")

# Subir archivo
subido = st.file_uploader("Sube tu archivo CSV", type=["csv"])

if subido:
    # Leer archivo subido
    contenido = subido.read().decode("utf-8")
    
    # Procesar contenido
    df = procesar_csv(contenido)
    
    # Mostrar DataFrame en la app
    st.dataframe(df)
    
    # Botón para descargar el archivo Excel
    def convertir_a_excel(dataframe):
        output = BytesIO()
        with pd.ExcelWriter(output, engine="openpyxl") as writer:
            dataframe.to_excel(writer, index=False, sheet_name="Productos")
        return output.getvalue()
    
    archivo_excel = convertir_a_excel(df)
    st.download_button(
        label="Descargar archivo en Excel",
        data=archivo_excel,
        file_name="productos_procesados.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
