import streamlit as st

def render_solicitud():
    st.markdown("<h1 style='text-align: center; color: #1E3A8A;'>📝 SOLICITUD DE ADHESIÓN</h1>", unsafe_allow_html=True)
    st.markdown("---")

    st.write("Seleccioná el plan que mejor se adapte a tu grupo para comenzar con la gestión del viaje.")

    # Definimos los nombres de los planes de forma clara
    planes = ["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4"]
    
    # Widget de selección con los nombres corregidos
    seleccion = st.radio(
        "Elija su plan de viaje:",
        planes,
        horizontal=True,
        index=0
    )

    st.success(f"Has seleccionado el **{seleccion}**")

    # Formulario de adhesión
    with st.form("formulario_adhesion"):
        st.subheader("Datos del Pasajero")
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre Completo")
            dni = st.text_input("DNI")
        with col2:
            fecha_nac = st.date_input("Fecha de Nacimiento")
            colegio = st.text_input("Institución Educativa")

        st.subheader("Datos del Responsable")
        nombre_tutor = st.text_input("Nombre del Padre/Madre/Tutor")
        tel_tutor = st.text_input("WhatsApp de contacto")

        st.markdown("---")
        st.info("💡 **Recordá:** Contamos con presupuestos a medida y planes de pago en cuotas.")
        
        enviado = st.form_submit_button("ENVIAR SOLICITUD")
        
        if enviado:
            if nombre and dni and tel_tutor:
                st.balloons()
                st.success(f"¡Solicitud del {seleccion} enviada con éxito! Nos contactaremos al {tel_tutor}.")
            else:
                st.error("Por favor, completá los campos obligatorios para procesar la adhesión.")

    st.caption("Al enviar este formulario, un asesor de Serrano Turismo se pondrá en contacto para finalizar el alta.")
