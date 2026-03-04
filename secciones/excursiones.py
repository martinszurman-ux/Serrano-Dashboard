import streamlit as st
import os

def render_excursiones(destino):
    # --- ESTILOS CSS (Slim, Mobile & TV Frame Real) ---
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
        /* MARCO DE TV MEJORADO */
        .tv-frame {
            background: #222;
            border: 12px solid #333;
            border-radius: 25px;
            padding: 10px;
            box-shadow: 0px 15px 35px rgba(0,0,0,0.4);
            margin: 20px auto;
        }
        </style>
    """, unsafe_allow_html=True)

    if destino == "Villa Carlos Paz":
        # (Aquí va tu bloque de VCP que ya tenías)
        st.markdown("## 🏞️ Experiencias en Carlos Paz")
        # ...

    elif destino == "San Pedro":
        # 1. ENCABEZADO (Archivo: assets/sanpedroexc.jpg)
        if os.path.exists("assets/sanpedroexc.jpg"):
            st.image("assets/sanpedroexc.jpg", use_container_width=True)
        
        st.markdown("## 🏞️ Excursiones San Pedro")

        # 1. EL FUERTE DE OBLIGADO (Archivo: assets/sanpedroexc2.jpg)
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/sanpedroexc2.jpg"):
            st.image("assets/sanpedroexc2.jpg")
        st.markdown("""
            <div class="excursion-content">
                <div class="excursion-title">🚌 1. El Fuerte de Obligado</div>
                <div class="excursion-desc">Turismo aventura extremo: palestra, péndulo, rappel y tirolesa. Además, toboganes de agua y un asado criollo a tenedor libre inolvidable.</div>
                <div class="excursion-tag">Aventura • Asado Criollo</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 2. BEACH DAY CON CANOTAJE
        st.markdown("""
            <div class="excursion-card">
                <div class="excursion-content">
                    <div class="excursion-title">🚌 2. Beach Day con Canotaje</div>
                    <div class="excursion-desc">Día de playa en balneario privado con bautismo de canotaje en sectores seguros, ideal para disfrutar el sol y el río.</div>
                    <div class="excursion-tag">Playa • Náutica</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 3. COMPLEJO LAS AMALIAS
        st.markdown("""
            <div class
