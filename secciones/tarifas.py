import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    # 1. INICIALIZACIÓN DE SESIÓN Y CARPETAS
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    # Lógica para San Pedro: Selección de año
    archivo_nombre = "tarifas_y_formas_de_pago.csv"
    if destino == "San Pedro":
        st.markdown("<h4 style='margin-bottom:0px;'>🗓️ Temporada del viaje</h4>", unsafe_allow_html=True)
        temporada = st.segmented_control(
            "Temporada", 
            options=["Temporada 2026", "Temporada 2027"], 
            default="Temporada 2026",
            label_visibility="collapsed"
        )
        archivo_nombre = "tarifas_2026.csv" if temporada == "Temporada 2026" else "tarifas_2027.csv"
        suffix = "2026" if temporada == "Temporada 2026" else "2027"
        session_key = f"sel_index_{folder}_{suffix}"
        header_path = f"data/{folder}/tarifariosanpedro.jpg"
    else:
        session_key = f"sel_index_{folder}"
        header_path = f"data/{folder}/tarifas_y_formas_header.png"
    
    if session_key not in st.session_state:
        st.session_state[session_key] = 0

    # 2. ESTILOS CSS (VERSION COMPACTA)
    st.markdown("""
        <style>
        [data-testid="stImage"] { margin-top: -55px; margin-bottom: -20px; }
        .contenedor-selector-pago { display: flex; flex-direction: column; align-items: center; justify-content: center; width: 100%; margin: 10px 0; }
        div[data-testid="stPills"] > div { justify-content: center !important; display: flex !important; gap: 6px; }
        .instruccion-pago { text-align: center; font-weight: 700; color: #495057; margin-bottom: 8px; font-size: 0.95rem; }
        
        /* Itinerarios más chicos */
        .plan-card-container { border-radius: 12px; padding: 10px; background: #E8E8E8; border: 1px solid #d1d1d1; text-align: center; min-height: 110px; display: flex; flex-direction: column; justify-content: center; align-items: center; margin-bottom: 5px; transition: all 0.3s ease; }
        .selected-plan { border: 2px solid #4A90E2 !important; background-color: #ffffff !important; box-shadow: 0px 2px 8px rgba(0,0,0,0.05); }
        .header-content { display: flex; justify-content: center; align-items: center; gap: 8px; width: 100%; }
        .day-number { color: #4A90E2; font-size: 2.2rem; font-weight: 900; line-height: 1; margin: 0; }
        .transport-icon { font-size: 1.5rem; line-height: 1; margin: 0; }
        .day-text { color: #495057; font-size: 0.7rem; font-weight: 700; text-transform: uppercase; margin-top: 5px; }
        
        /* Hero Widget más compacto */
        .hero-payment-card { background: linear-gradient(145deg, #ffffff, #f0f2f6); border-radius: 20px; padding: 20px 30px; text-align: center; border: 1px solid #e0e4e8; box-shadow: 10px 10px 30px #d9dbe0; max-width: 400px; margin: 15px auto; transition: all 0.5s ease; cursor: default; }
        .hero-payment-card:hover { transform: translateY(-5px); }
        .hero-label { color: #6c757d; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; margin-bottom: 5px; }
        .hero-value { color: #1a1c1e; font-size: 2.8rem; font-weight: 900; margin: 0; line-height: 1; background: -webkit-linear-gradient(#1a1c1e, #4A90E2); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .hero-subtitle { color: #4A90E2; font-size: 1rem; font-weight: 600; margin-top: 5px; }
        
        /* Beneficio más discreto */
        .beneficio-box { max-width: 600px; margin: 15px auto; padding: 12px; background-color: #f0f7ff; border-radius: 10px; border: 1px dashed #4A90E2; }
        
        .styled-table th { background-color: #333333 !important; color: white !important; font-size: 0.8rem; padding: 5px !important; }
        .styled-table td { font-size: 0.8rem; padding: 5px !important; }
        </style>
    """, unsafe_allow_html=True)

    # --- 3. CARGA DE IMAGEN ---
    if os.path.exists(header_path):
        _, col_img, _ = st.columns([1.5, 3, 1.5])
        with col_img: st.image(header_path)

    # --- 4. CARGA DE DATOS ---
    path_tarifas = f"data/{folder}/{archivo_nombre}"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        df.columns = df.columns.str.strip()
        
        def clean_val(val):
            if pd.isna(val) or val == '': return 0.0
            clean = str(val).replace('$', '').replace('.', '').replace(',', '').replace('s', '').strip()
            try: return float(clean)
            except: return 0.0

        # --- SECCIÓN 1: ITINERARIO ---
        st.markdown("<h4 style='margin-bottom:10px;'>📅 Itinerario</h4>", unsafe_allow_html=True)
        planes = df['Programa'].tolist()
        cols_p = st.columns(len(planes))
        
        for i, plan in enumerate(planes):
            partes = plan.split(' ', 1)
            numero = partes[0]
            resto = partes[1] if len(partes) > 1 else ""
            icono = "🚌" if "bus" in plan.lower() else "✈️"
            
            with cols_p[i]:
                es_activo = st.session_state[session_key] == i
                clase_card = "selected-plan" if es_activo else ""
                card_html = f"""
                <div class="plan-card-container {clase_card}">
                    <div class="header-content"><span class="day-number">{numero}</span><span class="transport-icon">{icono}</span></div>
                    <div class="day-text">{resto}</div>
                </div>
                """
                st.markdown(card_html, unsafe_allow_html=True)
                if st.button("Elegir", key=f"btn_{folder}_{i}_{archivo_nombre}", use_container_width=True):
                    st.session_state[session_key] = i
                    st.rerun()

        idx = st.session_state[session_key]
        if idx >= len(df): idx = 0
        v = df.iloc[idx]

        # --- SECCIÓN 2: OPCIONES DE PAGO ---
        excluir = ['Programa', 'Contado', 'Valor del Viaje', 'Costo Total', 'Valor del viaje']
        opciones_cuotas = [c.replace('_', ' ') for c in df.columns if c not in excluir]
        opciones_finales = ["1 Pago"] + opciones_cuotas

        st.markdown('<div class="contenedor-selector-pago">', unsafe_allow_html=True)
        st.markdown('<p class="instruccion-pago">Plan de pago:</p>', unsafe_allow_html=True)
        cuota_sel = st.pills("Cuotas", options=opciones_finales, default=opciones_finales[1] if len(opciones_finales) > 1 else opciones_finales[0], label_visibility="collapsed", key=f"pills_{folder}_{archivo_nombre}")
        if not cuota_sel: cuota_sel = opciones_finales[1]
        st.markdown('</div>', unsafe_allow_html=True)

        # --- SECCIÓN 3: HERO WIDGET ---
        if cuota_sel == "1 Pago":
            m_display = f"${clean_val(v['Contado']):,.0f}"
            label_cuota = "Pago Único"
        else:
            c_db = cuota_sel.replace(' ', '_')
            m_display = f"${clean_val(v[c_db]):,.0f}"
            label_cuota = f"Cuota ({cuota_sel})"

        st.markdown(f"""
            <div class="hero-payment-card">
                <p class="hero-label">A abonar</p>
                <p class="hero-value">{m_display}</p>
                <p class="hero-subtitle">💳 {label_cuota}</p>
            </div>
        """, unsafe_allow_html=True)

        # Beneficio Serrano Compacto
        st.markdown(f"""
            <div class='beneficio-box'>
                <p style='font-size: 0.85rem; color: #333; text-align: center; margin: 0;'>
                    🎁 <b>¡10% OFF Serrano!</b> Pagando del 1 al 10 en efectivo (aplicado en última cuota).
                </p>
            </div>
        """, unsafe_allow_html=True)

        # --- SECCIÓN 4: TABLA Y BENEFICIOS ---
        with st.expander("Comparativa de tarifas"):
            df_format = df.copy()
            cols_a_borrar = [c for c in df_format.columns if 'valor del' in c.lower() or 'costo total' in c.lower()]
            df_format = df_format.drop(columns=cols_a_borrar)
            if 'Contado' in df_format.columns: df_format = df_format.rename(columns={'Contado': '1 Pago'})
            df_format.columns = [c.replace('_', ' ') for c in df_format.columns]
            for col in df_format.columns.drop('Programa'): df_format[col] = df_format[col].apply(clean_val)
            st.markdown('<div class="styled-table">', unsafe_allow_html=True)
            st.table(df_format.set_index('Programa').style.format("$ {:,.0f}"))
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("<h5 style='margin-bottom:5px;'>🛡️ Servicios Incluidos</h5>", unsafe_allow_html=True)
        beneficios = ["Liberados para niños.", "Descuentos por pago.", "Opciones personalizadas.", "Ayudas incluidas.", "Fiesta de Egresados.", "Descuentos Camperas."]
        c1, c2 = st.columns(2)
        for i, b in enumerate(beneficios):
            with c1 if i % 2 == 0 else c2:
                st.markdown(f'<p style="font-size:0.8rem; margin-bottom:2px; color:#495057;">✓ {b}</p>', unsafe_allow_html=True)
    else:
        st.warning(f"No se encontró el archivo en data/{folder}/")
