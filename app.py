import streamlit as st

def render_landing():
    # URL de la imagen en tu GitHub
    LANDING_IMG = "https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg"

    # CSS TOTAL (Simplificado para evitar el "Pantallazo Blanco")
    st.markdown("""
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        
        /* 1. AJUSTE DE CONTENEDOR PRINCIPAL */
        .main .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            max-width: 100% !important;
        }

        /* 2. HERO SECTION (Más arriba) */
        .hero-section {
            padding: 10px 5% 30px 5%;
            margin-top: -30px; /* Sube el contenido hacia el header */
        }
        .hero-title {
            font-size: 3.8rem !important;
            font-weight: 800;
            color: #1a1a1a;
            line-height: 1;
            margin-bottom: 10px;
        }
        .hero-subtitle {
            font-size: 1.2rem;
            color: #555;
        }
        .img-hero-style {
            width: 100%;
            max-width: 420px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        /* 3. SECCIÓN EXPERIENCIAS (Gris de lado a lado con fallback) */
        .experiences-outer {
            background-color: #d1d5db; /* El gris de tu imagen */
            width: 100%;
            padding: 50px 0;
            margin: 40px 0;
        }
        .experiences-inner {
            padding: 0 8%;
            text-align: center;
        }
        .section-title {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 40px;
            color: #1a1a1a;
        }
        .exp-card { text-align: center; padding: 10px; }
        .exp-circle {
            width: 100px; height: 100px; background-color: white;
            border-radius: 50%; margin: 0 auto 15px auto;
            display: flex; align-items: center; justify-content: center;
            font-size: 2.2rem; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }

        /* 4. FOOTER COMPACTO */
        .footer-black {
            background-color: #1a1a1a;
            color: white;
            padding: 30px 8%;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 20px;
        }
        .footer-col h4 { font-size: 0.9rem; color: white; margin-bottom: 10px; letter-spacing: 1px; }
        .footer-col p { color: #999; font-size: 0.8rem; line-height: 1.4; }
        
        .social-icons-container a { color: white; font-size: 1.3rem; margin-right: 15px; }

        /* WHATSAPP */
        .whatsapp-btn {
            position: fixed; bottom: 20px; right: 20px;
            background-color: #25d366; color: white !important;
            width: 50px; height: 50px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 25px; z-index: 9999;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- RENDERIZADO ---

    # 1. HERO
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Tu aventura de egresados empieza acá.<br>28 años de trayectoria y confianza.</p>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div style="text-align:right;"><img src="{LANDING_IMG}" class="img-hero-style"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. EXPERIENCIAS (Fondo Gris)
    # Usamos un div que envuelve las columnas de Streamlit
    st.markdown('<div class="experiences-outer"><div class="experiences-inner">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Experiencias Inolvidables</h2>', unsafe_allow_html=True)
    
    e1, e2, e3 = st.columns(3)
    with e1:
        st.markdown('<div class="exp-card"><div class="exp-circle">🚌</div><h4>Transporte Premium</h4><p>Unidades modernas para tu seguridad.</p></div>', unsafe_allow_html=True)
    with e2:
        st.markdown('<div class="exp-card"><div class="exp-circle">🏨</div><h4>Hoteles Propios</h4><p>Alojamiento exclusivo de la empresa.</p></div>', unsafe_allow_html=True)
    with e3:
        st.markdown('<div class="exp-card"><div class="exp-circle">🛡️</div><h4>Seguridad 24/7</h4><p>Atención médica y coordinación permanente.</p></div>', unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

    # 3. FOOTER
    st.markdown("""
        <div class="footer-black">
            <div class="footer-col">
                <h4>SERRANO TURISMO</h4>
                <p>Expertos en viajes estudiantiles con casi tres décadas de trayectoria.</p>
            </div>
            <div class="footer-col">
                <h4>CONTACTO</h4>
                <p>📍 Av. Rivadavia 4532 | 📍 Del Cimarrón 1846<br>📞 11-4847-6467</p>
            </div>
            <div class="footer-col">
                <h4>SÍGUENOS</h4>
                <div class="social-icons-container">
                    <a href="https://instagram.com/serrano_turismo" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="https://facebook.com/serranoturismo" target="_blank"><i class="fab fa-facebook"></i></a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. WHATSAPP
    st.markdown('<a href="https://wa.me/5491156096283" class="whatsapp-btn" target="_blank"><i class="fab fa-whatsapp"></i></a>', unsafe_allow_html=True)
