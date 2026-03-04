import streamlit as st
from utilidades.footer import render_footer

def render_landing():
    # URL de la imagen en tu GitHub
    LANDING_IMG = "https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg"

    # CSS TOTAL - AJUSTE DE ALTURA Y TEXTO
    st.markdown("""
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        
        /* 1. RESET ESTRUCTURAL - SUBIDA MÁXIMA CONTROLADA */
        header {visibility: hidden; height: 0px;}
        footer {display: none !important;}
        
        .main .block-container {
            padding-top: 0.1rem !important; /* Casi nada de espacio arriba */
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }

        /* Subir el bloque del Hero sin que se esconda bajo el navegador */
        [data-testid="stVerticalBlock"] > div:first-child {
            margin-top: -30px !important; 
        }

        /* 2. HERO SECTION */
        .hero-container {
            padding: 0px 8% 10px 8%; 
            background-color: white;
        }
        .hero-title {
            font-size: 4.2rem !important;
            font-weight: 800;
            color: #1a1a1a;
            line-height: 1;
            margin-bottom: 20px;
        }
        .hero-subtitle {
            font-size: 1.2rem;
            color: #444;
            line-height: 1.6;
            text-align: justify;
        }
        .img-hero-style {
            width: 100%;
            max-width: 500px;
            border-radius: 20px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        }

        /* 3. SECCIÓN EXPERIENCIAS (Gris Full Width) */
        .experiences-outer {
            background-color: #d1d5db;
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            padding: 70px 0;
        }
        
        .experiences-inner {
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
            padding: 0 20px;
        }

        /* 4. SPACERS SIMÉTRICOS BLANCOS */
        .simetric-spacer {
            background-color: white;
            height: 80px; 
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
        }

        /* 5. FOOTER FINAL NEGRO */
        .footer-full {
            background-color: #1a1a1a;
            color: white;
            padding: 60px 8% 80px 8%;
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
            margin-bottom: -100px !important;
        }

        /* 6. WHATSAPP IZQUIERDA CON PULSO */
        .whatsapp-btn {
            position: fixed; 
            bottom: 30px; 
            left: 30px; 
            background-color: #25d366; 
            color: white !important;
            width: 60px; 
            height: 60px; 
            border-radius: 50%;
            display: flex; 
            align-items: center; 
            justify-content: center;
            font-size: 32px; 
            z-index: 9999;
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
            text-decoration: none !important;
            animation: pulse-green 2s infinite;
        }

        @keyframes pulse-green {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0.7); }
            70% { transform: scale(1.05); box-shadow: 0 0 0 20px rgba(37, 211, 102, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(37, 211, 102, 0); }
        }
        </style>
    """, unsafe_allow_html=True)

    # --- CONTENIDO ---

    # 1. HERO SECTION
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    c1, c2 = st.columns([1.2, 0.8], gap="large")
    with c1:
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        # TEXTO ACTUALIZADO
        st.markdown("""
            <p class="hero-subtitle">
                Tu aventura de egresados empieza acá.<br>
                Más de 100.000 egresados de Buenos Aires ya confiaron en nosotros.<br>
                Con 29 años de experiencia, Serrano Turismo es sinónimo de transparencia y cumplimiento,<br>
                transformando cada viaje en una experiencia inolvidable con la seriedad que tu familia busca.
            </p>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div style="text-align:right;"><img src="{LANDING_IMG}" class="img-hero-style"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. SPACER ANTES
    st.markdown('<div class="simetric-spacer"></div>', unsafe_allow_html=True)

    # 3. SECCIÓN EXPERIENCIAS (FONDO GRIS)
    st.markdown("""
        <div class="experiences-outer">
            <div class="experiences-inner">
                <h2 style="font-size:2.8rem; font-weight:700; margin-bottom:60px; color:#1a1a1a;">Experiencias Inolvidables</h2>
                <div style="display: flex; justify-content: center; gap: 50px; flex-wrap: wrap;">
                    <div style="flex:1; min-width:280px; text-align:center;">
                        <div style="width:115px; height:115px; background:white; border-radius:50%; margin:0 auto 25px; display:flex; align-items:center; justify-content:center; font-size:3rem; box-shadow:0 8px 20px rgba(0,0,0,0.06);">🚌</div>
                        <h4 style="font-weight:800; font-size:1.3rem;">Transporte Premium</h4>
                        <p style="color:#4b5563; line-height:1.5;">Unidades modernas de última generación con todo el confort para la ruta.</p>
                    </div>
                    <div style="flex:1; min-width:280px; text-align:center;">
                        <div style="width:115px; height:115px; background:white; border-radius:50%; margin:0 auto 25px; display:flex; align-items:center; justify-content:center; font-size:3rem; box-shadow:0 8px 20px rgba(0,0,0,0.06);">🏨</div>
                        <h4 style="font-weight:800; font-size:1.3rem;">Hoteles Propios</h4>
                        <p style="color:#4b5563; line-height:1.5;">Exclusividad y seguridad en los mejores destinos del país.</p>
                    </div>
                    <div style="flex:1; min-width:280px; text-align:center;">
                        <div style="width:115px; height:115px; background:white; border-radius:50%; margin:0 auto 25px; display:flex; align-items:center; justify-content:center; font-size:3rem; box-shadow:0 8px 20px rgba(0,0,0,0.06);">🛡️</div>
                        <h4 style="font-weight:800; font-size:1.3rem;">Seguridad 24/7</h4>
                        <p style="color:#4b5563; line-height:1.5;">Coordinación permanente y asistencia médica integral para tu tranquilidad.</p>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. SPACER DESPUÉS
    st.markdown('<div class="simetric-spacer"></div>', unsafe_allow_html=True)

  # --- 5. FOOTER INSTITUCIONAL ---
    # Invocamos la función del archivo utilidades/footer.py
    render_footer()
