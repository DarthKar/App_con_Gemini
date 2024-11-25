
import streamlit as st
import re

def evaluar_contrasena(contrasena):
    # Expresiones regulares para cada criterio
    mayuscula = re.compile(r'[A-Z]')
    minuscula = re.compile(r'[a-z]')
    numero = re.compile(r'\d')
    especial = re.compile(r'[^a-zA-Z0-9]')

    # Validar la longitud y cada criterio
    if len(contrasena) < 8:
        return "La contraseña debe tener al menos 8 caracteres."
    elif not mayuscula.search(contrasena):
        return "La contraseña debe incluir al menos una letra mayúscula."
    elif not minuscula.search(contrasena):
        return "La contraseña debe incluir al menos una letra minúscula."
    elif not numero.search(contrasena):
        return "La contraseña debe incluir al menos un número."
    elif not especial.search(contrasena):
        return "La contraseña debe incluir al menos un carácter especial."
    else:
        return "La contraseña es segura."

# Interfaz de usuario de Streamlit
st.title("Evaluador de Contraseñas")
contrasena = st.text_input("Ingrese su contraseña")

if contrasena:
    resultado = evaluar_contrasena(contrasena)
    st.write(resultado)

    # Sugerencias personalizadas
    if "mayúscula" in resultado:
        st.write("Sugerencia: Incluye al menos una letra mayúscula.")
    if "minúscula" in resultado:
        st.write("Sugerencia: Incluye al menos una letra minúscula.")
    if "número" in resultado:
        st.write("Sugerencia: Incluye al menos un número.")
    if "especial" in resultado:
        st.write("Sugerencia: Incluye al menos un carácter especial.")
