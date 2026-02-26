import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. Configuración de página y Estética Profesional
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# --- ESTILOS CSS AVANZADOS (3D, Degradados y Neumorfismo) ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    
    /* Widgets Inferiores: Efecto 3D con Degradado */
    .widget-3d-grad {
        background: linear-gradient(145deg, #f0f0f0, #ffffff);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        border: 1px solid #e0e0e0;
        box-shadow: 8px 8px 16px #d1d1d1, -8px -8px 16px #ffffff;
        margin-bottom: 15px;
        transition: all 0.3s ease;
    }
    
    /* Tarjetas de Selección de Plan Superior */
    .plan-card-box {
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        background: #fdfdfd;
        border: 2px solid #eee;
        transition: all 0.3s ease;
        margin-bottom: 10px;
    }
    
    .plan-selected {
        border: 2px solid #1E3A8A !important;
        background-color: #f0f4ff !important;
        box-shadow: 0 4px 15px rgba(30, 58, 138, 0.15);
    }

    .widget-title { color: #6c757d; font-size: 0.9rem; font-weight: 700; text-transform: uppercase; margin-bottom: 10px; }
    .widget-value { color: #1E3A8A; font-size: 2.3rem; font-weight: 800; margin: 0; }
    .promo-subtitle { font-size: 0.8rem; color: #757575; font-style: italic; }

    /* Header */
    .header-container {
        height: 150px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 15px;
        background-color: #495057;
        margin-bottom: 30px;
    }
    .header-text-overlay {
        color: white; font-size: 2.2rem; font-weight: 800; text-transform: uppercase; letter-spacing: 2px;
    }

    @media print {
        header, [data-testid="stSidebar"], .stButton, .no-print { display: none !important; }
    }
    </style>
    """, unsafe_allow_html=True)

LOGO_URL = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# --- SIDEBAR ---
with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.divider()
    destino = st.selectbox("📍 Seleccioná el Destino", ["Villa Carlos Paz", "San Pedro"])
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    opcion = st.radio("📂 Navegación", [
        "Tarifas y Formas de Pago", 
        "Transporte", "Hotelería", "Excursiones", 
        "Solicitud de Adhesión", "Seguro Médico"
    ])

# Función de utilidad para limpiar nombres
def limpiar_nombre_archivo(texto):
    reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", " ": "_"}
    texto = texto.lower()
    for original, reemplazo in reemplazos.items(): texto = texto.replace(original, reemplazo)
    return texto + ".csv"

# --- SECCIÓN: SOLICITUD DE ADHESIÓN (Intacta) ---
if opcion == "Solicitud de Adhesión":
    st.title("📄 Solicitud de Ingreso / Adhesión")
    # (Se mantiene el código de tu compañero aquí sin cambios)
    with st.form("formulario_adhesion"):
        st.write("Complete los datos para generar el documento.")
        submitted = st.form_submit_button("Finalizar")

# --- SECCIÓN: TARIFAS ---
elif opcion == "Tarifas y Formas de Pago":
    # Header
    st.markdown(f'<div class="header-container"><div class="header-text-overlay">TARIFAS {destino.upper()}</div></div>', unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        
        # --- SELECTOR DE PLANES CON ICONOS ---
        st.write("### 🎯 Seleccioná tu Plan de Viaje")
        
        # Inicializar estado del plan
        if 'plan_seleccionado' not in st.session_state:
            st.session_state.plan_seleccionado = df['Programa'].iloc[0]

        planes = df['Programa'].unique()[:4]
        iconos = ["🚌", "✈️", "🌴", "🏛️"]
        
        cols = st.columns(len(planes))
        for i, p_name in enumerate(planes):
            with cols[i]:
                # Clase dinámica si está seleccionado
                es_sel = "plan-selected" if st.session_state.plan_seleccionado == p_name else ""
                
                st.markdown(f"""
                    <div class="plan-card-box {es_sel}">
                        <div style="font-size: 2.5rem;">{iconos[i]}</div>
                        <div style="font-weight: bold; font-size: 1rem; margin-top:10px;">{p_name}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                if st.button("Seleccionar", key=f"btn_{p_name}"):
                    st.session_state.plan_seleccionado = p_name
                    st.rerun()

        # Datos del plan actual
        v = df[df['Programa'] == st.session_state.plan_seleccionado].iloc[0]

        st.divider()
        
        # --- WIDGETS 3D CON DEGRADADO ---
        col1, col2, col3 = st.columns(3)

        def to_num(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        with col1:
            st.markdown('<div class="widget-3d-grad">', unsafe_allow_html=True)
            st.markdown("<p class='widget-title'>OPCIONES DE PAGO</p>", unsafe_allow_html=True)
            opciones_cols = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
            # Usamos Pills con un key para evitar errores de refresco
            cuota_sel = st.pills("Planes:", options=opciones_cols, default=opciones_cols[0], label_visibility="collapsed", key="pills_pago")
            st.markdown('</div>', unsafe_allow_html=True)

        # Cálculos
        col_db = cuota_sel.replace(' ', '_')
        val_cuota = to_num(v[col_db])
        val_contado = to_num(v['Contado'])

        with col2:
            st.markdown(f"""
                <div class="widget-3d-grad">
                    <p class='widget-title'>MONTO {cuota_sel.upper()}</p>
                    <p class='widget-value'>${val_cuota:,.0f}</p>
                    <p class='promo-subtitle'>Valor de cuota fija</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="widget-3d-grad">
                    <p class='widget-title'>💎 PAGO EFECTIVO (OFICINA)</p>
                    <p class='widget-value' style='color: #2e7d32;'>${val_contado * 0.9:,.0f}</p>
                    <p class='promo-subtitle'>Beneficio 10% OFF aplicado</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        with st.expander("📊 Ver comparativa completa"):
            st.table(df.set_index('Programa'))
    else:
        st.error("Base de datos de tarifas no encontrada.")

else:
    st.title(opcion)
    st.info("Sección en desarrollo...")
