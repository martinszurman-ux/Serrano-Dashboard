import streamlit as st
import os

def render_excursiones(destino):
    if destino == "Villa Carlos Paz":
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
                font-size: 1.15rem;
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
            </style>
        """, unsafe_allow_html=True)

    # 1. ENCABEZADO (Archivo: encabezado.jpg)
    # Probamos con .jpg y .png por las dudas
    if os.path.exists("assets/encabezado.jpg"):
        st.image("assets/encabezado.jpg", caption="¡Viví la experiencia Serrano!")
    elif os.path.exists("assets/encabezado.png"):
        st.image("assets/encabezado.png")

    st.markdown("## 🏞️ Experiencias en Carlos Paz")

    # 2. PEKOS (Archivo: pekos.jpg)
    st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
    if os.path.exists("assets/pekos.jpg"):
        st.image("assets/pekos.jpg")
    elif os.path.exists("assets/pekos.png"):
        st.image("assets/pekos.png")
    st.markdown("""
        <div class="excursion-content">
            <div class="excursion-title">🚌 1. Pekos Multiparque</div>
            <div class="excursion-desc">Un mundo de sensaciones con shows de lobos marinos, cine 5D, laberintos y adrenalina. Un clásico de Serrano Turismo para disfrutar al máximo.</div>
            <div class="excursion-tag">Full Day • Entretenimiento</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 3. WAVE ZONE & AQUAVENTURE (Archivo: aqua.jpg)
    st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
    if os.path.exists("assets/aqua.jpg"):
        st.image("assets/aqua.jpg")
    elif os.path.exists("assets/aqua.png"):
        st.image("assets/aqua.png")
    st.markdown("""
        <div class="excursion-content">
            <div class="excursion-title">🚌 2. Wave Zone & Aquaventure</div>
            <div class="excursion-desc">Piletas de olas, toboganes gigantes y complejos diseñados para pasar un día de agua inolvidable con todo el grupo.</div>
            <div class="excursion-tag">Agua • Adrenalina</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 4. CRAZY DONKEY
    st.markdown("""
        <div class="excursion-card">
            <div class="excursion-content">
                <div class="excursion-title">🚌 3. Crazy Donkey</div>
                <div class="excursion-desc">Aventura extrema en las sierras con tirolesas, desafíos físicos y recreación en un entorno natural increíble.</div>
                <div class="excursion-tag">Aventura • Naturaleza</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 5. CITY TOUR
    st.markdown("""
        <div class="excursion-card">
            <div class="excursion-content">
                <div class="excursion-title">🏙️ 4. City Tour Serrano</div>
                <div class="excursion-desc">Visitamos el Reloj Cucú, fábricas de alfajores y puntos panorámicos. La mejor forma de conocer la esencia de la Villa.</div>
                <div class="excursion-tag">Cultura • Tradición</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Caso San Pedro o error
    if destino == "San Pedro":
        st.info("Estamos preparando las mejores actividades para San Pedro.")
