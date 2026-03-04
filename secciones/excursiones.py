import streamlit as st
import os

def render_excursiones(destino):
    # --- 1. ESTILOS CSS ---
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
            background: #1a1a1a;
            padding: 12px;
            border-radius: 20px;
            border: 6px solid #333;
            box-shadow: 0px 10px 30px rgba(0,0,0,0.3);
            margin: 20px auto;
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 2. VILLA CARLOS PAZ ---
    if destino == "Villa Carlos Paz":
        if os.path.exists("assets/encabezado.jpg"):
            st.image("assets/encabezado.jpg", use_container_width=True)
        
        st.markdown("## 🏞️ Experiencias en Carlos Paz")
        
        # Pekos
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/pekos.jpg"):
            st.image("assets/pekos.jpg", use_container_width=True)
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
            st.image("assets/aqua.jpg", use_container_width=True)
        st.markdown("""
            <div class="excursion-content">
                <div class="excursion-title">🚌 2. Wave Zone & Aquaventure</div>
                <div class="excursion-desc">Piletas de olas y toboganes gigantes para vivir un día de sol.</div>
                <div class="excursion-tag">Agua • Adrenalina</div>
            </div>
        </div>""", unsafe_allow_html=True)

        # Otras Carlos Paz (Compactas)
        st.markdown("""
            <div class="excursion-card"><div class="excursion-content">
                <div class="excursion-title">🚌 3. Crazy Donkey</div>
                <div class="excursion-desc">Multiespacio de aventura: tirolesas y desafíos físicos en la naturaleza.</div>
                <div class="excursion-tag">Aventura</div>
            </div></div>
            <div class="excursion-card"><div class="excursion-content">
                <div class="excursion-title">🏙️ 4. City Tour Serrano</div>
                <div class="excursion-desc">Reloj Cucú, fábricas de alfajores y puntos panorámicos.</div>
                <div class="excursion-tag">Cultura</div>
            </div></div>
        """, unsafe_allow_html=True)

    # --- 3. SAN PEDRO ---
    elif destino == "San Pedro":
        if os.path.exists("assets/sanpedroexc.jpg"):
            st.image("assets/sanpedroexc.jpg", use_container_width=True)
        
        st.markdown("## 🏞️ Excursiones San Pedro")

        # El Fuerte
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/sanpedroexc2.jpg"):
            st.image("assets/sanpedroexc2.jpg", use_container_width=True)
        st.markdown("""
            <div class="excursion-content">
                <div class="excursion-title">🚌 1. El Fuerte de Obligado</div>
                <div class="excursion-desc">Turismo aventura extremo: palestra, péndulo, rappel y tirolesa con almuerzo de asado criollo.</div>
                <div class="excursion-tag">Aventura • Asado</div>
            </div>
        </div>""", unsafe_allow_html=True)

        # Otras San Pedro
        st.markdown("""
            <div class="excursion-card"><div class="excursion-content">
                <div class="excursion-title">🚌 2. Beach Day con Canotaje</div>
                <div class="excursion-desc">Día de playa exclusivo con bautismo de canotaje seguro en el río.</div>
                <div class="excursion-tag">Playa • Náutica</div>
            </div></div>
            <div class="excursion-card"><div class="excursion-content">
                <div class="excursion-title">🚌 3. Complejo Las Amalias</div>
                <div class="excursion-desc">Laberinto de ligustrinas, plaza húmeda y deportes recreativos.</div>
                <div class="excursion-tag">Recreación</div>
            </div></div>
            <div class="excursion-card"><div class="excursion-content">
                <div class="excursion-title">🚢 4. Sunset Catamarán</div>
                <div class="excursion-desc">Navegación por el Paraná con música al atardecer.</div>
                <div class="excursion-tag">Navegación</div>
            </div></div>
            <div class="excursion-card"><div class="excursion-content">
                <div class="excursion-title">🏙️ 5. City Tour</div>
                <div class="excursion-desc">Recorrido por barrancas, Vía Crucis y compras regionales.</div>
                <div class="excursion-tag">Cultura</div>
            </div></div>
        """, unsafe_allow_html=True)

        # Video San Pedro Final
        st.markdown("---")
        st.markdown("### 🎥 Mirá la Experiencia San Pedro")
        st.markdown('<div class="tv-frame">', unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=xBDqSrNB8Ro")
        st.markdown('</div>', unsafe_allow_html=True)
