import streamlit as st

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
            .img-container img {
                width: 100%;
                height: 200px;
                object-fit: cover;
            }
            </style>
        """, unsafe_allow_html=True)

    # Encabezado con foto grupal
    st.image("https://raw.githubusercontent.com/TuUsuario/TuRepo/main/data/vcp/Imagen3.jpg", 
             caption="¡Diversión garantizada con el equipo de Serrano!")

    st.markdown("## 🏞️ Experiencias en Carlos Paz")

    # 1. PEKOS (Con Imagen 2)
    st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/TuUsuario/TuRepo/main/data/vcp/Imagen2.jpg")
    st.markdown("""
        <div class="excursion-content">
            <div class="excursion-title">🎢 Pekos Multiparque</div>
            <div class="excursion-desc">El parque temático número uno. Shows de lobos marinos, cine 5D, laberintos y adrenalina pura en un entorno seguro para todo el grupo.</div>
            <div class="excursion-tag">Full Day • Clásico Imperdible</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 2. WAVE ZONE / AQUAVENTURE (Con Imagen 1)
    st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/TuUsuario/TuRepo/main/data/vcp/Imagen1.jpg")
    st.markdown("""
        <div class="excursion-content">
            <div class="excursion-title">🌊 Wave Zone & Aquaventure</div>
            <div class="excursion-desc">Los mejores parques acuáticos de las sierras. Piletas de olas, toboganes gigantes y complejos diseñados para pasar un día de agua inolvidable.</div>
            <div class="excursion-tag">Agua • Adrenalina • Sol</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 3. CRAZY DONKEY
    st.markdown("""
        <div class="excursion-card">
            <div class="excursion-content">
                <div class="excursion-title">🐴 Crazy Donkey</div>
                <div class="excursion-desc">Multiespacio de aventura: tirolesas, desafíos físicos y mucha recreación en contacto directo con la naturaleza serrana.</div>
                <div class="excursion-tag">Aventura • Team Building</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. CITY TOUR
    st.markdown("""
        <div class="excursion-card">
            <div class="excursion-content">
                <div class="excursion-title">🏙️ City Tour Serrano</div>
                <div class="excursion-desc">Visita al Reloj Cucú, fábricas de alfajores tradicionales y los puntos panorámicos más lindos de la Villa.</div>
                <div class="excursion-tag">Cultura • Regional</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
