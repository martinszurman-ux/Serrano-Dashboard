import streamlit as st
import os

def render_excursiones(destino):
    # --- ESTILOS CSS (Slim & Mobile Ready) ---
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
        .video-container {
            margin-bottom: 25px;
            border-radius: 12px;
            overflow: hidden;
        }
        </style>
    """, unsafe_allow_html=True)

    if destino == "Villa Carlos Paz":
        # (Aquí va tu código actual de Carlos Paz que ya funciona perfecto)
        st.markdown("## 🏞️ Experiencias en Carlos Paz")
        # ... resto del código de VCP ...

    elif destino == "San Pedro":
        # 1. ENCABEZADO (Foto nueva encabezado_sp.jpg)
        if os.path.exists("assets/encabezado_sp.jpg"):
            st.image("assets/encabezado_sp.jpg", use_container_width=True)
        
        # 2. VIDEO INSTITUCIONAL
        st.markdown('<div class="video-container">', unsafe_allow_html=True)
        st.video("https://www.youtube.
