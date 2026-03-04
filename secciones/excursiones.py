import streamlit st
import os

def render_excursiones(destino):
    # --- ESTILOS CSS ---
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
        .video-tv-frame {
            background: #1a1a1a;
            padding: 10px;
            border-radius: 20px;
            border: 6px solid #333;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
            margin: 20px auto;
        }
        </style>
    """, unsafe_allow_html=True)

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
                <div class="excursion-desc">Cine 5D, laberintos y adrenalina en un complejo recreativo único.</div>
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
                <div class="excursion-desc">Piletas de olas y toboganes gigantes para vivir un día de sol.</div>
                <div class="excursion-tag">Agua • Adrenalina</div>
            </div>
        </div>""", unsafe_allow_html=True)

    elif destino == "San Pedro":
        # 1. ENCABEZADO (Archivo: assets/sanpedroexc.jpg)
        if os.path.exists("assets/sanpedroexc.jpg"):
            st.image("assets/sanpedroexc.jpg", use_container_width=True)
        
        st.markdown("## 🏞️ Excursiones San Pedro")

        # 2. EL FUERTE DE OBLIGADO (Archivo: assets/sanpedroexc2.jpg)
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/sanpedroexc2.jpg"):
            st.image("assets/sanpedro
