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
        st.video("https://www.youtube.com/watch?v=xBDqSrNB8Ro")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("## 🏞️ Excursiones San Pedro")

        # 1. EL FUERTE DE OBLIGADO (Con foto fuerte.jpg)
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/fuerte.jpg"):
            st.image("assets/fuerte.jpg")
        st.markdown("""
            <div class="excursion-content">
                <div class="excursion-title">🚌 1. El Fuerte de Obligado</div>
                <div class="excursion-desc">Turismo aventura en estado puro: palestra, péndulo, rappel y tirolesa. Además, disfrutamos de toboganes de agua y un auténtico asado criollo a tenedor libre.</div>
                <div class="excursion-tag">Aventura • Gastronomía</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 2. BEACH DAY CON CANOTAJE
        st.markdown("""
            <div class="excursion-card">
                <div class="excursion-content">
                    <div class="excursion-title">🚌 2. Beach Day con Canotaje</div>
                    <div class="excursion-desc">Día de playa exclusivo en balneario privado con actividades deportivas. Incluye bautismo de canotaje en sectores seguros y controlados.</div>
                    <div class="excursion-tag">Playa • Náutica</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 3. COMPLEJO LAS AMALIAS
        st.markdown("""
            <div class="excursion-card">
                <div class="excursion-content">
                    <div class="excursion-title">🚌 3. Complejo Las Amalias</div>
                    <div class="excursion-desc">Tarde de recreación total: laberinto de ligustrinas, plaza húmeda, pileta, fútbol y vóley en un predio diseñado para el grupo.</div>
                    <div class="excursion-tag">Recreación • Aire Libre</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 4. SUNSET CATAMARÁN
        st.markdown("""
            <div class="excursion-card">
                <div class="excursion-content">
                    <div class="excursion-title">🚢 4. Sunset Catamarán</div>
                    <div class="excursion-desc">Navegación exclusiva por el Río Paraná. Disfrutamos del atardecer con la mejor música a bordo de un catamarán de primer nivel.</div>
                    <div class="excursion-tag">Navegación • Fiesta</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 5. CITY TOUR
        st.markdown("""
            <div class="excursion-card">
                <div class="excursion-content">
                    <div class="excursion-title">🏙️ 5. City Tour</div>
                    <div class="excursion-desc">Recorrido histórico por la ciudad, zona de barrancas y el Vía Crucis. Finalizamos con tiempo para compras de artículos regionales.</div>
                    <div class="excursion-tag">Cultura • Regional</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
