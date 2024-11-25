import streamlit as st
import re

def validar_datos(nombre, correo, telefono, fecha):
    """Valida los datos ingresados por el usuario utilizando expresiones regulares.

    Args:
        nombre: El nombre del usuario.
        correo: La dirección de correo electrónico.
        telefono: El número de teléfono.
        fecha: La fecha de nacimiento.

    Returns:
        Un diccionario con los resultados de la validación para cada campo.
    """

    validaciones = {
        "nombre": re.match(r"^[A-Z][a-zA-Z]+$", nombre),
        "correo": re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$", correo),
        "telefono": re.match(r"^\d{10}$", telefono),
        "fecha": re.match(r"^\d{4}-\d{2}-\d{2}$", fecha)
    }

    return validaciones

def main():
    st.title("Formulario de Registro")

    nombre = st.text_input("Nombre")
    correo = st.text_input("Correo electrónico")
    telefono = st.text_input("Teléfono")
    fecha = st.date_input("Fecha de nacimiento")

    if st.button("Validar"):
        resultados = validar_datos(nombre, correo, telefono, fecha)

        for campo, valido in resultados.items():
            if not valido:
                st.error(f"El campo {campo} no es válido.")
            else:
                st.success(f"El campo {campo} es válido.")

if __name__ == "__main__":
    main()
