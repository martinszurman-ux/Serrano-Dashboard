import streamlit as st

def render_landing():
    # LINK RAW QUE PASASTE
    LANDING_IMG = "https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg"

    st.markdown("""
        <style>
        /* --- SECCIÓN HERO --- */
        .hero-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 40px;
            padding: 60px 0;
        }
        .hero-title {
            font-size: 4.8rem !important;
            font-weight: 800;
            color: #1a1a1a;
            line-height: 0.9;
            margin-bottom: 15px;
        }
        .hero-subtitle {
            font-size: 1.4rem;
            color: #555;
            margin-bottom: 35px;
        }
        .img-hero-style {
            width: 100%;
            max-width: 520px;
            border-radius: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }

        /* --- SECCIÓN EXPERIENCIAS (Burbujas) --- */
        .section-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: 700;
            margin: 80px 0 50px 0;
            color: #1a1a1a;
        }
        .exp-card {
            text-align: center;
            padding: 20px;
        }
        .exp-circle {
            width: 180px;
            height: 180px;
            background-color: #f0f2f6;
            border-radius: 50%;
            margin: 0 auto 20px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            box-shadow: 0 10px 20px rgba(0,0,0,0.05);
            border: 2px solid #eeeeee;
        }
        .exp-card h3 { font-size: 1.3rem; margin-bottom: 10px; }
        .exp-card p { font-size: 0.95rem; color: #666; }

        /* --- FOOTER --- */
        .footer-full {
            background-color: #1a1a1a;
            color: white;
            padding: 60px 5% 30px 5%;
            margin-top: 100px;
            margin-left: -10%; /* Para romper el padding del contenedor de streamlit */
            margin-right: -10%;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
        }
        .footer-col { flex: 1; min-width: 250px; margin-bottom: 30px; }
        .footer-col h4 { color: #ffffff; margin-bottom: 20px; font-size: 1.1rem; }
        .footer-col p { color: #bbb; font-size: 0.9rem; margin-bottom: 10px; }
        </style>
    """, unsafe_allow_html=True)

    # 1. HERO SECTION
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    col_text, col_img = st.columns([1, 1], gap="large")

    with col_text:
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Tu aventura de egresados empieza acá.<br>Elegí tu destino para conocer más:</p>', unsafe_allow_html=True)
        
        c1, c2, _ = st.columns([1, 1, 0.5])
        with c1:
            if st.button("📍 Carlos Paz", use_container_width=True):
                st.query_params["destino"] = "Villa Carlos Paz"
                st.rerun()
        with c2:
            if st.button("📍 San Pedro", use_container_width=True):
                st.query_params["destino"] = "San Pedro"
                st.rerun()

    with col_img:
        st.markdown(f'<img src="{LANDING_IMG}" class="img-hero-style">', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. SECCIÓN EXPERIENCIAS
    st.markdown('<h2 class="section-title">Experiencias Inolvidables</h2>', unsafe_allow_html=True)
    
    e1, e2, e3 = st.columns(3)
    with e1:
        st.markdown("""<div class="exp-card">
            <div class="exp-circle">🚌</div>
            <h3>Transporte de Primera</h3>
            <p>Unidades de última generación con el máximo confort y seguridad para el grupo.</p>
        </div>""", unsafe_allow_html=True)
    with e2:
        st.markdown("""<div class="exp-card">
            <div class="exp-circle">🏨</div>
            <h3>Hoteles Exclusivos</h3>
            <p>Alojamiento en hoteles seleccionados con todas las comodidades y régimen de comidas.</p>
        </div>""", unsafe_allow_html=True)
    with e3:
        st.markdown("""<div class="exp-card">
            <div class="exp-circle">🏞️</div>
            <h3>Excursiones Únicas</h3>
            <p>Actividades diseñadas para que cada momento del viaje sea una aventura nueva.</p>
        </div>""", unsafe_allow_html=True)

    # 3. FOOTER
    st.markdown(f"""
        <div class="footer-full">
            <div class="footer-col">
                <h4>SERRANO TURISMO</h4>
                <p>Más de 20 años acompañando a grupos estudiantiles a cumplir sus sueños.</p>
            </div>
            <div class="footer-item" style="flex:1;">
                <h4>CONTACTO</h4>
                <p>📍 Av. Rivadavia 4532 - Gal. Alefa (L. 10)</p>
                <p>📍 Del Cimarrón 1846 - Ituzaingo</p>
                <p>📞 11 - 4847-6467</p>
            </div>
            <div class="footer-col">
                <h4>LEGAL</h4>
                <p>Legajo N° 12345</p>
                <p>Agencia autorizada por el Ministerio de Turismo.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
