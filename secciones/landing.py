import streamlit as st

def render_landing():
    # URL de la imagen en tu GitHub
    LANDING_IMG = "https://raw.githubusercontent.com/martinszurman-ux/Serrano-Dashboard/dc30c61e09bc3c22068eb77157a6e63893dd1f63/assets/Landing_image.jpeg"

    # CSS TOTAL ACTUALIZADO
    st.markdown("""
        <style>
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
        
        /* 1. RESET ESTRUCTURAL */
        .main .block-container {
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            padding-left: 0rem !important;
            padding-right: 0rem !important;
            max-width: 100% !important;
        }

        /* 2. HERO SECTION (Subida y con margen) */
        .hero-container {
            padding: 20px 8% 40px 8%;
            background-color: white;
            display: flex;
            align-items: center;
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
        .experiences-outer {
            background-color: #d1d5db; /* Gris de la referencia */
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            padding: 80px 0; /* Espaciado interno */
            margin-top: 20px; /* Separación de la imagen de arriba */
        }
        
        .experiences-inner {
            max-width: 1200px;
            margin: 0 auto;
            text-align: center;
            padding: 0 20px;
        }

        .section-title-grey {
            font-size: 2.5rem;
            font-weight: 700;
            margin-bottom: 60px;
            color: #1a1a1a;
        }

        .exp-grid {
            display: flex;
            justify-content: center;
            gap: 40px;
            flex-wrap: wrap;
        }

        .exp-card-grey {
            flex: 1;
            min-width: 250px;
            max-width: 350px;
            text-align: center;
        }

        .exp-icon-circle {
            width: 120px;
            height: 120px;
            background: white;
            border-radius: 50%;
            margin: 0 auto 20px auto;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        }

        /* 4. FOOTER COMPACTO */
        .footer-full {
            background-color: #1a1a1a;
            color: white;
            padding: 50px 8%;
            width: 100vw;
            position: relative;
            left: 50%;
            right: 50%;
            margin-left: -50vw;
            margin-right: -50vw;
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 30px;
        }
        
        /* WHATSAPP */
        .whatsapp-btn {
            position: fixed; bottom: 25px; right: 25px;
            background-color: #25d366; color: white !important;
            width: 55px; height: 55px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 28px; z-index: 9999;
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)

    # --- CONTENIDO ---

    # 1. HERO SECTION
    st.markdown('<div class="hero-container">', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1])
    with c1:
        st.markdown('<div style="margin-top:40px;">', unsafe_allow_html=True)
        st.markdown('<h1 class="hero-title">Serrano <br>Turismo</h1>', unsafe_allow_html=True)
        st.markdown('<p class="hero-subtitle">Tu aventura de egresados empieza acá.<br>28 años de trayectoria y confianza.</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div style="text-align:right;"><img src="{LANDING_IMG}" class="img-hero-style"></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. SECCIÓN EXPERIENCIAS (Fondo Gris)
    st.markdown("""
        <div class="experiences-outer">
            <div class="experiences-inner">
                <h2 class="section-title-grey">Experiencias Inolvidables</h2>
                <div class="exp-grid">
                    <div class="exp-card-grey">
                        <div class="exp-icon-circle">🚌</div>
                        <h4>Transporte Premium</h4>
                        <p>Unidades modernas de última generación para un viaje seguro.</p>
                    </div>
                    <div class="exp-card-grey">
                        <div class="exp-icon-circle">🏨</div>
                        <h4>Hoteles Propios</h4>
                        <p>Exclusividad y seguridad en los mejores destinos del país.</p>
                    </div>
                    <div class="exp-card-grey">
                        <div class="exp-icon-circle">🛡️</div>
                        <h4>Seguridad 24/7</h4>
                        <p>Coordinación permanente y asistencia médica integral.</p>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 3. FOOTER
    st.markdown("""
        <div class="footer-full">
            <div style="flex:1; min-width:250px;">
                <h4 style="margin-bottom:15px;">SERRANO TURISMO</h4>
                <p style="color:#999; font-size:0.85rem;">Expertos en viajes estudiantiles con casi tres décadas de trayectoria.</p>
            </div>
            <div style="flex:1; min-width:250px;">
                <h4 style="margin-bottom:15px;">CONTACTO</h4>
                <p style="color:#999; font-size:0.85rem;">📍 CABA: Av. Rivadavia 4532<br>📞 11-4847-6467</p>
            </div>
            <div style="flex:1; min-width:200px;">
                <h4 style="margin-bottom:15px;">REDES SOCIALES</h4>
                <div style="display:flex; gap:15px;">
                    <a href="https://instagram.com/serrano_turismo" target="_blank" style="color:white; font-size:1.5rem;"><i class="fab fa-instagram"></i></a>
                    <a href="https://facebook.com/serranoturismo" target="_blank" style="color:white; font-size:1.5rem;"><i class="fab fa-facebook-f"></i></a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. WHATSAPP
    st.markdown('<a href="https://wa.me/5491156096283" class="whatsapp-btn" target="_blank"><i class="fab fa-whatsapp"></i></a>', unsafe_allow_html=True)
