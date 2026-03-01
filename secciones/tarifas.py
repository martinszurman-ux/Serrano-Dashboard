import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    # 1. INICIALIZACIÓN
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    # Lógica de Temporada para San Pedro
    archivo_nombre = "tarifas_y_formas_de_pago.csv"
    if destino == "San Pedro":
        st.markdown("<h4 style='margin-bottom:0px;'>🗓️ Temporada</h4>", unsafe_allow_html=True)
        temporada = st.segmented_control(
            "Temporada", options=["2026", "2027"], default="2026", label_visibility="collapsed"
        )
        archivo_nombre = f"tarifas_{temporada}.csv"
        suffix = temporada
        session_key = f"sel_index_{folder}_{suffix}"
        header_path = f"data/{folder}/tarifariosanpedro.jpg"
    else:
        session_key = f"sel_index_{folder}"
        header_path = f"data/{folder}/tarifas_y_formas_header.png"
    
    if session_key not in st.session_state:
        st.session_state[session_key] = 0

    # 2. ESTILOS CSS (MEJORADOS Y RESPONSIVOS)
    st.markdown("""
        <style>
        [data-testid="stImage"] { margin-top: -55px; margin-bottom: -20px; }
        
        /* Contenedores Base */
        .contenedor-selector-pago { display: flex; flex-direction: column; align-items: center; margin: 10px 0; }
        
        /* Diseño de Tarjetas Itinerario (Solo para Web) */
        .plan-card-container { 
            border-radius: 12px; padding: 10px; background: #E8E8E8; 
            border: 1px solid #d1d1d1; text-align: center; min-height: 110px; 
            display: flex; flex-direction: column; justify-content: center; 
            align-items: center; transition: all 0.3s ease; 
        }
        .selected-plan { border: 2px solid #4A90E2 !important; background-color: #ffffff !important; box-shadow: 0px 2px 8px rgba(0,0,0,0.05); }
        .header-content { display: flex; justify-content: center; align-items: center; gap: 8px; }
        .day-number { color: #4A90E2; font-size: 2.2rem; font-weight: 900; line-height: 1; }
        .transport-icon { font-size: 1.5rem; }
        .day-text { color: #495057; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; }
        
        /* Hero Widget Responsivo */
        .hero-payment-card { 
            background: linear-gradient(145deg, #ffffff, #f0f2f6); 
            border-radius: 20px; padding: 20px; text-align: center; 
            border: 1px solid #e0e4e8; box-shadow: 10px 10px 30px #d9dbe0; 
            max-width: 400px; margin: 15px auto; 
        }
        .hero-value { 
            color: #1a1c1e; font-size: 2.5rem; font-weight: 900; 
            background: -webkit-linear-gradient(#1a1c1e, #4A90E2); 
            -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
        }

        /* Ocultar elementos en Mobile vía Media Queries si fuera necesario, 
           pero aquí usaremos lógica de Python para mayor control */
        </style>
    """, unsafe_allow_html=True)

    # --- 3. CARGA DE DATOS ---
    path_tarifas = f"data/{folder}/{archivo_nombre}"
    if not os.path.exists(path_tarifas):
        st.error("Archivo no encontrado"); return

    df = pd.read_csv(path_tarifas)
    df.columns = df.columns.str.strip()
    planes = df['Programa'].tolist()

    # --- 4. DETECCIÓN DE MOBILE / SELECCIÓN DE ITINERARIO ---
    st.markdown("<h4 style='margin-bottom:10px;'>📅 Itinerario</h4>", unsafe_allow_html=True)
    
    # Usamos columnas. En mobile, Streamlit las apila, pero podemos usar 
    # un selectbox para que sea más prolijo si detectamos que hay muchos planes.
    if len(planes) > 3: 
        # VERSION MOBILE (Dropdown)
        opcion_itinerario = st.selectbox(
            "Seleccioná tu plan", 
            options=range(len(planes)), 
            format_func=lambda x: planes[x],
            index=st.session_state[session_key],
            label_visibility="collapsed"
        )
        if opcion_itinerario != st.session_state[session_key]:
            st.session_state[session_key] = opcion_itinerario
            st.rerun()
    else:
        # VERSION WEB (Tarjetas)
        cols_p = st.columns(len(planes))
        for i, plan in enumerate(planes):
            partes = plan.split(' ', 1)
            numero, resto = partes[0], (partes[1] if len(partes) > 1 else "")
            icono = "🚌" if "bus" in plan.lower() else "✈️"
            with cols_p[i]:
                es_activo = st.session_state[session_key] == i
                clase_card = "selected-plan" if es_activo else ""
                st.markdown(f"""
                <div class="plan-card-container {clase_card}">
                    <div class="header-content"><span class="day-number">{numero}</span><span class="transport-icon">{icono}</span></div>
                    <div class="day-text">{resto}</div>
                </div>
                """, unsafe_allow_html=True)
                if st.button("Elegir", key=f"btn_{i}", use_container_width=True):
                    st.session_state[session_key] = i
                    st.rerun()

    # --- 5. LOGICA DE PRECIOS ---
    v = df.iloc[st.session_state[session_key]]
    
    def clean_val(val):
        if pd.isna(val) or val == '': return 0.0
        try: return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())
        except: return 0.0

    # --- SECCIÓN PAGOS ---
    excluir = ['Programa', 'Contado', 'Valor del Viaje', 'Costo Total']
    opciones_cuotas = ["1 Pago"] + [c.replace('_', ' ') for c in df.columns if c not in excluir]
    
    st.markdown('<div class="contenedor-selector-pago">', unsafe_allow_html=True)
    st.markdown('<p class="instruccion-pago">Plan de pago:</p>', unsafe_allow_html=True)
    cuota_sel = st.pills("Cuotas", options=opciones_cuotas, default=opciones_cuotas[1], label_visibility="collapsed", key="pills_pago")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- HERO WIDGET ---
    if cuota_sel == "1 Pago":
        m_display = f"${clean_val(v['Contado']):,.0f}"
        label_cuota = "Pago Único"
    else:
        m_display = f"${clean_val(v[cuota_sel.replace(' ', '_')]):,.0f}"
        label_cuota = f"Cuota ({cuota_sel})"

    st.markdown(f"""
        <div class="hero-payment-card">
            <p style="color: #6c757d; font-size: 0.8rem; font-weight: 700; text-transform: uppercase;">Monto a abonar</p>
            <p class="hero-value">{m_display}</p>
            <p style="color: #4A90E2; font-size: 1rem; font-weight: 600;">💳 {label_cuota}</p>
        </div>
    """, unsafe_allow_html=True)

    # Beneficio e Info Final
    st.info("🎁 **Beneficio 10% OFF:** Pagando del 1 al 10 en efectivo en Serrano.")
    
    with st.expander("Ver tabla completa"):
        st.dataframe(df)

    st.markdown("<h5 style='margin-top:10px;'>🛡️ Servicios Incluidos</h5>", unsafe_allow_html=True)
    st.caption("✓ Liberados • ✓ Descuentos • ✓ Seguro Médico • ✓ Coordinación")
