import streamlit as st
import os

def render_seguro(destino):
    # 1. ESTILOS CSS (Slim & Modern)
    st.markdown("""
        <style>
        .staff-header {
            background-color: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            border-left: 5px solid #4A90E2;
            margin-bottom: 25px;
        }
        .highlight-text {
            color: #4A90E2;
            font-weight: 800;
            font-size: 1.2rem;
            margin-bottom: 10px;
            display: block;
        }
        .feature-box {
            background: white;
            padding: 15px;
            border-radius: 10px;
            border: 1px solid #e0e0e0;
            height: 100%;
        }
        .experience-badge {
            background: #1a1a1a;
            color: #FFD700;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 15px;
            font-size: 0.8rem;
        }
        .viaxlab-card {
            background: linear-gradient(145deg, #6366f1, #4338ca);
            color: white;
            padding: 25px;
            border-radius: 20px;
            text-align: center;
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. ENCABEZADO VISUAL (Foto Staff)
    if os.path.exists("assets/Staff.jpg"):
        st.image("assets/Staff.jpg", use_container_width=True)
    elif os.path.exists("assets/Staff.png"):
        st.image("assets/Staff.png", use_container_width=True)

    # 3. BLOQUE DE COORDINACIÓN
    st.markdown('<div class="experience-badge">🏆 29 AÑOS DE TRAYECTORIA</div>', unsafe_allow_html=True)
    st.markdown("## 🏥 Coordinación y Seguridad")
    
    st.markdown("""
        <div class="staff-header">
            <span class="highlight-text">COORDINACIÓN Y PERSONAL ESTABLE</span>
            <p style='font-size: 1.05rem; line-height: 1.6; color: #333;'>
                Para <b>Serrano Turismo</b>, la coordinación es el pilar fundamental del viaje. 
                Contamos con un equipo de profesionales apasionados: <b>Profesores de Educación Física y Técnicos en Recreación</b> 
                especializados en manejo de grupos estudiantiles y deportivos.
                <br><br>
                Además, disponemos de <b>Personal Directivo apostado permanentemente en el destino</b>, 
                supervisando cada detalle y garantizando una ejecución perfecta para la tranquilidad absoluta de las familias.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 4. SECCIÓN VIAXLAB (APP DEL VIAJE)
    st.markdown("""
        <div class="viaxlab-card">
            <h3 style='color: white; margin-bottom: 10px;'>📱 Seguí el viaje con Viaxlab</h3>
            <p style='font-size: 0.95rem; opacity: 0.9;'>
                Toda la información del viaje en la palma de tu mano. 
                Fotos en tiempo real, itinerario actualizado y comunicación directa.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.link_button("🚀 Acceder a Viaxlab Web", "https://app.viaxlab.com/", use_container_width=True)
    with col_v2:
        st.link_button("📥 Descargar App", "https://viaxlab.com/descargar", use_container_width=True)

    st.divider()

    # 5. DETALLES DE COBERTURA MÉDICA
    st.markdown("### 🛡️ Cobertura Médica Total")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="feature-box">
                <h4 style='color: #4A90E2; font-size: 1.1rem;'>🚑 Asistencia 24hs</h4>
                <p style='font-size: 0.85rem; color: #555;'>
                    Atención médica en el hotel y centros especializados de alta complejidad. 
                    Traslados en ambulancias propias y servicio de enfermería permanente.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="feature-box">
                <h4 style='color: #4A90E2; font-size: 1.1rem;'>💊 Medicamentos</h4>
                <p style='font-size: 0.85rem; color: #555;'>
                    Cobertura total en medicamentos recetados, asistencia odontológica de urgencia 
                    y seguros de Accidentes Personales incluidos.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.caption("Serrano Turismo: Seguridad y confianza respaldada por casi 3 décadas de experiencia.")
