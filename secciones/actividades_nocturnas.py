import streamlit as st
import os
from utilidades.footer import render_footer

def render_nocturnas(destino):
    # --- 1. ESTILOS CSS ---
    st.markdown("""
        <style>
        .night-card { 
            background: white; 
            border-radius: 15px; 
            border: 1px solid #e0e0e0; 
            margin-bottom: 20px; 
            overflow: hidden; 
            box-shadow: 0px 4px 10px rgba(0,0,0,0.05); 
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 100%;
        }
        .night-card:hover {
            transform: translateY(-5px);
            box-shadow: 0px 10px 20px rgba(0,0,0,0.15);
        }
        .night-content { padding: 20px; }
        .night-title { color: #1E3A8A; font-size: 1.15rem; font-weight: 800; margin-bottom: 10px; text-transform: uppercase;}
        .night-desc { color: #444; font-size: 0.95rem; line-height: 1.5; }
        </style>
    """, unsafe_allow_html=True)

    # --- 2. TÍTULO Y PORTADA ---
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🌙 ACTIVIDADES NOCTURNAS EN {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # Portada centrada y contenida (para que no ocupe todo el ancho de la pantalla)
    col_espacio1, col_img, col_espacio2 = st.columns([1, 2, 1])
    with col_img:
        if os.path.exists("assets/fogon.jpg"):
            st.image("assets/fogon.jpg", use_container_width=True, caption="Noches inolvidables junto a tus compañeros")
        else:
            st.info("🖼️ Falta cargar: assets/fogon.jpg")
            
    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. SECCIÓN VILLA CARLOS PAZ ---
    if "Villa Carlos Paz" in destino:
        st.markdown("<h3 style='text-align: center; color: #1E3A8A;'>🕺 Diversión y Eventos Exclusivos</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666; margin-bottom: 30px;'>Noches diseñadas para crear recuerdos inolvidables con la máxima seguridad.</p>", unsafe_allow_html=True)
        
        # Grilla de 2 columnas
        col1, col2 = st.columns(2, gap="medium")

        with col1:
            st.markdown("""
                <div class="night-card">
                    <div class="night-content">
                        <div class="night-title">🧩 Juegos Nocturnos</div>
                        <div class="night-desc">En el marco del hotel realizaremos actividades como fiesta de disfraces, búsqueda del tesoro y fiestas temáticas.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("""
                <div class="night-card" style="border-left: 5px solid #1E3A8A;">
                    <div class="night-content">
                        <div class="night-title">🎭 Matinée Serrano VIP</div>
                        <div class="night-desc">Noche de Fiesta Privada en la Disco <b>MOLINO ROJO</b>, contando con la exclusividad del lugar para nuestros pasajeros.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("""
                <div class="night-card">
                    <div class="night-content">
                        <div class="night-title">🔥 Fogón</div>
                        <div class="night-desc">El grupo se reúne para cerrar la noche y afianzar los lazos de amistad de la primaria, permitiendo la libre expresión y reflexión del viaje.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div class="night-card">
                    <div class="night-content">
                        <div class="night-title">🕯️ Cena de Velas</div>
                        <div class="night-desc">Noche especial donde tendremos una cena a la luz de las velas llena de sorpresas y emociones.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("""
                <div class="night-card" style="border-left: 5px solid #1E3A8A;">
                    <div class="night-content">
                        <div class="night-title">💦 Pool Party</div>
                        <div class="night-desc">Fiesta increíble en pileta climatizada con show de láser y luces en un marco de total diversión y seguridad.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    # --- 4. SECCIÓN SAN PEDRO ---
    elif "San Pedro" in destino:
        st.markdown("<h3 style='text-align: center; color: #1E3A8A;'>✨ Noches de Integración y Magia</h3>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #666; margin-bottom: 30px;'>Momentos diseñados para fortalecer los lazos de amistad y la diversión compartida.</p>", unsafe_allow_html=True)

        col1, col2 = st.columns(2, gap="medium")
        
        with col1:
            st.markdown("""
                <div class="night-card" style="border-left: 5px solid #1E3A8A;">
                    <div class="night-content">
                        <div class="night-title">🎉 Fiesta de Bienvenida</div>
                        <div class="night-desc">Realizaremos una fiesta de disfraces en el complejo <b>Macoco</b> (exclusivo para los chicos de Serrano) con juegos, desfiles y concursos.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

            st.markdown("""
                <div class="night-card">
                    <div class="night-content">
                        <div class="night-title">🧩 Juegos Nocturnos</div>
                        <div class="night-desc">En el marco del hotel realizaremos actividades como fiesta de disfraces, búsqueda del tesoro y fiestas temáticas.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown("""
                <div class="night-card">
                    <div class="night-content">
                        <div class="night-title">🔥 Cena de Velas y Fogón</div>
                        <div class="night-desc">El grupo se reúne para cerrar la noche con el Fogón y afianzar los lazos de amistad de la primaria, permitiendo la libre expresión y reflexión del viaje.</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

    else:
        st.info("La agenda nocturna se confirmará según la disponibilidad de fechas locales.")

    st.markdown("---")
    st.caption("✨ *Todas las actividades nocturnas cuentan con la supervisión de nuestro equipo de animación propia y seguridad.*")

    # --- 5. FOOTER INSTITUCIONAL ---
    render_footer()
