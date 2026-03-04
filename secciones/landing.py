import streamlit as st

def render_landing():
    # URL de la imagen en tu GitHub
    LANDING_IMG = "https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg"

    # CSS TOTAL: Control de Layout, Hero, Experiencias, Footer Full Width y WhatsApp
    st.markdown("""
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        
        /* 1. ELIMINAR ESPACIO BLANCO INFERIOR Y LATERAL */
        .main .block-container {
            padding-top: 2rem !important;
            padding-bottom: 0px !important; /* Elimina el espacio abajo */
            padding-left: 0px !important;
            padding-right: 0px !important;
            max-width: 100% !important;
        }

        /* Forzar que el último bloque no tenga margen inferior */
        [data-testid="stVerticalBlock"] {
            gap: 0px !important;
        }

        /* Contenedor para elementos con margen (Hero y Experiencias) */
        .content-wrapper {
            padding: 0 7%;
        }

        /* HERO SECTION */
        .hero-title {
            font-size: 4.5rem !important;
            font-weight: 800;
            color: #1a1a1a;
            line-height: 1.1;
            margin-bottom: 20px;
        }
        .hero-subtitle {
            font-size: 1.4rem;
            color: #444;
            margin-bottom: 40px;
        }
        .img-hero-style {
            width: 100%;
            max-width: 550px;
            border-radius: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.15);
        }

        /* SECCIÓN EXPERIENCIAS */
        .section-title {
            text-align: center;
            font-size: 2.8rem;
            font-weight: 700;
            margin: 60px 0 40px 0;
            color: #1a1a1a;
        }
        .exp-card { text-align: center; padding: 20px; }
        .exp-circle {
            width: 120px; height: 120px; background-color: #f8f9fa;
            border-radius: 50%; margin: 0 auto 20px auto;
            display: flex; align-items: center; justify-content: center;
            font-size: 3rem; border: 1px solid #eee;
        }

        /* FOOTER FULL WIDTH SIN ESPACIO ABAJO */
        .footer-full {
            background-color: #1a1a1a;
            color: white;
            padding: 80px 8% 60px 8%;
            margin-top: 80px;
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 40px;
            margin-bottom: -100px; /* Truco para "comerse" el espacio extra de Streamlit */
            padding-bottom: 120px; /* Compensa el margen negativo */
        }
        
        .footer-col { flex: 1; min-width: 280px; }
        .footer-col h4 { color: white; margin-bottom: 25px; font-size: 1.1rem; letter-spacing: 1px; font-weight: 700; }
        .footer-col p { color: #aaa; font-size: 0.9rem; line-height: 1.7; }
        
        .social-icons-container { display: flex; gap: 20px; margin-top: 15px; }
        .social-icons-container a { color: white; font-size: 1.6rem; transition: 0.3s; text-decoration: none; }
        .social-icons-container a:hover { color: #25d366; transform: scale(1.2); }

        /* WHATSAPP */
        .whatsapp-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background-color: #25d366;
            color: white !important;
            width: 60px;
            height: 60px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            z-index: 9999;
            text-decoration: none !important;
            animation: pulse-wa 2s infinite;
        }
        @keyframes pulse-wa {
            0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
            70% { transform: scale(1.05); box-shadow: 0 0 0 15px rgba(37, 211, 102, 0); }
            100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }
        </style>
    """, unsafe_allow_html=True)

    # 1. HERO SECTION
    st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)
    col_txt, col_img = st.columns([1.1, 1], gap="large")
    with col_txt:
        st.markdown('<div style="margin-top:80px;">', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Tu aventura de egresados empieza acá.<br>28 años brindando servicio de excelencia en viajes de egresados y educativos.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_img:
        st.markdown(f'<img src="{LANDING_IMG}" class="img-hero-style">', unsafe_allow_html=True)

    # 2. SECCIÓN EXPERIENCIAS
    st.markdown('<h2 class="section-title">Experiencias Inolvidables</h2>', unsafe_allow_html=True)
    e1, e2, e3 = st.columns(3)
    with e1:
        st.markdown('<div class="exp-card"><div class="exp-circle">🚌</div><h4>Transporte Premium</h4><p>Unidades modernas para un viaje seguro.</p></div>', unsafe_allow_html=True)
    with e2:
        st.markdown('<div class="exp-card"><div class="exp-circle">🏨</div><h4>Hoteles Propios</h4><p>Exclusividad pensada para egresados.</p></div>', unsafe_allow_html=True)
    with e3:
        st.markdown('<div class="exp-card"><div class="exp-circle">🛡️</div><h4>Seguridad 24/7</h4><p>Atención médica y coordinación permanente.</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True) 

    # 3. FOOTER (Con truco de margen negativo para eliminar el blanco inferior)
    st.markdown("""
        <div class="footer-full">
            <div class="footer-col">
                <h4>SERRANO TURISMO</h4>
                <p>Expertos en viajes estudiantiles con más de 28 años de trayectoria impecable. Garantizamos seguridad y diversión.</p>
            </div>
            <div class="footer-col">
                <h4>CONTACTO</h4>
                <p>📍 CABA: Av. Rivadavia 4532</p>
                <p>📍 Ituzaingó: Del Cimarrón 1846</p>
                <p>📞 Tel: 11-4847-6467</p>
            </div>
            <div class="footer-col">
                <h4>REDES SOCIALES</h4>
                <div class="social-icons-container">
                    <a href="https://www.instagram.com/serrano_turismo/" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="https://www.facebook.com/serranoturismo/" target="_blank"><i class="fab fa-facebook-f"></i></a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. BOTÓN WHATSAPP
    st.markdown("""
        <a href="https://wa.me/5491156096283" class="whatsapp-btn" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    """, unsafe_allow_html=True)
