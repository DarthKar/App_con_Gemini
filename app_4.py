import streamlit as st
import re
import csv
import json

st.title("Buscador Inteligente de Patrones de Texto")
st.write("Por: Miguel Angel Peña Marin")

# Opciones para cargar texto
st.sidebar.header("Selecciona una opción:")
option = st.sidebar.radio("", ["Escribir texto", "Cargar archivo"])

# Variable inicial para el texto
text_input = ""

if option == "Escribir texto":
    text_input = st.text_area("Ingrese el texto aquí:")
else:
    uploaded_file = st.file_uploader("Cargar archivo de texto")
    if uploaded_file is not None:
        text_input = uploaded_file.read().decode('utf-8')

# Campo para la expresión regular
regex_pattern = st.text_input("Ingrese la expresión regular:")

# Inicializar variable de coincidencias
matches = []

# Botón para buscar
if st.button("Buscar"):
    try:
        matches = re.findall(regex_pattern, text_input)
        if matches:
            st.success("Coincidencias encontradas:")
            for match in matches:
                st.write(match)
        else:
            st.warning("No se encontraron coincidencias.")
    except re.error as e:
        st.error(f"Error en la expresión regular: {e}")

# Opciones para exportar resultados
if matches:
    st.sidebar.header("Exportar resultados:")
    export_format = st.sidebar.radio("", ["CSV", "JSON"])
    if st.sidebar.button("Exportar"):  # Cambiar el botón a la barra lateral
        if export_format == "CSV":
            # Crear archivo CSV en memoria
            csv_data = "Coincidencia\n" + "\n".join(matches)
            st.download_button(
                label="Descargar CSV",
                data=csv_data.encode("utf-8"),
                file_name="resultados.csv",
                mime="text/csv"
            )
        elif export_format == "JSON":
            # Crear archivo JSON en memoria
            json_data = json.dumps(matches, indent=2)
            st.download_button(
                label="Descargar JSON",
                data=json_data.encode("utf-8"),
                file_name="resultados.json",
                mime="application/json"
            )
