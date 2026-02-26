import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. Configuración de página y Estética Profesional
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# --- ESTILOS CSS AVANZADOS (3D y Degradados) ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    
    /* Efecto 3D y Degradado para Widgets inferiores */
    .widget-3d-grad {
        background: linear-gradient(145deg, #ffffff, #e6e6e6);
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        border: 1px solid #d1d1d1;
        box-shadow: 5px 5px 15px #d1d1d1, -5px -5px 15px #ffffff; /* Efecto Neumorfismo/3D */
        margin-bottom: 10px;
        transition: transform 0.2s;
    }
    .widget-3d-grad:hover {
        transform: translateY(-5px);
    }

    /* Estilo para las tarjetas de Selección de Viaje */
    .plan-card {
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        cursor: pointer;
        border: 2px solid #eee;
        transition: all 0.3s;
        background-color: #fdfdfd;
    }
    .plan-card-selected {
        border: 2px solid #1E3A8A !important;
        background-color: #f0f4ff !important;
        box-shadow: 0 4px 12px rgba(30, 58, 138, 0.2);
    }

    /* Header */
    .header-container {
        position: relative;
        height: 180px;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 15px;
        margin-bottom: 30px;
        background-color: #495057;
        overflow: hidden;
    }
    .header-text-overlay {
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
    }

    .widget-title { color: #6c757d; font-size: 0.85rem; font-weight: 700; text-transform: uppercase; margin-bottom: 5px; }
    .widget-value { color: #1E3A8A; font-size: 2.1rem; font-weight: 800; margin: 0; }
    .promo-subtitle { font-size: 0.75rem; color: #757575; }

    @media print {
        header, [data-testid="stSidebar"], .stButton, .no-print { display: none !important; }
        .print-only { display: block !important; }
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

    st.sidebar.divider()
    st.markdown("""<div style="font-size: 0.8rem; color: #6c757d;"><b>CABA:</b> Av. Rivadavia 4532<br><b>WA:</b> (011) 5609-6283</div>""", unsafe_allow_html=True)

def limpiar_nombre_archivo(texto):
    reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", " ": "_"}
    texto = texto.lower()
    for original, reemplazo in reemplazos.items(): texto = texto.replace(original, reemplazo)
    return texto + ".csv"

# --- SECCIÓN: SOLICITUD DE ADHESIÓN (Trabajo de tu compañero, intacto) ---
if opcion == "Solicitud de Adhesión":
    st.image(LOGO_URL, width=200)
    st.title("📄 Solicitud de Ingreso / Adhesión")
    with st.form("formulario_adhesion"):
        col1, col2, col3 = st.columns(3)
        with col1:
            fecha_doc = st.date_input("Fecha", datetime.now())
            contrato = st.text_input("Contrato N°")
        with col2:
            colegio = st.text_input("Colegio / Instituto")
            año_div = st.text_input("Año y División")
        with col3:
            liberado = st.text_input("% L.O. (Porcentaje Liberado)")
        
        st.markdown("#### Datos del Alumno")
        c_al1, c_al2 = st.columns(2)
        with c_al1:
            ap_alumno = st.text_input("Apellido Alumno")
            dni_alumno = st.text_input("DNI Alumno")
        with c_al2:
            nom_alumno = st.text_input("Nombres Alumno")
            sexo = st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)
            
        submitted = st.form_submit_button("Finalizar y Preparar para Imprimir")
        if submitted: st.success("Formulario completado.")

# --- SECCIÓN: TARIFAS ---
elif opcion == "Tarifas y Formas de Pago":
    # Header
    header_img_path = None
    for ext in [".jpg", ".png", ".jpeg"]:
        temp_path = f"data/{folder}/tarifas_y_formas_header{ext}"
        if os.path.exists(temp_path):
            header_img_path = temp_path
            break

    if header_img_path: st.image(header_img_path, use_container_width=True)
    else: st.markdown(f'<div class="header-container"><div class="header-text-overlay">TARIFAS {destino.upper()}</div></div>', unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        
        # --- NUEVO SELECTOR DE PLANES (4 ICONOS EN PARALELO) ---
        st.write("### 🎯 Seleccioná tu Plan de Viaje")
        
        # Inicializar estado si no existe
        if 'plan_idx' not in st.session_state:
            st.session_state.plan_idx = 0

        # Mostramos los primeros 4 programas del CSV
        planes_visibles = df['Programa'].tolist()[:4]
        iconos = ["🚌", "✈️", "🏢", "🌟"] # Iconos referenciales
        
        cols_planes = st.columns(4)
        for i, plan in enumerate(planes_visibles):
            with cols_planes[i]:
                # Estilo dinámico si está seleccionado
                es_seleccionado = (st.session_state.plan_idx == i)
                border_style = "border: 2px solid #1E3A8A; background-color: #f0f4ff;" if es_seleccionado else "border: 1px solid #eee;"
                
                # Usamos un botón invisible sobre un contenedor visual
                st.markdown(f"""
                    <div style="{border_style} border-radius:12px; padding:15px; text-align:center;">
                        <div style="font-size:2rem;">{iconos[i % len(iconos)]}</div>
                        <div style="font-weight:bold; font-size:0.9rem; margin-top:5px;">{plan}</div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"Seleccionar {i}", key=f"btn_{i}", label_visibility="collapsed"):
                    st.session_state.plan_idx = i
                    st.rerun()

        # Datos del plan seleccionado
        v = df.iloc[st.session_state.plan_idx]

        st.divider()
        
        # --- WIDGETS 3D CON DEGRADADO EN PARALELO ---
        col_pago, col_monto, col_efectivo = st.columns(3)

        def clean_val(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        with col_pago:
            st.markdown('<div class="widget-3d-grad">', unsafe_allow_html=True)
            st.markdown("<p class='widget-title'>OPCIONES DE PAGO</p>", unsafe_allow_html=True)
            cols_cuotas = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
            cuota_sel = st.pills("Selección:", options=cols_cuotas, default=cols_cuotas[0], label_visibility="collapsed")
            st.markdown('</div>', unsafe_allow_html=True)

        col_db = cuota_sel.replace(' ', '_')
        val_cuota = clean_val(v[col_db])
        val_contado = clean_val(v['Contado'])

        with col_monto:
            st.markdown(f"""
                <div class="widget-3d-grad">
                    <p class='widget-title'>MONTO {cuota_sel.upper()}</p>
                    <p class='widget-value'>${val_cuota:,.0f}</p>
                    <p class='promo-subtitle'>Valor por cuota según plan</p>
                </div>
            """, unsafe_allow_html=True)

        with col_efectivo:
            st.markdown(f"""
                <div class="widget-3d-grad">
                    <p class='widget-title'>💎 PAGO EFECTIVO (OFICINA)</p>
                    <p class='widget-value' style='color: #2e7d32;'>${val_contado * 0.9:,.0f}</p>
                    <p class='promo-subtitle'>Beneficio especial del 10% OFF</p>
                </div>
            """, unsafe_allow_html=True)

        st.divider()
        with st.expander("📊 Ver tabla comparativa completa"):
            st.table(df.set_index('Programa'))
    else:
        st.error(f"Archivo no encontrado en {path_tarifas}")

# --- VISTA ESTÁNDAR ---
else:
    st.title(opcion)
    path_info = f"data/{folder}/{limpiar_nombre_archivo(opcion)}"
    if os.path.exists(path_info):
        df_info = pd.read_csv(path_info)
        for _, row in df_info.iterrows():
            with st.expander(f"🔹 {row['Titulo']}", expanded=True):
                st.write(row['Contenido'])
    else:
        st.error(f"Contenido no disponible para {destino}.")

st.sidebar.divider()
st.sidebar.caption("Serrano Turismo - 29 años de trayectoria")
