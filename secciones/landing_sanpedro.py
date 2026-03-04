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
            font-size: 60px;
            font-weight: 900;
            color: #1b5e20;
            line-height: 1.1;
            margin-bottom: 20px;
            text-transform: uppercase;
        }
        .sub-text {
            font-size: 1.2rem;
            color: #444;
            margin-bottom: 30px;
            line-height: 1.5;
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
        
        /* Sección de Trayectoria */
        .trayectoria-box {
            background-color: #f8f9fa;
            border-left: 5px solid #1b5e20;
            padding: 20px 30px;
            border-radius: 10px;
            margin: 30px 0;
            font-size: 18px;
            color: #333;
        }

        /* Marco de TV para el Video */
        .tv-wrapper {
            margin: 50px auto;
            max-width: 800px;
        }
        .tv-frame {
            position: relative;
            background: #2c2c2c;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 15px 35px rgba(0,0,0,0.4), inset 0px 0px 10px rgba(255,255,255,0.1);
            border: 2px solid #111;
        }
        .tv-screen {
            position: relative;
            padding-bottom: 56.25%; /* Relación de aspecto 16:9 */
            height: 0;
            overflow: hidden;
            border-radius: 8px;
            background: #000;
            box-shadow: inset 0px 0px 15px rgba(0,0,0,0.8);
        }
        .tv-screen iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }
        .tv-stand {
            width: 120px;
            height: 25px;
            background: #2c2c2c;
            margin: 0 auto;
            border-radius: 0 0 10px 10px;
            border: 2px solid #111;
            border-top: none;
        }
        .tv-base {
            width: 250px;
            height: 12px;
            background: #111;
            margin: 0 auto;
            border-radius: 10px;
            box-shadow: 0px 5px 10px rgba(0,0,0,0.5);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 2. SECCIÓN HERO (Encabezado) ---
    col_text, col_img = st.columns([1.1, 0.9], gap="large")

    with col_text:
        st.markdown('<h1 class="hero-title">SAN PEDRO</h1>', unsafe_allow_html=True)
        st.markdown("""
            <p class="sub-text">
                Un destino que abrimos hace 17 años, cercano y con la estructura para poder realizar el viaje de egresados de una manera divertida y segura.
            </p>
        """, unsafe_allow_html=True)
        
        if st.button("Ver opciones de Hotelería", key="btn_reserva_sp"):
            # Combinamos tu toast con la navegación a Hotelería
            st.toast("¡Preparando tus opciones para San Pedro! 🌿")
            st.query_params["nav"] = "Hoteleria"
            st.rerun()

    with col_img:
        # Lógica de carga de imagen robusta
        img_path = "assets/landing_sanPedro_imagen.png"
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True, caption="Tu viaje inolvidable")
        else:
            # Placeholder elegante si no hay imagen
            st.info("🖼️ Imagen de San Pedro próximamente disponible.")
            st.markdown("""
                <div style="width:100%; height:300px; background:#e0e0e0; border-radius:15px; 
                display:flex; align-items:center; justify-content:center; color:#888;">
                Espacio reservado para landing_sanPedro_imagen.png
                </div>
            """, unsafe_allow_html=True)

    # --- SECCIÓN TRAYECTORIA EMPRESA ---
    st.markdown("""
        <div class="trayectoria-box">
            <strong>Con 29 años de trayectoria ininterrumpida</strong>, en Serrano Turismo hemos consolidado una marca definida por la transparencia y la responsabilidad. Nuestra mayor recompensa es haber cumplido el sueño del viaje de egresados a más de <strong>100.000 chicos</strong>.
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

    # --- VIDEO INSTITUCIONAL EN MARCO DE TV ---
    st.markdown("""
        <div class="tv-wrapper">
            <h3 style="text-align: center; color: #1b5e20; margin-bottom: 20px;">Conocé nuestra experiencia en San Pedro</h3>
            <div class="tv-frame">
                <div class="tv-screen">
                    <iframe src="https://www.youtube.com/embed/xBDqSrNB8Ro?autoplay=0&rel=0" allowfullscreen></iframe>
                </div>
            </div>
            <div class="tv-stand"></div>
            <div class="tv-base"></div>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # --- 3. SECCIÓN EXPERIENCIAS ---
    st.markdown("<h2 style='text-align: center; color: #1b5e20;'>Experiencias Imperdibles</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Todo lo que necesitás para un viaje perfecto</p>", unsafe_allow_html=True)
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
