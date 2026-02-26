import streamlit as st
import pandas as pd
import os
from datetime import datetime

# 1. Configuración de página y Estética Profesional
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

# --- ESTILOS CSS AVANZADOS ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    
    .widget-3d-grad {
        background: linear-gradient(145deg, #f0f0f0, #ffffff);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        border: 1px solid #e0e0e0;
        box-shadow: 8px 8px 16px #d1d1d1, -8px -8px 16px #ffffff;
        margin-bottom: 15px;
    }
    
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
        .print-only {
            display: block !important;
        }
    }

    .text-legal {
        font-size: 0.75rem;
        line-height: 1.3;
        color: #333;
        text-align: justify;
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

# --- SECCIÓN: SOLICITUD DE ADHESIÓN ---
if opcion == "Solicitud de Adhesión":
    st.image(LOGO_URL, width=180)
    st.markdown("<h2 style='text-align: center; margin-bottom: 0;'>SOLICITUD DE INGRESO</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-weight: bold;'>Ficha del Cliente / Pasajero</p>", unsafe_allow_html=True)

    with st.form("formulario_adhesion"):
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            fecha_doc = st.date_input("Fecha", datetime.now())
        with col2:
            cliente_n = st.text_input("Cliente N°")
        with col3:
            contrato = st.text_input("Contrato")
        with col4:
            liberado = st.text_input("% L.O.")

        c1, c2 = st.columns(2)
        with c1:
            colegio = st.text_input("Colegio / Instituto")
        with c2:
            año_div = st.text_input("Año y Div.")

        st.markdown("---")
        c3, c4 = st.columns(2)
        with c3:
            ap_alumno = st.text_input("Apellido")
            dni_alumno = st.text_input("D.N.I. Nº")
            f_nac_alumno = st.date_input("Fecha de Nacimiento", min_value=datetime(2000,1,1))
        with c4:
            nom_alumno = st.text_input("Nombres")
            nacionalidad = st.text_input("Nacionalidad", value="Argentina")
            sexo = st.radio("Sexo", ["Masculino", "Femenino", "X"], horizontal=True)

        c5, c6, c7 = st.columns([2, 1, 1])
        with c5:
            domicilio = st.text_input("Domicilio")
        with c6:
            cp = st.text_input("Código Postal")
        with c7:
            localidad = st.text_input("Localidad")
        
        c8, c9 = st.columns(2)
        with c8:
            provincia = st.text_input("Provincia")
        with c9:
            telefono = st.text_input("Teléfono Cod. Área")

        st.markdown("---")
        c10, c11 = st.columns(2)
        with c10:
            padre_nom = st.text_input("Madre / Padre / Tutor (1)")
            padre_dni = st.text_input("D.N.I. (1)")
        with c11:
            madre_nom = st.text_input("Madre / Padre / Tutor (2)")
            madre_dni = st.text_input("D.N.I. (2)")
        
        email = st.text_input("E-mail:")
        st.caption("En caso de no poseer o no utilizar toda la información de caracter personal será enviada al e-mail del representante del grupo.")

        st.markdown("#### OBSERVACIONES")
        observaciones = st.text_area("", label_visibility="collapsed")

        st.markdown("---")
        st.markdown("""
        <div class="text-legal">
        Declaro bajo juramento que los datos aquí volcados son absolutamente exactos y acepto, para la cancelación de los servicios 
        a prestar por <b>TRANSPORTE SERRANO TURISMO RECREATIVO</b>, el plan de pagos que figura en la solicitud de reserva mencionada 
        anteriormente, denominado: (Por favor coloque una X en el plan elegido)
        </div>
        """, unsafe_allow_html=True)
        
        plan_pago = st.radio("", 
                             ["PLAN 1", "PLAN 2", "PLAN 3", "PLAN 4", "OTROS"], 
                             horizontal=True, label_visibility="collapsed")

        st.markdown("""
        <div class="text-legal">
        <b>PLAN 1:</b> Las cuotas deberán abonarse mensualmente tal como se indicó en el contrato.<br>
        <b>PLAN 2:</b> Los planes al contado deberán abonarse dentro de los 30 días de haberse firmado el contrato.<br><br>
        Además declaro conocer todas y cada una de las condiciones del contrato suscripto por mi y/u otro representante del contingente de referencia.<br><br>
        <b>NOTA:</b> De no marcarse ningún plan de pago, su chequera se emitirá como PLAN CUOTAS (PLAN 1). Las cuotas se abonan del 1 al 10 de cada mes. 
        Pasada dicha fecha, la misma sufrirá el recargo administrativo correspondiente. La empresa no se responsabiliza por la falta de entrega de la chequera 
        si los datos de esta ficha son erróneos o están incompletos.
        <br><br>
        <b>IMPORTANTE:</b> Los servicios cuentan con Seguro de Caución (Ley 25.599 / 26.208) de la compañía <b>ALBA CAUCION</b>. 
        Serrano Turismo Recreativo Leg. 12.441 disp. 1018/05.
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            st.divider()
            st.caption("Firma del Padre/Madre/Tutor")
        with col_f2:
            st.divider()
            st.caption("Aclaración y DNI")

        submitted = st.form_submit_button("Finalizar y Preparar para Imprimir")

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
        iconos = ["🚌", "✈️", "🌴", "🏛️", "⛰️"]
        
        cols = st.columns(len(planes))
        for i, p_name in enumerate(planes):
            with cols[i]:
                es_sel = "plan-selected" if st.session_state.plan_seleccionado == p_name else ""
                icon = iconos[i] if i < len(iconos) else "📍"
                st.markdown(f'<div class="plan-card-box {es_sel}"><div style="font-size: 2.5rem;">{icon}</div><div style="font-weight: bold; font-size: 0.9rem; margin-top:10px;">{p_name}</div></div>', unsafe_allow_html=True)
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
            st.markdown(f'<div class="widget-3d-grad"><p class="widget-title">MONTO {cuota_sel.upper()}</p><p class="widget-value">${val_cuota:,.0f}</p><p class="promo-subtitle">Valor de cuota fija</p></div>', unsafe_allow_html=True)

        with col3:
            st.markdown(f'<div class="widget-3d-grad"><p class="widget-title">💎 PAGO EFECTIVO (OFICINA)</p><p class="widget-value" style="color: #2e7d32;">${val_contado * 0.9:,.0f}</p><p class="promo-subtitle">Beneficio 10% OFF aplicado</p></div>', unsafe_allow_html=True)

        st.divider()
        with st.expander("📊 Ver comparativa completa"):
            st.table(df.set_index('Programa'))
    else:
        st.error("Base de datos de tarifas no encontrada.")

# --- VISTA ESTÁNDAR ---
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
        st.error(f"Contenido no disponible.")

st.sidebar.divider()
st.sidebar.caption("Serrano Turismo - 29 años de trayectoria")
