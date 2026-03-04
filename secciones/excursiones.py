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
        .tv-frame {
            background: #222;
            border: 10px solid #333;
            border-radius: 20px;
            padding: 10px;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
            margin: 20px auto;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 2. LÓGICA VILLA CARLOS PAZ ---
    if destino == "Villa Carlos Paz":
        if os.path.exists("assets/encabezado.jpg"):
            st.image("assets/encabezado.jpg", use_container_width=True)
        
        st.markdown("## 🏞️ Experiencias en Carlos Paz")

        # 1. Pekos
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/pekos.jpg"):
            st.image("assets/pekos.jpg")
        st.markdown("""
            <div class="excursion-content">
