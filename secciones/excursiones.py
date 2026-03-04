import streamlit as st
import os

def render_excursiones(destino):
    # --- 1. ESTILOS CSS (Slim, Mobile & TV Frame) ---
    st.markdown("""
        <style>
        .excursion-card {
            background: #ffffff;
            border-radius: 12px;
            padding: 0px;
            border: 1px solid #e0e0e0;
            margin-bottom: 20px;
            overflow: hidden;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
        }
        .excursion-content { padding: 15px; }
        .excursion-title {
            color: #1a1c1e;
            font-size: 1.1rem;
            font-weight: 700;
            margin-bottom: 5px;
        }
        .excursion-desc {
            color: #495057;
            font-size: 0.85rem;
            line-height: 1.4;
        }
        .excursion-tag {
            display: inline-block;
            background: #e1edff;
            color: #4A90E2;
            font-size: 0.7rem;
            font-weight: 700;
            padding: 3px 10px;
            border-radius: 5px;
            margin-top: 10px;
            text-transform: uppercase;
        }
        /* ESTILO TV FRAME PARA EL VIDEO */
        .video-tv-frame {
            background: #1a1a1a;
            padding: 12px;
            border-radius: 20px;
            border: 6px solid #333;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
            margin: 20px auto;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 2. VILLA CARLOS PAZ ---
    if destino == "Villa Carlos Paz":
        if os.path.exists("assets/encabezado.jpg"):
            st.image("assets/encabezado.jpg", use_container_width=True)
        
        st.markdown("## 🏞️ Experiencias en Carlos Paz")

        # Pekos
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/pekos.jpg"):
            st.image("assets/pekos.jpg")
        st.markdown("""
            <div class="excursion-content">
                <div class="excursion-title">🚌 1. Pekos Multiparque</div>
                <div class="excursion-desc">Cine 5D, laberintos y adrenalina en un complejo recreativo único diseñado para el disfrute del grupo.</div>
                <div class="excursion-tag">Full Day • Diversión</div>
            </div>
        </div>""", unsafe_allow_html=True)

        # Aqua
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/aqua.jpg"):
            st.image("assets/aqua.jpg")
        st.markdown("""
            <div class="excursion-content">
                <div class="excursion-title">🚌 2. Wave Zone & Aquaventure</div>
                <div class="excursion-desc">Piletas de olas y toboganes gigantes para vivir un día de sol y pura acción en las sierras.</div>
                <div class="excursion-tag">Agua • Adrenalina</div>
            </div>
        </div>""", unsafe_allow_html=True)

        # Otros VCP
        st.markdown("""
            <div class="excursion-card"><div class="excursion-content">
                <div class="excursion-title">🚌 3. Crazy Donkey</div>
                <div class="excursion-desc">Aventura extrema con tirolesas y desafíos naturales.</div>
                <div class="excursion-tag">Aventura</div>
            </div></div>
            <div class="excursion-card"><div class="excursion-content">
                <div class="excursion-title">🏙️ 4. City Tour</div>
                <div class="excursion-desc">Reloj Cucú y las mejores fábricas de alfajores tradicionales.</div>
                <div class="excursion-tag">Cultura</div>
            </div></div>
        """, unsafe_allow_html=True)

    # --- 3. SAN PEDRO ---
    elif destino == "San Pedro":
        # Encabezado San Pedro
        if os.path.exists("assets/sanpedroexc.jpg"):
            st.image("assets/sanpedroexc.jpg", use_container_width=True)
        
        st.markdown("## 🏞️ Excursiones San Pedro")

        # El Fuerte (con foto sanpedroexc2.jpg)
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/sanpedroexc2.jpg"):
            st.image("assets/sanpedroexc2.jpg")
        st.markdown("""
            <div class="excursion-content">
                <div class="excursion-title">🚌 1. El Fuerte de Obligado</div>
                <div class="excursion-desc">Turismo aventura extremo: palestra, péndulo, rappel y tirolesa. Almu
