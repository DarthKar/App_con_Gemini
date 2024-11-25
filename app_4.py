import streamlit as st
import re

st.title("Buscador Inteligente de Patrones de Texto")

# Opciones para cargar texto
st.sidebar.header("Selecciona una opción:")
option = st.sidebar.radio("", ["Escribir texto", "Cargar archivo"])

if option == "Escribir texto":
    text_input = st.text_area("Ingrese el texto aquí:")
else:
    uploaded_file = st.file_uploader("Cargar archivo de texto")
    if uploaded_file is not None:
        text_input = uploaded_file.read().decode('utf-8')

# Campo para la expresión regular
regex_pattern = st.text_input("Ingrese la expresión regular:")

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
    if st.button("Exportar"):
        if export_format == "CSV":
            import csv
            with open("resultados.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Coincidencia"])
                for match in matches:
                    writer.writerow([match])
            st.success("Resultados exportados a CSV")
        else:
            import json
            with open("resultados.json", "w") as jsonfile:
                json.dump(matches, jsonfile)
            st.success("Resultados exportados a JSON")
