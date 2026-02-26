import streamlit as st
from datetime import datetime

def render_adhesion(LOGO_URL):
    st.image(LOGO_URL, width=180)
    st.markdown("<h2 style='text-align: center;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    
    with st.form("form_adhesion_original"):
        # ... Aquí va el resto del código del formulario que me pasaste ...
        st.write("DATOS DEL ALUMNO")
        st.text_input("Apellido")
        st.form_submit_button("Guardar Formulario")
