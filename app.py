import 

def render_landing():
    # URL de la imagen en tu GitHub
    LANDING_IMG = "https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg"

    # 1. CSS ESTÁTICO (Sin cálculos de ancho de pantalla para evitar errores)
    st.markdown("""
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        
        /* Ajuste de márgenes de Streamlit */
        .main .block-container {
            padding-top: 0px !important;
            padding-bottom: 0px !important;
            max-width: 100% !important;
        }

        /* Hero */
        .hero-container {
            padding: 0 5% 20px 5%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .hero-title {
            font-size: 3.5rem !important;
            font-weight: 800;
            line-height: 1;
            margin: 0;
        }

        /* Sección Experiencias con fondo gris */
        .grey-box {
            background-color: #d1d5db !important; /* El gris de tu referencia */
            padding: 40px 5%;
            margin: 20px 0;
            text-align: center;
            width: 100%;
        }

        /* Footer Compacto */
        .footer-box {
            background-color: #1a1a1a;
            color: white;
            padding: 30px 5%;
            width: 100%;
        }

        /* WhatsApp */
        .wa-float {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #25d366;
            color: white !important;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 25px;
            z-index: 1000;
            text-decoration: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. HERO SECTION
    # Usamos columnas nativas de Streamlit pero con nuestro CSS
    col1, col2 = st.columns([1, 1])
    with col1:
        st.markdown('<div style="padding-left: 10%; padding-top: 20px;">', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        st.markdown('<p style="font-size: 1.2rem; color: #555;">Tu aventura de egresados empieza acá.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div style="text-align: right; padding-right: 10%;"><img src="{LANDING_IMG}" style="width: 100%; max-width: 400px; border-radius: 20px;"></div>', unsafe_allow_html=True)

    # 3. SECCIÓN EXPERIENCIAS (FONDO GRIS)
    st.markdown('<div class="grey-box">', unsafe_allow_html=True)
    st.markdown('<h2 style="font-weight: 700; margin-bottom: 30px;">Experiencias Inolvidables</h2>', unsafe_allow_html=True)
    
    # Columnas para los iconos
    ex1, ex2, ex3 = st.columns(3)
    with ex1:
        st.markdown('<div style="background: white; border-radius: 50%; width: 80px; height: 80px; margin: 0 auto; display: flex; align-items: center; justify-content: center; font-size: 2rem;">🚌</div>', unsafe_allow_html=True)
        st.markdown('<strong>Transporte Premium</strong>', unsafe_allow_html=True)
    with ex2:
        st.markdown('<div style="background: white; border-radius: 50%; width: 80px; height: 80px; margin: 0 auto; display: flex; align-items: center; justify-content: center; font-size: 2rem;">🏨</div>', unsafe_allow_html=True)
        st.markdown('<strong>Hoteles Propios</strong>', unsafe_allow_html=True)
    with ex3:
        st.markdown('<div style="background: white; border-radius: 50%; width: 80px; height: 80px; margin: 0 auto; display: flex; align-items: center; justify-content: center; font-size: 2rem;">🛡️</div>', unsafe_allow_html=True)
        st.markdown('<strong>Seguridad 24/7</strong>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 4. FOOTER
    st.markdown("""
        <div class="footer-box">
            <div style="display: flex; justify-content: space-between; flex-wrap: wrap;">
                <div>
                    <h4 style="margin-bottom: 10px;">SERRANO TURISMO</h4>
                    <p style="font-size: 0.8rem; color: #999;">28 años de trayectoria impecable.</p>
                </div>
                <div>
                    <h4 style="margin-bottom: 10px;">CONTACTO</h4>
                    <p style="font-size: 0.8rem; color: #999;">📍 Av. Rivadavia 4532 | 📞 11-4847-6467</p>
                </div>
                <div>
                    <h4 style="margin-bottom: 10px;">SÍGUENOS</h4>
                    <a href="#" style="color: white; margin-right: 10px;"><i class="fab fa-instagram"></i></a>
                    <a href="#" style="color: white;"><i class="fab fa-facebook"></i></a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 5. WHATSAPP
    st.markdown('<a href="https://wa.me/5491156096283" class="wa-float" target="_blank"><i class="fab fa-whatsapp"></i></a>', unsafe_allow_html=True)

