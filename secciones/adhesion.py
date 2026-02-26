import streamlit as st
from datetime import datetime

def render_adhesion(LOGO_URL):
    st.image(LOGO_URL, width=180)
    st.markdown("<h2 style='text-align: center;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    with st.form("form_adhesion_modular"):
        col1, col2, col3, col4 = st.columns(4)
        with col1: f_doc = st.date_input("Fecha", datetime.now())
        with col2: c_num = st.text_input("Cliente N°")
        with col3: cont = st.text_input("Contrato")
        with col4: perc_lo = st.text_input("% L.O.")

        c_inst, c_anio = st.columns(2)
        with c_inst: colegio = st.text_input("Colegio / Instituto")
        with c_anio: anio_div = st.text_input("Año y Div.")

        st.markdown("---")
        st.write("**DATOS DEL ALUMNO**")
        c_al1, c_al2 = st.columns(2)
        with c_al1:
            ape_al = st.text_input("Apellido")
            dni_al = st.text_input("D.N.I. Nº")
            fnac_al = st.date_input("Fecha de Nacimiento", min_value=datetime(2000,1,1))
        with c_al2:
            nom_al = st.text_input("Nombres")
            nac_al = st.text_input("Nacionalidad", value="Argentina")
            sex_al = st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

        st.markdown("---")
        st.markdown("#### OBSERVACIONES")
        obs_val = st.text_area("", label_visibility="collapsed")
        
        plan_elegido = st.radio("Seleccione Plan:", ["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "OTROS"], horizontal=True)

        st.form_submit_button("Guardar Formulario")

    st.button("🖨️ Imprimir Formulario", on_click=lambda: st.write('<script>window.print();</script>', unsafe_allow_html=True))
