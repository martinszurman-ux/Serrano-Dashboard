import streamlit as st

def render_landing():
    # Link directo de la imagen
    LANDING_IMG = "https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg"

    # CSS
    st.markdown("""
        <style>
        .hero-title {
            font-size: 4.2rem !important;
            font-weight: 800;
            color: #1a1a1a;
            line-height: 1;
            margin-bottom: 15px;
        }
        .hero-subtitle {
            font-size: 1.3rem;
            color: #555;
            margin-bottom: 35px;
        }
        .img-hero-style {
            width: 100%;
            max-width: 500px;
            border-radius: 25px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }
        .section-title {
            text-align: center;
            font-size: 2.2rem;
            font-weight: 700;
            margin: 60px 0 40px 0;
            color: #1a1a1a;
        }
        .exp-card { text-align: center; padding: 15px; }
        .exp-circle {
            width: 120px; height: 120px; background-color: #f8f9fa;
            border-radius: 50%; margin: 0 auto 20px auto;
            display: flex; align-items: center; justify-content: center;
            font-size: 2.5rem; border: 1px solid #eee;
        }
        .footer-container {
            background-color: #1a1a1a; color: white;
            padding: 50px 5%; margin-top: 80px;
            display: flex; justify-content: space-around; flex-wrap: wrap;
        }
        .footer-col { flex: 1; min-width: 200px; padding: 10px; }
        </style>
    """, unsafe_allow_html=True)

    # 1. HERO SECTION
    col_text, col_img = st.columns([1, 1], gap="large")

    with col_text:
        st.markdown('<div style="margin-top:60px;">', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Tu aventura de egresados empieza acá.<br>Experiencias diseñadas para los más chicos.</p>', unsafe_allow_html=True)
        # AQUÍ ANTES ESTABAN LOS BOTONES. AHORA NO HAY NADA.
        st.markdown('</div>', unsafe_allow_html=True)

    with col_img:
        st.markdown(f'<img src="{LANDING_IMG}" class="img-hero-style">', unsafe_allow_html=True)

    # 2. EXPERIENCIAS
    st.markdown('<h2 class="section-title">Experiencias Inolvidables</h2>', unsafe_allow_html=True)
    e1, e2, e3 = st.columns(3)
    with e1:
        st.markdown('<div class="exp-card"><div class="exp-circle">🚌</div><h4>Transporte Premium</h4><p>Unidades modernas.</p></div>', unsafe_allow_html=True)
    with e2:
        st.markdown('<div class="exp-card"><div class="exp-circle">🏨</div><h4>Hoteles Propios</h4><p>Servicio exclusivo.</p></div>', unsafe_allow_html=True)
    with e3:
        st.markdown('<div class="exp-card"><div class="exp-circle">🏞️</div><h4>Excursiones</h4><p>Diversión total.</p></div>', unsafe_allow_html=True)

    # 3. FOOTER
    st.markdown("""
        <div class="footer-container">
            <div class="footer-col"><h4>SERRANO TURISMO</h4><p>Más de 28 años de trayectoria.</p></div>
            <div class="footer-col"><h4>CONTACTO</h4><p>📍 Rivadavia 4532 - CABA</p></div>
            <div class="footer-col"><h4>INFO</h4><p>Agencia habilitada por el Ministerio de Turismo.</p></div>
        </div>
    """, unsafe_allow_html=True)
