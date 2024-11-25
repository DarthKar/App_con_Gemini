import streamlit as st
import re

def evaluar_contrasena(contrasena):
    """Evalúa la fortaleza de una contraseña y devuelve un diccionario con las condiciones faltantes."""
    # Expresiones regulares para cada criterio
    mayuscula = re.compile(r'[A-Z]')
    minuscula = re.compile(r'[a-z]')
    numero = re.compile(r'\d')
    especial = re.compile(r'[^a-zA-Z0-9]')

    # Condiciones faltantes
    faltantes = {
        'longitud mayor o igual a 8': len(contrasena) < 8,
        'al menos una mayuscula': not mayuscula.search(contrasena),
        'al menos una minuscula': not minuscula.search(contrasena),
        'al menos un numero': not numero.search(contrasena),
        'al menos un caracter especial': not especial.search(contrasena)
    }

    return faltantes

# Interfaz de usuario de Streamlit
st.title("Evaluador de Contraseñas")
contrasena = st.text_input("Ingrese su contraseña")
st.write("programado por miguel angel peña marin")

if contrasena:
    faltantes = evaluar_contrasena(contrasena)
    
    if all(not valor for valor in faltantes.values()):
        st.success("¡La contraseña es segura!")
    else:
        st.error("La contraseña no cumple con los siguientes criterios:")
        for criterio, falta in faltantes.items():
            if falta:
                st.write(f"- {criterio}.")
