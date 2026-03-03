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

        # 1. ENCABEZADO GRUPAL (Imagen 3)
        if os.path.exists("assets/Imagen3.jpg"):
            st.image("assets/Imagen3.jpg", caption="¡El equipo de Serrano disfrutando en las sierras!")

        st.markdown("## 🏞️ Experiencias en Carlos Paz")

        # 2. PEKOS (Imagen 2)
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/Imagen2.jpg"):
            st.image("assets/Imagen2.jpg")
        st.markdown("""
            <div class="excursion-content">
                <div class="excursion-title">🎢 Pekos Multiparque</div>
                <div class="excursion-desc">Un clásico que nunca falla. Disfrutamos de shows exclusivos, laberintos, cine 5D y mucha diversión temática con la seguridad que caracteriza a Serrano.</div>
                <div class="excursion-tag">Full Day • Entretenimiento</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 3. WAVE ZONE & AQUAVENTURE (Imagen 1)
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/Imagen1.jpg"):
            st.image("assets/Imagen1.jpg")
        st.markdown("""
            <div class="excursion-content">
                <div class="excursion-title">🌊 Wave Zone & Aquaventure</div>
                <div class="excursion-desc">Adrenalina en el agua: piletas de olas, toboganes gigantes y complejos de primer nivel para vivir un día de sol y pura acción serrana.</div>
                <div class="excursion-tag">Agua • Adrenalina</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # 4. CRAZY DONKEY
        st.markdown("""
            <div class="excursion-card">
                <div class="excursion-content">
                    <div class="excursion-title">🐴 Crazy Donkey</div>
                    <div class="excursion-desc">Aventura extrema en las sierras: tirolesas, arquería y desafíos grupales en un complejo diseñado para el trabajo en equipo y la diversión.</div>
                    <div class="excursion-tag">Aventura • Naturaleza</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 5. CITY TOUR
        st.markdown("""
            <div class="excursion-card">
                <div class="excursion-content">
                    <div class="excursion-title">🏙️ City Tour Serrano</div>
                    <div class="excursion-desc">Visitamos el Reloj Cucú, las mejores fábricas de alfajores y los puntos panorámicos más emblemáticos para llevarte el mejor recuerdo de la Villa.</div>
                    <div class="excursion-tag">City Tour • Tradición</div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.markdown("## 🏞️ Excursiones San Pedro")
        st.info("Estamos preparando las mejores actividades para San Pedro.")
