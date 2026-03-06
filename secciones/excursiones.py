import streamlit as st
import os
from utilidades.footer import render_footer

def render_excursiones(destino):
    # --- 1. ESTILOS CSS MEJORADOS ---
    st.markdown("""
        <style>
        .excursion-card { 
            background: white; 
            border-radius: 15px; 
            border: 1px solid #e0e0e0; 
            margin-bottom: 20px; 
            overflow: hidden; 
            box-shadow: 0px 4px 10px rgba(0,0,0,0.05); 
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 100%;
        }
        .excursion-card:hover {
            transform: translateY(-5px);
            box-shadow: 0px 10px 20px rgba(0,0,0,0.15);
        }
        .excursion-content { padding: 15px; }
        .excursion-title { color: #1E3A8A; font-size: 1.2rem; font-weight: 800; margin-bottom: 5px; }
        .excursion-desc { color: #555; font-size: 0.9rem; line-height: 1.4; }
        .excursion-tag { 
            display: inline-block; 
            background: #e1edff; 
            color: #1E3A8A; 
            font-size: 0.75rem; 
            font-weight: bold; 
            padding: 4px 12px; 
            border-radius: 20px; 
            margin-top: 12px; 
            text-transform: uppercase; 
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 2. VILLA CARLOS PAZ ---
    if destino == "Villa Carlos Paz":
        if os.path.exists("assets/encabezado.jpg"):
            st.image("assets/encabezado.jpg", use_container_width=True)
        
        st.markdown("<h2 style='text-align: center; color: #1E3A8A; margin-top: 20px;'>🎢 Parques y Aventura en Carlos Paz</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666; margin-bottom: 30px;'>Los mejores complejos para vivir días a pura adrenalina y diversión con amigos.</p>", unsafe_allow_html=True)
        
        # Grilla de 2 columnas para que quede ordenado y visual
        col1, col2 = st.columns(2, gap="medium")

        with col1:
            # 1. Pekos
            st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
            if os.path.exists("assets/pekos.png"):
                st.image("assets/pekos.png", use_container_width=True)
            else:
                st.info("🖼️ Falta: assets/pekos.png")
            st.markdown('<div class="excursion-content"><div class="excursion-title">🎡 Pekos Multiparque</div><div class="excursion-desc">Cine 5D, laberintos de espejos, montañas rusas, shows y juegos mecánicos en un complejo recreativo inmenso.</div><div class="excursion-tag">Día Completo</div></div></div>', unsafe_allow_html=True)

            # 3. Crazy Donkey
            st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
            if os.path.exists("assets/crazy.png"):
                st.image("assets/crazy.png", use_container_width=True)
            else:
                st.info("🖼️ Falta: assets/crazy.png")
            st.markdown('<div class="excursion-content"><div class="excursion-title">🧗‍♂️ Crazy Donkey</div><div class="excursion-desc">Aventura en las sierras: tirolesas gigantes, puentes colgantes, parque acuatico, y toboganes novedosos.</div><div class="excursion-tag">Aventura</div></div></div>', unsafe_allow_html=True)

        with col2:
            # 2. Aquaventure
            st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
            if os.path.exists("assets/aqua.png"):
                st.image("assets/aqua.png", use_container_width=True)
            else:
                st.info("🖼️ Falta: assets/aqua.png")
            st.markdown('<div class="excursion-content"><div class="excursion-title">🌊 Aquaventure</div><div class="excursion-desc">Toboganes, piletas, plaza humeda y juegos acuáticos increíbles para disfrutar a pleno bajo el sol cordobés.</div><div class="excursion-tag">Parque Acuático</div></div></div>', unsafe_allow_html=True)

            # 4. Wave Zone
            st.markdown('<div class="excursion-card">', unsafe_allow_html=True)
            if os.path.exists("assets/wave.png"):
                st.image("assets/wave.png", use_container_width=True)
            else:
                st.info("🖼️ Falta: assets/wave.png")
            st.markdown('<div class="excursion-content"><div class="excursion-title">🏄‍♀️ Wave Zone</div><div class="excursion-desc">La pileta de olas más grande de la villa, animadores en vivo y mucha música. Rampas, toboganes inflables y mucho mas.</div><div class="excursion-tag">Agua & Fiesta</div></div></div>', unsafe_allow_html=True)

        st.divider()

        # Paseos clásicos (Sin fotos, solo iconos)
        st.markdown("<h3 style='color: #1E3A8A;'>🏙️ Paseos Clásicos</h3>", unsafe_allow_html=True)
        
        c_city, c_alfa = st.columns(2)
        with c_city:
            st.markdown("""
                <div class="excursion-card" style="border-left: 5px solid #1E3A8A;">
                    <div class="excursion-content">
                        <div class="excursion-title">📸 City Tour Serrano</div>
                        <div class="excursion-desc">Recorremos el pintoresco centro, la costanera del Lago San Roque y su nuevo puente.</div>
                        <div class="excursion-tag">Recorrido</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
        with c_alfa:
            st.markdown("""
                <div class="excursion-card" style="border-left: 5px solid #1E3A8A;">
                    <div class="excursion-content">
                        <div class="excursion-title">🍫 Fábrica de Alfajores</div>
                        <div class="excursion-desc">Visita guiada para conocer los secretos de la elaboración de los alfajores cordobeses. ¡Obviamente incluye degustación!</div>
                        <div class="excursion-tag">Gastronomía</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # --- 3. SAN PEDRO ---
    elif destino == "San Pedro":
        if os.path.exists("assets/sanpedroexc.jpg"):
            st.image("assets/sanpedroexc.jpg", use_container_width=True)
        st.markdown("## 🏞️ Excursiones San Pedro")

        # Dos imágenes en reemplazo del video
        col_img1, col_img2 = st.columns(2)
        
        with col_img1:
            if os.path.exists("assets/imagen1.jpg"):
                st.image("assets/imagen1.jpg", use_container_width=True)
            else:
                st.info("🖼️ Falta cargar: assets/imagen1.jpg")
                
        with col_img2:
            if os.path.exists("assets/imagen2.jpg"):
                st.image("assets/imagen2.jpg", use_container_width=True)
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
    render_footer()
