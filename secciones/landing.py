import streamlit as st

def render_landing():
    # Link directo de la imagen en tu GitHub
    LANDING_IMG = "https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg"

    # CSS para diseño, redes y WhatsApp
    st.markdown("""
        <style>
        /* Importar iconos */
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');

        /* Ajuste para eliminar espacios en blanco de Streamlit */
        .main .block-container {
            padding-bottom: 0rem;
            max-width: 100%;
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
            margin: 80px 0 50px 0;
            color: #1a1a1a;
        }
        .exp-card { text-align: center; padding: 20px; }
        .exp-circle {
            width: 140px; height: 140px; background-color: #fcfcfc;
            border-radius: 50%; margin: 0 auto 25px auto;
            display: flex; align-items: center; justify-content: center;
            font-size: 3.5rem; border: 1px solid #f0f0f0;
            box-shadow: 0 10px 20px rgba(0,0,0,0.02);
        }

        /* FOOTER FULL WIDTH */
        .footer-full {
            background-color: #1a1a1a;
            color: white;
            padding: 80px 8% 60px 8%;
            margin-top: 100px;
            width: 100%;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 40px;
        }
        .footer-col { flex: 1; min-width: 280px; }
        .footer-col h4 { color: #ffffff; margin-bottom: 25px; font-size: 1.2rem; text-transform: uppercase; letter-spacing: 2px; }
        .footer-col p { color: #bbbbbb; font-size: 0.95rem; line-height: 1.8; }
        
        /* Redes Sociales */
        .social-links { display: flex; gap: 20px; margin-top: 25px; }
        .social-links a { 
            color: #ffffff; font-size: 1.8rem; transition: 0.3s; 
            text-decoration: none !important;
        }
        .social-links a:hover { color: #25d366; transform: translateY(-5px); }

        /* WHATSAPP FLOTANTE ANIMADO */
        .whatsapp-btn {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background-color: #25d366;
            color: white !important;
            width: 65px;
            height: 65px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 35px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            z-index: 9999;
            text-decoration: none !important;
            animation: pulse-wa 2s infinite;
        }
        @keyframes pulse-wa {
            0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
            70% { transform: scale(1.05); box-shadow: 0 0 0 20px rgba(37, 211, 102, 0); }
            100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }
        </style>
    """, unsafe_allow_html=True)

    # 1. HERO SECTION
    col_txt, col_img = st.columns([1.1, 1], gap="large")
    with col_txt:
        st.markdown('<div style="margin-top:100px;">', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Tu aventura de egresados empieza acá.<br>Más de 28 años acompañando a grupos escolares con seguridad y pasión.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col_img:
        st.markdown(f'<img src="{LANDING_IMG}" class="img-hero-style">', unsafe_allow_html=True)

    # 2. SECCIÓN EXPERIENCIAS
    st.markdown('<h2 class="section-title">Experiencias Inolvidables</h2>', unsafe_allow_html=True)
    e1, e2, e3 = st.columns(3)
    with e1:
        st.markdown('<div class="exp-card"><div class="exp-circle">🚌</div><h4>Transporte Premium</h4><p>Unidades de última generación con todo el confort para la ruta.</p></div>', unsafe_allow_html=True)
    with e2:
        st.markdown('<div class="exp-card"><div class="exp-circle">🏨</div><h4>Hoteles Propios</h4><p>Exclusividad y seguridad en los mejores destinos del país.</p></div>', unsafe_allow_html=True)
    with e3:
        st.markdown('<div class="exp-card"><div class="exp-circle">🛡️</div><h4>Seguridad 24/7</h4><p>Coordinación permanente y asistencia médica integral para tu tranquilidad.</p></div>', unsafe_allow_html=True)

    # 3. FOOTER
    st.markdown("""
        <div class="footer-full">
            <div class="footer-col">
                <h4>Serrano Turismo</h4>
                <p>Expertos en viajes de egresados primarios y turismo educativo. Brindamos experiencias seguras y divertidas desde hace casi tres décadas.</p>
            </div>
            <div class="footer-col">
                <h4>Contacto</h4>
                <p>📍 CABA: Av. Rivadavia 4532</p>
                <p>📍 Ituzaingó: Del Cimarrón 1846</p>
                <p>📞 Tel: 11-4847-6467</p>
            </div>
            <div class="footer-col">
                <h4>Redes Sociales</h4>
                <p>Seguí de cerca nuestras aventuras:</p>
                <div class="social-links">
                    <a href="https://instagram.com/serrano_turismo" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="https://facebook.com/serranoturismo" target="_blank"><i class="fab fa-facebook"></i></a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. WHATSAPP FLOTANTE
    # Número de Serrano Turismo: 5491156096283
    st.markdown("""
        <a href="https://wa.me/5491156096283" class="whatsapp-btn" target="_blank">
            <i class="fab fa-whatsapp"></i>
        </a>
    """, unsafe_allow_html=True)
