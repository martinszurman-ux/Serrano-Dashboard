import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. Configuración de página y Estética Profesional
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# --- ESTILOS CSS AVANZADOS (3D, Degradados, Neumorfismo e Impresión) ---
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
        overflow: hidden;
    }
    .header-text-overlay {
        color: white; font-size: 2.2rem; font-weight: 800; text-transform: uppercase; letter-spacing: 2px;
    }

    /* Estilo para impresión */
    @media print {
        header, [data-testid="stSidebar"], .stButton, .no-print {
            display: none !important;
        }
        .main .block-container {
            padding: 0 !important;
        }
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
    st.markdown("""
    <div style="font-size: 0.8rem; color: #6c757d;">
    <b>CABA:</b> Av. Rivadavia 4532<br>
    <b>Leloir:</b> Del Cimarrón 1846<br>
    <b>WA:</b> (011) 5609-6283
    </div>
    """, unsafe_allow_html=True)

# Función de utilidad para limpiar nombres
def limpiar_nombre_archivo(texto):
    reemplazos = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", " ": "_"}
    texto = texto.lower()
    for original, reemplazo in reemplazos.items(): 
        texto = texto.replace(original, reemplazo)
    return texto + ".csv"

# --- SECCIÓN: SOLICITUD DE ADHESIÓN (RECUPERADA) ---
if opcion == "Solicitud de Adhesión":
    st.image(LOGO_URL, width=200)
    st.title("📄 Solicitud de Ingreso / Adhesión")
    st.subheader("Ficha del Cliente / Pasajero")

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
            f_nac_alumno = st.date_input("Fecha de Nacimiento", min_value=datetime(2000,1,1))
        with c_al2:
            nom_alumno = st.text_input("Nombres Alumno")
            dni_venc = st.date_input("Vencimiento de DNI")
            nacionalidad = st.text_input("Nacionalidad", value="Argentina")
        
        sexo = st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

        st.markdown("#### Domicilio y Contacto")
        c_dom1, c_dom2, c_dom3 = st.columns([2, 1, 1])
        with c_dom1:
            domicilio = st.text_input("Domicilio")
        with c_dom2:
            cp = st.text_input("Código Postal")
        with c_dom3:
            localidad = st.text_input("Localidad")
        
        c_dom4, c_dom5 = st.columns(2)
        with c_dom4:
            provincia = st.text_input("Provincia", value="Buenos Aires")
        with c_dom5:
            telefono = st.text_input("Teléfono (Cod. Área + Número)")

        st.markdown("#### Datos de los Padres / Tutores")
        c_p1, c_p2 = st.columns(2)
        with c_p1:
            padre_nom = st.text_input("Nombre y Apellido Padre / Tutor (1)")
            padre_dni = st.text_input("DNI Padre")
        with c_p2:
            madre_nom = st.text_input("Nombre y Apellido Madre / Tutor (2)")
            madre_dni = st.text_input("DNI Madre")
        
        email_padres = st.text_input("E-mail de contacto (Madre o Padre)")

        st.markdown("#### Plan de Pago Elegido")
        plan_pago = st.radio("Seleccione el plan de pago acordado:", 
                             ["PLAN 1: Cuotas mensuales según contrato", 
                              "PLAN 2: Pago contado (dentro de los 30 días)", 
                              "PLAN 3: Plan personalizado", 
                              "PLAN 4: Plan especial grupo", 
                              "OTROS: Ver observaciones"], horizontal=False)

        observaciones = st.text_area("Observaciones")

        st.markdown("---")
        st.write("**Declaración Jurada:** Declaro bajo juramento que los datos aquí volcados son absolutamente exactos y acepto, para la cancelación de los servicios a prestar por SERRANO TURISMO, el plan de pagos mencionado anteriormente. Declaro conocer todas y cada una de las condiciones del contrato suscripto.")
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.divider()
            st.caption("Firma del Padre/Madre/Tutor")
        with col_f2:
            st.divider()
            st.caption("Aclaración y DNI")

        submitted = st.form_submit_button("Finalizar y Preparar para Imprimir")
        
        if submitted:
            st.success("Formulario completado. Use el botón de abajo para imprimir.")

    # Botón de impresión
    st.button("🖨️ Enviar a Imprimir Formulario", on_click=lambda: st.write('<script>window.print();</script>', unsafe_allow_html=True))

# --- SECCIÓN: TARIFAS ---
elif opcion == "Tarifas y Formas de Pago":
    st.markdown(f'<div class="header-container"><div class="header-text-overlay">TARIFAS {destino.upper()}</div></div>', unsafe_allow_html=True)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        
        st.write("### 🎯 Seleccioná tu Plan de Viaje")
        
        if 'plan_seleccionado' not in st.session_state:
            st.session_state.plan_seleccionado = df['Programa'].iloc[0]

        planes = df['Programa'].unique()
        iconos = ["🚌", "✈️", "🌴", "🏛️", "⛰️", "🚢"] # Iconos genéricos por si hay muchos planes
        
        cols = st.columns(len(planes))
        for i, p_name in enumerate(planes):
            with cols[i]:
                es_sel = "plan-selected" if st.session_state.plan_seleccionado == p_name else ""
                icon = iconos[i] if i < len(iconos) else "📍"
                
                st.markdown(f"""
                    <div class="plan-card-box {es_sel}">
                        <div style="font-size: 2.5rem;">{icon}</div>
                        <div style="font-weight: bold; font-size: 0.9rem; margin-top:10px;">{p_name}</div>
                    </div>
                """, unsafe_allow_html=True)
                
                if st.button("Seleccionar", key=f"btn_{p_name}"):
                    st.session_state.plan_seleccionado = p_name
                    st.rerun()

        v = df[df['Programa'] == st.session_state.plan_seleccionado].iloc[0]
        st.divider()
        
        col1, col2, col3 = st.columns(3)

        def to_num(val):
            return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())

        with col1:
            st.markdown('<div class="widget-3d-grad">', unsafe_allow_html=True)
            st.markdown("<p class='widget-title'>OPCIONES DE PAGO</p>", unsafe_allow_html=True)
            opciones_cols = [c.replace('_', ' ') for c in df.columns if c not in ['Programa', 'Contado']]
            cuota_sel = st.pills("Planes:", options=opciones_cols, default=opciones_cols[0], label_visibility="collapsed", key="pills_pago")
            st.markdown('</div>', unsafe_allow_html=True)

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

# --- VISTA ESTÁNDAR PARA EL RESTO ---
else:
    st.title(opcion)
    path_info = f"data/{folder}/{limpiar_nombre_archivo(opcion)}"
    if os.path.exists(path_info):
        df_info = pd.read_csv(path_info)
        for _, row in df_info.iterrows():
            with st.expander(f"🔹 {row['Titulo']}", expanded=True):
                st.write(row['Contenido'])
                if 'Destacado' in row: st.info(row['Destacado'])
    else:
        st.error(f"Contenido no disponible para {destino}.")

st.sidebar.divider()
st.sidebar.caption("Serrano Turismo - 29 años de trayectoria")
