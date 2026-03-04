import streamlit as st
import os
from utilidades.footer import render_footer

def render_excursiones(destino):
    # --- 1. ESTILOS CSS ---
    st.markdown("""
        <style>
        .excursion-card { background: white; border-radius: 12px; border: 1px solid #e0e0e0; margin-bottom: 20px; overflow: hidden; box-shadow: 0px 4px 10px rgba(0,0,0,0.05); }
        .excursion-content { padding: 15px; }
        .excursion-title { color: #1a1c1e; font-size: 1.1rem; font-weight: 700; margin-bottom: 5px; }
        .excursion-desc { color: #495057; font-size: 0.85rem; line-height: 1.4; }
        .excursion-tag { display: inline-block; background: #e1edff; color: #4A90E2; font-size: 0.7rem; font-weight: 700; padding: 3px 10px; border-radius: 5px; margin-top: 10px; text-transform: uppercase; }
        .tv-container { background: #1a1a1a; padding: 15px; border-radius: 20px; border: 8px solid #333; box-shadow: 0px 10px 30px rgba(0,0,0,0.3); margin-bottom: 25px; }
        </style>
    """, unsafe_allow_html=True)

    # --- 2. VILLA CARLOS PAZ ---
    if destino == "Villa Carlos Paz":
        if os.path.exists("assets/encabezado.jpg"):
            st.image("assets/encabezado.jpg", use_container_width=True)
        st.markdown("## 🏞️ Experiencias en Carlos Paz")
        
        # Video VCP
        st.markdown('<div class="tv-container">', unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=D-YV7S6Oatc")
        st.markdown('</div>', unsafe_allow_html=True)

        # Pekos
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/pekos.jpg"):
            st.image("assets/pekos.jpg", use_container_width=True)
        st.markdown('<div class="excursion-content"><div class="excursion-title">🚌 1. Pekos Multiparque</div><div class="excursion-desc">Cine 5D, laberintos y adrenalina en un complejo recreativo único.</div><div class="excursion-tag">Full Day</div></div></div>', unsafe_allow_html=True)

        # Aqua
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/aqua.jpg"):
            st.image("assets/aqua.jpg", use_container_width=True)
        st.markdown('<div class="excursion-content"><div class="excursion-title">🚌 2. Wave Zone & Aquaventure</div><div class="excursion-desc">Piletas de olas y toboganes gigantes para vivir un día de sol.</div><div class="excursion-tag">Agua</div></div></div>', unsafe_allow_html=True)

        # Otros VCP
        st.markdown('<div class="excursion-card"><div class="excursion-content"><div class="excursion-title">🚌 3. Crazy Donkey</div><div class="excursion-desc">Aventura: tirolesas y desafíos físicos en la naturaleza.</div><div class="excursion-tag">Aventura</div></div></div>', unsafe_allow_html=True)
        st.markdown('<div class="excursion-card"><div class="excursion-content"><div class="excursion-title">🏙️ 4. City Tour Serrano</div><div class="excursion-desc">Reloj Cucú y fábricas de alfajores tradicionales.</div><div class="excursion-tag">Cultura</div></div></div>', unsafe_allow_html=True)

    # --- 3. SAN PEDRO ---
    elif destino == "San Pedro":
        if os.path.exists("assets/sanpedroexc.jpg"):
            st.image("assets/sanpedroexc.jpg", use_container_width=True)
        st.markdown("## 🏞️ Excursiones San Pedro")

        # Dos imágenes en reemplazo del video
        col_img1, col_img2 = st.columns(2)
        
        with col_img1:
            # Reemplazá "imagen1.jpg" por el nombre de tu primer foto
            if os.path.exists("assets/imagen1.jpg"):
                st.image("assets/imagen1.jpg", use_container_width=True, border=True)
            else:
                st.info("🖼️ Falta cargar: assets/imagen1.jpg")
                
        with col_img2:
            # Reemplazá "imagen2.jpg" por el nombre de tu segunda foto
            if os.path.exists("assets/imagen2.jpg"):
                st.image("assets/imagen2.jpg", use_container_width=True, border=True)
            else:
                st.info("🖼️ Falta cargar: assets/imagen2.jpg")

        st.markdown("<br>", unsafe_allow_html=True)

        # El Fuerte
        st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
        if os.path.exists("assets/sanpedroexc2.jpg"):
            st.image("assets/sanpedroexc2.jpg", use_container_width=True)
        st.markdown('<div class="excursion-content"><div class="excursion-title">🚌 1. El Fuerte de Obligado</div><div class="excursion-desc">Aventura extrema: palestra, rappel y tirolesa con asado criollo.</div><div class="excursion-tag">Aventura • Asado</div></div></div>', unsafe_allow_html=True)

        # Otros San Pedro
        st.markdown('<div class="excursion-card"><div class="excursion-content"><div class="excursion-title">🚌 2. Beach Day con Canotaje</div><div class="excursion-desc">Día de playa exclusivo con bautismo de canotaje seguro.</div><div class="excursion-tag">Playa</div></div></div>', unsafe_allow_html=True)
        st.markdown('<div class="excursion-card"><div class="excursion-content"><div class="excursion-title">🚌 3. Complejo Las Amalias</div><div class="excursion-desc">Laberinto de ligustrinas y deportes recreativos.</div><div class="excursion-tag">Recreación</div></div></div>', unsafe_allow_html=True)
        st.markdown('<div class="excursion-card"><div class="excursion-content"><div class="excursion-title">🚢 4. Sunset Catamarán</div><div class="excursion-desc">Navegación por el Paraná con música al atardecer.</div><div class="excursion-tag">Navegación</div></div></div>', unsafe_allow_html=True)
        st.markdown('<div class="excursion-card"><div class="excursion-content"><div class="excursion-title">🏙️ 5. City Tour</div><div class="excursion-desc">Recorrido por barrancas y compras regionales.</div><div class="excursion-tag">Cultura</div></div></div>', unsafe_allow_html=True)

    # --- 5. FOOTER INSTITUCIONAL ---
    # Invocamos la función del archivo utilidades/footer.py
    render_footer()
