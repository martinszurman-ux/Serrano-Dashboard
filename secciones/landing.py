import streamlit as st

def render_landing():
    # Link directo (Raw) de tu imagen en GitHub
    LANDING_IMG = "https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg"

    # CSS específico para la Landing (Hero, Experiencias y Footer)
    st.markdown("""
        <style>
        /* HERO SECTION */
        .hero-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 40px;
            padding: 40px 0;
        }
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

        /* SECCIÓN EXPERIENCIAS */
        .section-title {
            text-align: center;
            font-size: 2.2rem;
            font-weight: 700;
            margin: 60px 0 40px 0;
            color: #1a1a1a;
        }
        .exp-card {
            text-align: center;
            padding: 15px;
        }
        .exp-circle {
            width: 150px;
            height: 150px;
            background-color: #f8f9fa;
            border-radius: 50%;
            margin: 0 auto 20px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 2.5rem;
            border: 1px solid #eee;
            box-shadow: 0 5px 15px rgba(0,0,0,0.03);
        }

        /* FOOTER */
        .footer-container {
            background-color: #1a1a1a;
            color: white;
            padding: 50px 5%;
            margin-top: 80px;
            margin-left: -10%;
            margin-right: -10%;
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
        }
        .footer-col { flex: 1; min-width: 200px; padding: 10px; }
        .footer-col h4 { color: #fff; margin-bottom: 15px; font-size: 1rem; letter-spacing: 1px; }
        .footer-col p { color: #aaa; font-size: 0.85rem; line-height: 1.6; }
        </style>
    """, unsafe_allow_html=True)

    # 1. HERO SECTION (Título e Imagen)
    col_text, col_img = st.columns([1, 1], gap="large")

    with col_text:
        st.markdown('<div style="margin-top:30px;">', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Tu aventura de egresados empieza acá.<br>Elegí tu destino para conocer más:</p>', unsafe_allow_html=True)
        
        # Botones de Acción: Actualizan Session State y Rerunean la App
        btn_col1, btn_col2, _ = st.columns([1, 1, 0.5])
        with btn_col1:
            if st.button("📍 Carlos Paz", use_container_width=True, key="btn_cp"):
                st.session_state.destino = "Villa Carlos Paz"
                st.session_state.nav = "Transporte"
                st.rerun()
        with btn_col2:
            if st.button("📍 San Pedro", use_container_width=True, key="btn_sp"):
                st.session_state.destino = "San Pedro"
                st.session_state.nav = "Transporte"
                st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    with col_img:
        st.markdown(f'<img src="{LANDING_IMG}" class="img-hero-style">', unsafe_allow_html=True)

    # 2. SECCIÓN EXPERIENCIAS (Burbujas del Wireframe)
    st.markdown('<h2 class="section-title">Experiencias Inolvidables</h2>', unsafe_allow_html=True)
    
    e1, e2, e3 = st.columns(3)
    with e1:
        st.markdown("""<div class="exp-card">
            <div class="exp-circle">🚌</div>
            <h4>Transporte Premium</h4>
            <p>Unidades modernas con el máximo confort para un viaje seguro.</p>
        </div>""", unsafe_allow_html=True)
    with e2:
        st.markdown("""<div class="exp-card">
            <div class="exp-circle">🏨</div>
            <h4>Hoteles Propios</h4>
            <p>Alojamiento exclusivo con servicios pensados para egresados.</p>
        </div>""", unsafe_allow_html=True)
    with e3:
        st.markdown("""<div class="exp-card">
            <div class="exp-circle">🏞️</div>
            <h4>Full Excursiones</h4>
            <p>Cronograma completo de actividades para no parar ni un segundo.</p>
        </div>""", unsafe_allow_html=True)

    # 3. FOOTER INSTITUCIONAL
    st.markdown("""
        <div class="footer-container">
            <div class="footer-col">
                <h4>SERRANO TURISMO</h4>
                <p>Expertos en viajes estudiantiles con más de 20 años de trayectoria impecable.</p>
            </div>
            <div class="footer-col">
                <h4>CONTACTO</h4>
                <p>📍 Rivadavia 4532 - CABA</p>
                <p>📍 Del Cimarrón 1846 - Ituzaingo</p>
                <p>📞 11-4847-6467</p>
            </div>
            <div class="footer-col">
                <h4>NOSOTROS</h4>
                <p>Legajo N° 12345<br>Agencia habilitada por el Ministerio de Turismo y Deportes.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
