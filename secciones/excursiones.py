import streamlit as st
import os

def render_excursiones(destino):
    # --- ESTILOS CSS (Slim, Mobile & TV Frame) ---
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
            padding: 15px;
            border-radius: 25px;
            border: 8px solid #333;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
            margin: 20px auto;
            max-width: 800px;
        }
        </style>
    """, unsafe_allow_html=True)

    if destino == "Villa Carlos Paz":
        # Mantenemos tu código de Carlos Paz aquí...
        st.markdown("## 🏞️ Experiencias en Carlos Paz")
        # (Resto del código de VCP)

    elif destino == "San Pedro":
        # 1. ENCABEZADO (Archivo: assets/sanpedroexc.jpg)
        if os.path.exists("assets/sanpedroexc.jpg"):
            st.image("assets/sanpedroexc.jpg", use_container_width=True)
        
        st.markdown("## 🏞️ Excursiones San Pedro")

        # 2. EL FUERTE DE OBLIGADO (Archivo: assets/2.jpg)
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/2.jpg"):
            st.image("assets/2.jpg")
        st.markdown("""
            <div class="excursion-content">
                <div class="excursion-title">🚌 1. El Fuerte de Obligado</div>
                <div class="excursion-desc">Turismo aventura extremo: palestra, péndulo, rappel y tirolesa. Además, toboganes de agua y un asado criollo a tenedor libre inolvidable.</div>
                <div class="excursion-tag">Aventura • Asado Criollo</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 3. BEACH DAY CON CANOTAJE
        st.markdown("""
            <div class="excursion-card">
                <div class="excursion-content">
                    <div class="excursion-title">🚌 2. Beach Day con Canotaje</div>
                    <div class="excursion-desc">Día de playa en balneario privado con bautismo de canotaje en sectores seguros, ideal para disfrutar el sol y el río.</div>
                    <div class="excursion-tag">Playa • Náutica</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 4. COMPLEJO LAS AMALIAS
        st.markdown("""
            <div class="excursion-card">
                <div class="excursion-content">
                    <div class="excursion-title">🚌 3. Complejo Las Amalias</div>
                    <div class="excursion-desc">Laberinto de ligustrinas, plaza húmeda, piletas y deportes. Un predio gigante para la recreación del grupo.</div>
                    <div class="excursion-tag">Recreación • Aire Libre</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 5. SUNSET CATAMARÁN
        st.markdown("""
            <div class="excursion-card">
                <div class="excursion-content">
                    <div class="excursion-title">🚢 4. Sunset Catamarán</div>
                    <div class="excursion-desc">Navegación por el Paraná al atardecer con música exclusiva. Una experiencia mágica para cerrar el día.</div>
                    <div class="excursion-tag">Navegación • Música</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 6. CITY TOUR
        st.markdown("""
            <div class="excursion-card">
                <div class="excursion-content">
                    <div class="excursion-title">🏙️ 5. City Tour</div>
                    <div class="excursion-desc">Recorrido por barrancas, Vía Crucis y centros históricos, con tiempo para compras de productos regionales.</div>
                    <div class="excursion-tag">Cultura • Regalos</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 7. VIDEO INSTITUCIONAL AL FINAL (Con Marco de TV)
        st.markdown("---")
        st.markdown("### 🎥 Mirá cómo vivimos San Pedro")
        st.markdown('<div class="video-tv-frame">', unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=xBDqSrNB8Ro")
        st.markdown('</div>', unsafe_allow_html=True)
