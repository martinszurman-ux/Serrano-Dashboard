import streamlit as st

def render_landing():
    # URL de la imagen en tu GitHub
    LANDING_IMG = "https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg"

    # CSS TOTAL REFORMULADO
    st.markdown("""
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        
        /* 1. RESET ESTRUCTURAL */
        .main .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0px !important;
            max-width: 100% !important;
        }

        /* 2. HERO SECTION (Mucho más arriba) */
        .hero-section {
            padding: 20px 8% 40px 8%;
            background-color: white;
        }
        .hero-title {
            font-size: 4rem !important;
            font-weight: 800;
            color: #1a1a1a;
            line-height: 1;
            margin-top: 0px !important;
        }
        .hero-subtitle {
            font-size: 1.2rem;
            color: #555;
            margin-top: 20px;
        }
        .img-hero-style {
            width: 100%;
            max-width: 450px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        /* 3. SECCIÓN EXPERIENCIAS (Fondo gris de lado a lado) */
        .experiences-container {
            background-color: #d1d5db; /* Gris de la referencia */
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            padding: 60px 8%;
            text-align: center;
        }
        .section-title {
            font-size: 2.2rem;
            font-weight: 700;
            margin-bottom: 40px;
            color: #1a1a1a;
        }
        .exp-card { text-align: center; }
        .exp-circle {
            width: 110px; height: 110px; background-color: white;
            border-radius: 50%; margin: 0 auto 20px auto;
            display: flex; align-items: center; justify-content: center;
            font-size: 2.5rem; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        }

        /* 4. FOOTER COMPACTO Y PEGADO AL FONDO */
        .footer-full {
            background-color: #1a1a1a;
            color: white;
            padding: 40px 8%;
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 20px;
        }
        .footer-col { flex: 1; min-width: 250px; }
        .footer-col h4 { font-size: 1rem; margin-bottom: 15px; letter-spacing: 1px; }
        .footer-col p { color: #999; font-size: 0.85rem; line-height: 1.5; }
        
        /* Redes Sociales */
        .social-icons-container { display: flex; gap: 15px; margin-top: 10px; }
        .social-icons-container a { color: white; font-size: 1.3rem; transition: 0.3s; }
        .social-icons-container a:hover { color: #25d366; }

        /* WHATSAPP */
        .whatsapp-btn {
            position: fixed; bottom: 25px; right: 25px;
            background-color: #25d366; color: white !important;
            width: 55px; height: 55px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 28px; z-index: 9999;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
            animation: pulse-wa 2s infinite;
        }
        @keyframes pulse-wa {
            0% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
            70% { box-shadow: 0 0 0 10px rgba(37, 211, 102, 0); }
            100% { box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }
        </style>
    """, unsafe_allow_html=True)

    # --- CONTENIDO ---

    # 1. HERO SECTION
    st.markdown('<div class="hero-section">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Tu aventura de egresados empieza acá.<br>28 años de trayectoria y confianza.</p>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div style="text-align:right;"><img src="{LANDING_IMG}" class="img-hero-style"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. EXPERIENCIAS (Fondo Gris)
    st.markdown('<div class="experiences-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">Experiencias Inolvidables</h2>', unsafe_allow_html=True)
    e1, e2, e3 = st.columns(3)
    with e1:
        st.markdown('<div class="exp-card"><div class="exp-circle">🚌</div><h4>Transporte Premium</h4><p>Unidades modernas para tu seguridad.</p></div>', unsafe_allow_html=True)
    with e2:
        st.markdown('<div class="exp-card"><div class="exp-circle">🏨</div><h4>Hoteles Propios</h4><p>Alojamiento exclusivo de la empresa.</p></div>', unsafe_allow_html=True)
    with e3:
        st.markdown('<div class="exp-card"><div class="exp-circle">🛡️</div><h4>Seguridad 24/7</h4><p>Atención médica y coordinación permanente.</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 3. FOOTER
    st.markdown("""
        <div class="footer-full">
            <div class="footer-col">
                <h4>SERRANO TURISMO</h4>
                <p>Expertos en viajes estudiantiles con casi tres décadas de trayectoria impecable.</p>
            </div>
            <div class="footer-col">
                <h4>CONTACTO</h4>
                <p>📍 CABA: Av. Rivadavia 4532<br>📍 Ituzaingó: Del Cimarrón 1846<br>📞 Tel: 11-4847-6467</p>
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
