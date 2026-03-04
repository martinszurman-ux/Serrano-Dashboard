import streamlit as st
import os
from utilidades.footer import render_footer

def render_landing_cp():
    """
    Renderiza la landing page completa de Villa Carlos Paz.
    Asegúrate de que la imagen esté en: assets/landingcarlospazimagen.png
    """
    
    # --- 1. ESTILOS CSS ESPECÍFICOS DE LA LANDING ---
    st.markdown("""
        <style>
        /* Tipografía y Colores */
        .hero-title {
            font-size: 60px;
            font-weight: 900;
            color: #1E3A8A; /* Azul Serrano */
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
            background-color: #1E3A8A;
            color: white;
            border-radius: 30px;
            padding: 0.6rem 2.5rem;
            font-weight: bold;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #112255;
            transform: translateY(-2px);
            color: white;
        }
        /* Tarjetas de actividades */
        .activity-card {
            background-color: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            border-left: 5px solid #1E3A8A;
            height: 100%;
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
        st.markdown('<h1 class="hero-title">CARLOS PAZ</h1>', unsafe_allow_html=True)
        st.markdown("""
            <p class="sub-text">
                El destino por excelencia para tu viaje de egresados. Una experiencia completa que combina las sierras, diversión asegurada y la mejor infraestructura para vivir días inolvidables junto a tus compañeros.
            </p>
        """, unsafe_allow_html=True)
        
        if st.button("Ver opciones de Hotelería", key="btn_reserva_cp"):
            st.toast("¡Preparando tus opciones para Carlos Paz! ⛰️")
            st.query_params["nav"] = "Hoteleria"
            st.rerun()

    with col_img:
        # Lógica de carga de imagen robusta
        img_path = "assets/landingcarlospazimagen.png"
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True, caption="El corazón del Valle de Punilla")
        else:
            st.info("🖼️ Imagen de Carlos Paz próximamente disponible.")
            st.markdown("""
                <div style="width:100%; height:300px; background:#e0e0e0; border-radius:15px; 
                display:flex; align-items:center; justify-content:center; color:#888;">
                Espacio reservado para landingcarlospazimagen.png
                </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

    # --- 3. VIDEO INSTITUCIONAL EN MARCO DE TV ---
    st.markdown("""
        <div class="tv-wrapper">
            <h3 style="text-align: center; color: #1E3A8A; margin-bottom: 20px;">Conocé nuestra experiencia en Carlos Paz</h3>
            <div class="tv-frame">
                <div class="tv-screen">
                    <iframe src="https://www.youtube.com/embed/ZG_3Bc8wkx8?start=31&autoplay=0&rel=0" allowfullscreen></iframe>
                </div>
            </div>
            <div class="tv-stand"></div>
            <div class="tv-base"></div>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # --- 4. SECCIÓN EXPERIENCIAS EGRESADOS ---
    st.markdown("<h2 style='text-align: center; color: #1E3A8A;'>Tu Viaje de Egresados Inolvidable</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #666;'>Todo está diseñado para que disfruten al máximo de manera segura y dinámica.</p>", unsafe_allow_html=True)
    st.write("")

    exp_col1, exp_col2, exp_col3 = st.columns(3)

    with exp_col1:
        st.markdown("""
            <div class="activity-card">
                <h3>📍 Cercanía Estratégica</h3>
                <p>Menos tiempo viajando y más tiempo disfrutando. Nuestros hoteles están ubicados a minutos de los principales complejos y excursiones de la Villa.</p>
            </div>
        """, unsafe_allow_html=True)

    with exp_col2:
        st.markdown("""
            <div class="activity-card">
                <h3>🏞️ Entorno Único</h3>
                <p>Rodeados por las sierras cordobesas y el imponente Lago San Roque, el escenario perfecto para vivir aventuras al aire libre y sacar las mejores fotos.</p>
            </div>
        """, unsafe_allow_html=True)

    with exp_col3:
        st.markdown("""
            <div class="activity-card">
                <h3>🎉 Actividades Exclusivas</h3>
                <p>Desde parques acuáticos y multiparques de diversiones durante el día, hasta actividades recreativas y cenas inolvidables pensadas para el grupo.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # --- 5. FOOTER INSTITUCIONAL ---
    render_footer()

if __name__ == "__main__":
    render_landing_cp()
