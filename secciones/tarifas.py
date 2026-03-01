import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    # 1. INICIALIZACIÓN
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    archivo_nombre = "tarifas_y_formas_de_pago.csv"
    
    if destino == "San Pedro":
        st.markdown("<h4 style='margin-bottom:0px;'>🗓️ Temporada del viaje</h4>", unsafe_allow_html=True)
        temporada = st.segmented_control("Temporada", options=["2026", "2027"], default="2026", label_visibility="collapsed")
        archivo_nombre = f"tarifas_{temporada}.csv"
        suffix = temporada
        header_path = f"data/{folder}/tarifariosanpedro.jpg"
    else:
        suffix = ""
        header_path = f"data/{folder}/tarifas_y_formas_header.png"
    
    session_key = f"sel_index_{folder}_{suffix}"
    if session_key not in st.session_state:
        st.session_state[session_key] = 0

    # 2. ESTILOS CSS (LÓGICA RESPONSIVE)
    st.markdown("""
        <style>
        /* Ajustes generales */
        [data-testid="stImage"] { margin-top: -55px; margin-bottom: -20px; }
        
        /* --- SELECTOR DE PAGO --- */
        .contenedor-selector-pago { display: flex; flex-direction: column; align-items: center; margin: 10px 0; }
        div[data-testid="stPills"] > div { justify-content: center !important; display: flex !important; gap: 6px; }

        /* --- TARJETAS (VERSION WEB) --- */
        .plan-card-container { 
            border-radius: 12px; padding: 10px; background: #E8E8E8; 
            border: 1px solid #d1d1d1; text-align: center; min-height: 110px; 
            display: flex; flex-direction: column; justify-content: center; align-items: center; 
        }
        .selected-plan { border: 2px solid #4A90E2 !important; background-color: #ffffff !important; }
        .day-number { color: #4A90E2; font-size: 2.2rem; font-weight: 900; line-height: 1; }
        .transport-icon { font-size: 1.5rem; }
        .day-text { color: #495057; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; }

        /* --- HERO WIDGET --- */
        .hero-payment-card { 
            background: linear-gradient(145deg, #ffffff, #f0f2f6); 
            border-radius: 20px; padding: 20px; text-align: center; 
            border: 1px solid #e0e4e8; box-shadow: 10px 10px 30px #d9dbe0; 
            max-width: 400px; margin: 15px auto; 
        }
        .hero-value { 
            color: #1a1c1e; font-size: 2.8rem; font-weight: 900; 
            background: -webkit-linear-gradient(#1a1c1e, #4A90E2); 
            -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
        }

        /* --- LÓGICA DE VISIBILIDAD (HACK) --- */
        /* Por defecto ocultamos el selector mobile en Web */
        div[data-testid="stSelectbox"] { display: block; } 
        
        /* Media Query: Si la pantalla es mayor a 768px (Desktop) */
        @media (min-width: 768px) {
            .mobile-only { display: none !important; }
            .desktop-only { display: block !important; }
        }

        /* Media Query: Si la pantalla es menor a 768px (Mobile) */
        @media (max-width: 767px) {
            .desktop-only { display: none !important; }
            .mobile-only { display: block !important; }
        }
        </style>
    """, unsafe_allow_html=True)

    # --- 3. CARGA DE DATOS ---
    path_tarifas = f"data/{folder}/{archivo_nombre}"
    if not os.path.exists(path_tarifas):
        st.error("Archivo no encontrado"); return

    df = pd.read_csv(path_tarifas)
    df.columns = df.columns.str.strip()
    planes = df['Programa'].tolist()

    # --- 4. SELECTOR DE ITINERARIO DUAL ---
    st.markdown("<h4 style='margin-bottom:10px;'>📅 Itinerario</h4>", unsafe_allow_html=True)

    # A. VERSION MOBILE (Dropdown)
    # Envolvemos el selectbox en un div con clase mobile-only
    st.markdown('<div class="mobile-only">', unsafe_allow_html=True)
    opcion_mobile = st.selectbox(
        "Seleccioná tu plan", 
        options=range(len(planes)), 
        format_func=lambda x: planes[x],
        index=st.session_state[session_key],
        key=f"mobile_sel_{suffix}"
    )
    if opcion_mobile != st.session_state[session_key]:
        st.session_state[session_key] = opcion_mobile
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # B. VERSION DESKTOP (Tarjetas)
    # Envolvemos las tarjetas en un div con clase desktop-only
    st.markdown('<div class="desktop-only">', unsafe_allow_html=True)
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
                    <div style="display:flex; align-items:center; gap:8px;">
                        <span class="day-number">{numero}</span>
                        <span class="transport-icon">{icono}</span>
                    </div>
                    <div class="day-text">{resto}</div>
                </div>
            """, unsafe_allow_html=True)
            if st.button("Elegir", key=f"btn_web_{i}_{suffix}", use_container_width=True):
                st.session_state[session_key] = i
                st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    # --- 5. LOGICA DE PRECIOS Y HERO ---
    v = df.iloc[st.session_state[session_key]]
    def clean_val(val):
        try: return float(str(val).replace('$', '').replace('.', '').replace(',', '').strip())
        except: return 0.0

    excluir = ['Programa', 'Contado', 'Valor del Viaje', 'Costo Total']
    opciones_cuotas = ["1 Pago"] + [c.replace('_', ' ') for c in df.columns if c not in excluir]
    
    st.markdown('<div class="contenedor-selector-pago">', unsafe_allow_html=True)
    st.markdown('<p class="instruccion-pago">Plan de pago:</p>', unsafe_allow_html=True)
    cuota_sel = st.pills("Cuotas", options=opciones_finales, default=opciones_finales[1], label_visibility="collapsed", key=f"pills_{suffix}")
    st.markdown('</div>', unsafe_allow_html=True)

    # Hero Widget
    m_val = v['Contado'] if cuota_sel == "1 Pago" else v[cuota_sel.replace(' ', '_')]
    m_display = f"${clean_val(m_val):,.0f}"

    st.markdown(f"""
        <div class="hero-payment-card">
            <p style="color: #6c757d; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; margin-bottom:5px;">Monto a abonar</p>
            <p class="hero-value">{m_display}</p>
            <p style="color: #4A90E2; font-size: 1rem; font-weight: 600; margin-top:5px;">💳 {cuota_sel}</p>
        </div>
    """, unsafe_allow_html=True)

    # Beneficio e Info Final
    st.info("🎁 **Beneficio 10% OFF:** Pagando del 1 al 10 en efectivo en Serrano.")
    
    with st.expander("🛡️ Ver servicios incluidos y tabla completa"):
        st.dataframe(df)
        st.write("- Liberados para acompañantes")
        st.write("- Seguro médico incluido")
