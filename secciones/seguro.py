import streamlit as st
import os
from utilidades.footer import render_footer

def render_seguro(destino):
    # 1. ESTILOS CSS (Slim & Trust-Focused)
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
            background: #ffffff;
            padding: 18px;
            border-radius: 12px;
            border: 1px solid #eef2f6;
            height: 100%;
            box-shadow: 0px 2px 4px rgba(0,0,0,0.02);
        }
        .insurance-partner {
            background: #f1f5f9;
            padding: 10px 15px;
            border-radius: 8px;
            font-weight: 700;
            color: #1e293b;
            font-size: 0.85rem;
            display: inline-block;
            margin-right: 10px;
            margin-bottom: 10px;
            border: 1px solid #cbd5e1;
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
                Todos los pasajeros están identificados con una <b>pulsera de seguimiento</b> vinculada a la App, 
                conteniendo sus datos médicos actualizados para una respuesta inmediata.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col_v1, col_v2 = st.columns(2)
    with col_v1:
        st.link_button("🚀 Acceder a Viaxlab Web", "https://app.viaxlab.com/", use_container_width=True)
    with col_v2:
        st.link_button("📥 Descargar App", "https://viaxlab.com/descargar", use_container_width=True)

    st.divider()

    # 5. COBERTURA MÉDICA AMPLIADA
    st.markdown("### 🛡️ Respaldo y Cobertura Total")
    
    # Partners de Seguro
    st.markdown("""
        <div style='margin-bottom: 20px;'>
            <div class="insurance-partner">🛡️ San Cristóbal Seguros</div>
            <div class="insurance-partner">⚕️ Assistravel</div>
        </div>
    """, unsafe_allow_html=True)

    st.write("Contamos con el respaldo de las empresas más importantes del país, con asistencia inmediata y permanente desde el inicio hasta el fin del tour.")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="feature-box">
                <h4 style='color: #4A90E2; font-size: 1rem;'>🏥 Infraestructura Médica</h4>
                <ul style='font-size: 0.85rem; color: #444; padding-left: 20px;'>
                    <li><b>Médico permanente</b> a disposición 24hs en el hotel.</li>
                    <li>Acceso a más de <b>45 Clínicas y Sanatorios</b> en todo el trayecto.</li>
                    <li>Atención en ruta y destino asegurada.</li>
                    <li>Traslados terrestres y aéreos (regulares y sanitarios).</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="feature-box">
                <h4 style='color: #4A90E2; font-size: 1rem;'>💊 Cobertura Prestacional</h4>
                <ul style='font-size: 0.85rem; color: #444; padding-left: 20px;'>
                    <li><b>Medicamentos en mano</b> para respuesta eficaz.</li>
                    <li>Internaciones, cirugías (mayor y menor) y yesos.</li>
                    <li>Odontología de urgencia y material descartable.</li>
                    <li>Cobertura de <b>preexistencias agudizadas</b>.</li>
                    <li>Seguimiento post-viaje hasta el alta médica.</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.info("💡 **Dato Serrano:** La seguridad de nuestros pasajeros no es un opcional, es nuestra prioridad absoluta desde hace 29 años.")


 # --- 5. FOOTER INSTITUCIONAL ---
    # Invocamos la función del archivo utilidades/footer.py
    render_footer()
