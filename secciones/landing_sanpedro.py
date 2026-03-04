import streamlit as st
import os
# Importamos el footer institucional desde tu archivo de utilidades
from utilidades.footer import render_footer

def render_landing_sp():
    """
    Renderiza la landing page completa de San Pedro.
    Asegúrate de que la imagen esté en: assets/landing_sanPedro_imagen.png
    """
    
    # --- 1. ESTILOS CSS ESPECÍFICOS DE LA LANDING ---
    st.markdown("""
        <style>
        /* Tipografía y Colores */
        .hero-title {
            font-size: 52px;
            font-weight: 800;
            color: #1b5e20;
            line-height: 1.1;
            margin-bottom: 20px;
        }
        .sub-text {
            font-size: 1.2rem;
            color: #444;
            margin-bottom: 30px;
        }
        /* Botón personalizado de la landing */
        .stButton>button {
            background-color: #2e7d32;
            color: white;
            border-radius: 30px;
            padding: 0.6rem 2.5rem;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #1b5e20;
            transform: translateY(-2px);
        }
        /* Tarjetas de actividades */
        .activity-card {
            background-color: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border-left: 5px solid #2e7d32;
            height: 100%;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 2. SECCIÓN HERO (Encabezado) ---
    col_text, col_img = st.columns([1.1, 0.9], gap="large")

    with col_text:
        st.markdown('<h1 class="hero-title">San Pedro:<br>Naturaleza y Sabor</h1>', unsafe_allow_html=True)
        st.markdown("""
            <p class="sub-text">
                Escapate a la ciudad de los azahares. Disfrutá de la calidez del río Paraná, 
                recorré túneles históricos y deleitate con la auténtica ensaimada mallorquina. 
                <b>A solo 90 minutos de la ciudad.</b>
            </p>
        """, unsafe_allow_html=True)
        
        if st.button("Quiero Reservar Mi Escapada", key="btn_reserva_sp"):
            st.toast("¡Preparando tus opciones para San Pedro! 🌿")

    with col_img:
        # Lógica de carga de imagen robusta
        img_path = "assets/landing_sanPedro_imagen.png"
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True, caption="Vistas del Paraná en San Pedro")
        else:
            # Placeholder elegante si no hay imagen
            st.info("🖼️ Imagen de San Pedro próximamente disponible.")
            st.markdown("""
                <div style="width:100%; height:300px; background:#e0e0e0; border-radius:15px; 
                display:flex; align-items:center; justify-content:center; color:#888;">
                Espacio reservado para landing_sanPedro_imagen.png
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.divider()

    # --- 3. SECCIÓN EXPERIENCIAS ---
    st.markdown("<h2 style='text-align: center; color: #1b5e20;'>Experiencias Imperdibles</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Todo lo que necesitás para un fin de semana perfecto</p>", unsafe_allow_html=True)
    st.write("")

    exp_col1, exp_col2, exp_col3 = st.columns(3)

    with exp_col1:
        st.markdown("""
            <div class="activity-card">
                <h3>🚣 Náutica</h3>
                <p>Navegación por las islas, alquiler de kayaks y pesca deportiva en el Delta del Paraná.</p>
            </div>
        """, unsafe_allow_html=True)

    with exp_col2:
        st.markdown("""
            <div class="activity-card">
                <h3>🥐 Sabores</h3>
                <p>Circuito gastronómico de la Ensaimada, visitas a plantaciones de cítricos y asados al asador.</p>
            </div>
        """, unsafe_allow_html=True)

    with exp_col3:
        st.markdown("""
            <div class="activity-card">
                <h3>🏛️ Historia</h3>
                <p>Visita al sitio histórico de la Batalla de la Vuelta de Obligado y museos locales.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- 4. SECCIÓN CONTACTO RÁPIDO ---
    with st.container():
        st.markdown("""
            <div style="background-color: #f1f8e9; padding: 40px; border-radius: 20px; text-align: center;">
                <h3>¿Necesitás asesoramiento personalizado?</h3>
                <p>Nuestros expertos en San Pedro te ayudan a planificar tu itinerario sin cargo.</p>
            </div>
        """, unsafe_allow_html=True)
        
        c_left, c_mid, c_right = st.columns([1, 2, 1])
        with c_mid:
            with st.form("sp_contact_form"):
                nombre = st.text_input("Nombre")
                tel = st.text_input("WhatsApp")
                submit = st.form_submit_button("Enviar consulta ahora")
                if submit:
                    st.success(f"¡Gracias {nombre}! Un asesor de Serrano Turismo te escribirá en breve.")

    # --- 5. FOOTER INSTITUCIONAL ---
    # Invocamos la función del archivo utilidades/footer.py
    render_footer()
