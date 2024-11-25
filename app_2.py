import streamlit as st
import pandas as pd
import re

def validar_nombre(nombre):
    """Valida si el nombre solo contiene caracteres alfabéticos y comienza con mayúscula."""
    patron = r"^[A-Z][a-zA-Z]*$"
    return bool(re.match(patron, nombre))

def validar_email(email):
    """Valida un formato de correo electrónico básico."""
    patron = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(patron, email))

def validar_telefono(telefono):
    """Valida un número de teléfono de 10 dígitos (ajusta según tu formato)."""
    patron = r"^\d{10}$"
    return bool(re.match(patron, telefono))

def validar_fecha(fecha):
    """Valida una fecha en formato YYYY-MM-DD."""
    patron = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(patron, fecha))

def main():
    st.title("Formulario de Validación")

    with st.form("my_form"):
        nombre = st.text_input("Nombre:")
        email = st.text_input("Correo electrónico:")
        telefono = st.text_input("Teléfono:")
        fecha = st.text_input("Fecha (AAAA-MM-DD):")
        submitted = st.form_submit_button("Validar")

        if submitted:
            if not validar_nombre(nombre):
                st.error("Nombre inválido. Solo se permiten letras y debe iniciar con mayúscula.")
            if not validar_email(email):
                st.error("Correo electrónico inválido.")
            if not validar_telefono(telefono):
                st.error("Número de teléfono inválido.")
            if not validar_fecha(fecha):
                st.error("Fecha inválida. Utiliza el formato AAAA-MM-DD.")

            if validar_nombre(nombre) and validar_email(email) and validar_telefono(telefono) and validar_fecha(fecha):
                st.success("¡Todos los datos son válidos!")

if __name__ == "__main__":
    main()
