import streamlit as st
import os

def render_seguro(destino):
    # 1. ESTILOS CSS PARA ESTA SECCIÓN
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
            color: gold;
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            display: inline-block;
            margin-bottom: 15px;
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. ENCABEZADO VISUAL (Foto Staff)
    if os.path.exists("assets/Staff.jpg"):
        st.image("assets/Staff.jpg", use_container_width=True, caption="Equipo de Coordinación Serrano Turismo")
    elif os.path.exists("assets/Staff.png"):
        st.image("assets/Staff.png", use_container_width=True)

    # 3. BLOQUE DE COORDINACIÓN (Lo más importante)
    st.markdown('<div class="experience-badge">🏆 29 Años de Trayectoria</div>', unsafe_allow_html=True)
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
                supervisando cada detalle, desde la hotelería hasta las excursiones, garantizando una 
                ejecución perfecta y la tranquilidad absoluta de las familias.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 4. DETALLES DE COBERTURA MÉDICA
    st.markdown("### 🛡️ Cobertura Médica Total")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="feature-box">
                <h4 style='color: #4A90E2;'>🚑 Asistencia 24hs</h4>
                <ul style='font-size: 0.9rem; color: #555;'>
                    <li>Atención médica en el hotel y centros especializados.</li>
                    <li>Traslados en ambulancias de alta complejidad si fuera necesario.</li>
                    <li>Servicio de enfermería permanente.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="feature-box">
                <h4 style='color: #4A90E2;'>💊 Medicamentos y Más</h4>
                <ul style='font-size: 0.9rem; color: #555;'>
                    <li>Cobertura total en medicamentos recetados.</li>
                    <li>Asistencia odontológica de urgencia.</li>
                    <li>Seguro de Accidentes Personales y Responsabilidad Civil.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.info("💡 **Dato Serrano:** Nuestra estructura de coordinación propia nos permite resolver cualquier imprevisto en tiempo real, sin depender de terceros.")
