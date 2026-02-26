import streamlit as st
from datetime import datetime

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# Versión: Planes 1-5 + Texto Legal Exacto + Opción Otros
# =================================================================

def render_adhesion(logo_url):
    # Cabecera institucional
    st.image(logo_url, width=180)
    
    st.markdown("<h2 style='text-align: center; color: #1E3A8A; margin-bottom: 0;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    with st.form("form_adhesion_serrano_v3"):
        
        # --- DATOS DE CONTROL ---
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.date_input("Fecha", datetime.now())
        with col2:
            st.text_input("Cliente N°")
        with col3:
            st.text_input("Contrato")
        with col4:
            st.text_input("% L.O.")

        c_inst, c_anio = st.columns(2)
        with c_inst:
            st.text_input("Colegio / Instituto")
        with c_anio:
            st.text_input("Año y División")

        st.markdown("---")
        
        # --- DATOS DEL ALUMNO ---
        st.write("**DATOS DEL ALUMNO / PASAJERO**")
        c_al1, c_al2 = st.columns(2)
        with c_al1:
            st.text_input("Apellido")
            st.text_input("D.N.I. Nº")
            st.date_input("Fecha de Nacimiento", min_value=datetime(2000, 1, 1))
        with c_al2:
            st.text_input("Nombres")
            st.text_input("Nacionalidad", value="Argentina")
            st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

        c_dom1, c_dom2, c_dom3 = st.columns([2, 1, 1])
        with c_dom1:
            st.text_input("Domicilio")
        with c_dom2:
            st.text_input("C.P.")
        with c_dom3:
            st.text_input("Localidad")
        
        c_prov, c_tel = st.columns(2)
        with c_prov:
            st.text_input("Provincia", value="Buenos Aires")
        with c_tel:
            st.text_input("Teléfono (Cod. Área + Número)")

        st.markdown("---")
        
        # --- DATOS DE LOS PADRES ---
        st.write("**DATOS DE LOS PADRES / TUTORES**")
        c_t1, c_t2 = st.columns(2)
        with c_t1:
            st.text_input("Madre / Padre / Tutor (1)")
            st.text_input("D.N.I. (1)")
        with c_t2:
            st.text_input("Madre / Padre / Tutor (2)")
            st.text_input("D.N.I. (2)")
        
        st.text_input("E-mail de contacto:")

        st.markdown("#### OBSERVACIONES")
        st.text_area("Notas adicionales:", label_visibility="collapsed")

        # --- SECCIÓN DE PLANES ---
        st.markdown("---")
        st.write("**Seleccione su plan de pago:**")
        
        col_p1, col_p2 = st.columns([2, 1])
        with col_p1:
            plan_sel = st.pills(
                "Plan Elegido:", 
                options=["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "PLAN 5", "OTROS"], 
                default="PLAN 1", 
                label_visibility="collapsed"
            )
        with col_p2:
            if plan_sel == "OTROS":
                st.text_input("Aclarar otro plan:", placeholder="Especifique aquí...")

        # --- TEXTO LEGAL EXACTO SOLICITADO ---
        st.markdown(f"""
            <div style="font-size: 0.85rem; text-align: justify; color: #333; line-height: 1.5; background-color: #f8f9fa; padding: 20px; border-radius: 10px; border: 1px solid #dee2e6;">
            Declaro bajo juramento que los datos aqui volcados son absolutamente exactos y acepto, para la cancelacion de los servicios 
            a prestar por <b>SERRANO TURISMO</b>, el plan de pagos que figura en la solicitud de reserva mencionada anteriormente.<br><br>
            Los planes contado deberan abonarse dentro de los 30 dias de haberse firmado el contrato.<br><br>
            Ademas declaro conocer todas y cada uno de las condiciones del contrato suscripto por mi y/u otro representantes del contingente de referencia.<br>
            <b>NOTA:</b> de no marcarse ningun plan de pago, su chequera se emitira como <b>PLAN 1</b>.
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.divider()
            st.caption("Firma del Padre/Madre/Tutor")
        with col_f2:
            st.divider()
            st.caption("Aclaración y D.N.I.")

        st.form_submit_button("Finalizar y Guardar")

    # Botón de impresión
    st.button("🖨️ Enviar a Imprimir Formulario", on_click=lambda: st.write('<script>window.print();</script>', unsafe_allow_html=True))
