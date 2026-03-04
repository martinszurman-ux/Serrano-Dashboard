import streamlit as st
import os

def render_excursiones(destino):
    # --- 1. ESTILOS CSS (Slim & TV Frame) ---
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
        /* MARCO DE TV QUE ENCIERRA EL VIDEO */
        .tv-container {
            background: #1a1a1a;
            padding: 15px;
            border-radius: 20px;
            border: 8px solid #333;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
            margin-bottom: 25px;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 2. VILLA CARLOS PAZ ---
    if destino == "Villa Carlos Paz":
        if os.path.exists("assets/encabezado.jpg"):
            st.image("assets/encabezado.jpg", use_container_width=True)
        
        st.markdown("## 🏞️ Experiencias en Carlos Paz")

        # Video Carlos Paz (Recuperado)
        st.markdown('<div class="tv-container">', unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=D-YV7S6Oatc") # Video institucional VCP
        st.markdown('</div>', unsafe_allow_html=True)

        # Listado Excursiones VCP
        excursiones_vcp = [
            {"img": "assets/pekos.jpg", "t": "🚌 1. Pekos Multiparque", "d": "Cine 5D, laberintos y adrenalina en un complejo recreativo único.", "tag": "Full Day"},
            {"img": "assets/aqua.jpg", "t
