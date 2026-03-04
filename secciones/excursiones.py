import streamlit as st
import os

def render_excursiones(destino):
    # 1. ESTILOS CSS
    st.markdown("""
        <style>
        .excursion-card {
            background: white;
            border-radius: 12px;
            padding: 15px;
            border: 1px solid #e0e0e0;
            margin-bottom: 15px;
        }
        .excursion-title { color: #1a1c1e; font-weight: 700; margin-bottom: 5px; }
        .excursion-desc { color: #495057; font-size: 0.85rem; }
        .tv-frame {
            background: #222;
            border: 10px solid #333;
            border-radius: 20px;
            padding: 10px;
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    if destino == "Villa Carlos Paz":
        if os.path.exists("assets/encabezado.jpg"):
            st.image("assets/encabezado.jpg")
        st.header("🏞️ Excursiones Carlos Paz")
        
        # Pekos
        st.subheader("🚌 1. Pekos Multiparque")
        if os.path.exists("assets/pekos.jpg"):
            st.image("assets/pekos.jpg")
        st.write("Cine 5D, laberintos y adrenalina en un complejo único.")

        # Aqua
        st.subheader("🚌 2. Wave Zone & Aquaventure")
        if os.path.exists("assets/aqua.jpg"):
            st.image("assets/aqua.jpg")
        st.write("Piletas de olas y toboganes gigantes.")

    elif destino == "San Pedro":
        # Encabezado San Pedro
        if os.path.exists("assets/sanpedroexc.jpg"):
            st.image("assets/sanpedroexc.jpg")
        
        st.header("🏞️ Excursiones San Pedro")

        # Fuerte de Obligado
        st.subheader("🚌 1. El Fuerte de Obligado")
        if os.path.exists("assets/sanpedroexc2.jpg"):
            st.image("assets/sanpedroexc2.jpg")
        st.write("Aventura con palestra, rappel y tirolesa. Almuerzo de asado criollo.")

        # Otros San Pedro
        st.markdown("""
            <div class="excursion-card">
                <div class="excursion-title">🚌 2. Beach Day con Canotaje</div>
                <div class="excursion-desc">Día de playa exclusivo con bautismo de canotaje seguro.</div>
            </div>
            <div class="excursion-card">
                <div class="excursion-title">🚌 3. Complejo Las Amalias</div>
                <div class="excursion-desc">Laberinto de ligustrinas, piletas y deportes recreativos.</div>
            </div>
            <div class="excursion-card">
                <div class="excursion-title">🚢 4. Sunset Catamarán</div>
                <div class="excursion-desc">Navegación por el Paraná con música al atardecer.</div>
            </div>
            <div class="excursion-card">
                <div class="excursion-title">🏙️ 5. City Tour</div>
                <div class="excursion-desc">Recorrido por barrancas y compras regionales.</div>
            </div>
        """, unsafe_allow_html=True)

        # Video San Pedro con Marco de TV
        st.divider()
        st.subheader("🎥 Mirá la Experiencia San Pedro")
        st.markdown('<div class="tv-frame">', unsafe_allow_html=True)
        st.video("https://www.youtube.com/watch?v=xBDqSrNB8Ro")
        st.markdown('</div>', unsafe_allow_html=True)
