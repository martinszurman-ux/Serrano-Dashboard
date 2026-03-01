import streamlit as st
import json
import os

def cargar_datos():
    with open('data.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def guardar_datos(datos):
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def render_admin():
    st.title("⚙️ Panel de Administración")
    
    # Sistema de Login Simple
    if "autenticado" not in st.session_state:
        st.session_state.autenticado = False

    if not st.session_state.autenticado:
        pass_input = st.text_input("Introduce la contraseña de Staff:", type="password")
        if st.button("Ingresar"):
            if pass_input == "serrano2024": # Podés cambiar esta clave
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta")
        return

    # Si está autenticado, mostramos el editor
    st.success("Sesión iniciada como Administrador")
    datos = cargar_datos()
    
    destino_edit = st.selectbox("Seleccionar destino para editar:", list(datos.keys()))
    
    st.markdown(f"### Editando: {destino_edit}")
    
    new_transporte = st.text_input("Descripción Transporte:", datos[destino_edit]["transporte"])
    new_hotel = st.text_input("Nombre del Hotel:", datos[destino_edit]["hotel"])
    new_tarifa = st.number_input("Tarifa Base ($):", value=datos[destino_edit]["tarifa_base"], step=1000)

    if st.button("💾 Guardar Cambios"):
        datos[destino_edit]["transporte"] = new_transporte
        datos[destino_edit]["hotel"] = new_hotel
        datos[destino_edit]["tarifa_base"] = new_tarifa
        guardar_datos(datos)
        st.balloons()
        st.success(f"¡Valores de {destino_edit} actualizados correctamente!")

    if st.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()
