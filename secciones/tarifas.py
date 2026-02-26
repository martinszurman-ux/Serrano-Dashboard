import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    # 1. INICIALIZACIÓN
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    session_key = f"sel_index_{folder}"
    
    if session_key not in st.session_state:
        st.session_state[session_key] = 0

    # 2. ESTILOS CSS (Diseño Hero, Cards e Interactividad)
    st.markdown("""
        <style>
        /* Mover el contenido hacia arriba */
        [data-testid="stImage"] {
            margin-top: -45px;
            margin-bottom: -10px;
        }
        
        /* Centrar dinámicamente los botones de st.pills */
        div[data-testid="stPills"] {
            display: flex;
            justify-content: center;
            width: 100%;
        }
        div[data-testid="stPills"] > div {
            justify-content: center;
        }

        /* Widgets Superiores */
        .plan-card-container {
            border-radius: 15px; 
            padding: 20px; 
            background: #D9D9D9;
            border: 1px solid #ccc; 
            text-align: center;
            min-height: 140px; 
            display: flex; 
            flex-direction: column;
            justify-content: center; 
            align-items: center; 
            margin-bottom: 10px;
            transition: all 0.3s ease;
        }
        
        .selected-plan { 
            border: 2px solid #d32f2f !important; 
            background-color: #ffffff !important;
            transform: scale(1.05);
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        }
        
        .day-number { color: #d32f2f; font-size: 2.8rem; font-weight: 900; line-height: 1; }
        .transport-icon { font-size: 1.6rem; margin-left: 8px; }
        .day-text { color: #495057; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; }

        /* MEGA WIDGET HERO CON EFECTO HOVER */
        .hero-payment-card {
            background: linear-gradient(145deg, #ffffff, #f0f2f6);
            border-radius: 24px;
            padding: 40px;
            text-align: center;
            border: 1px solid #e0e4e8;
            box-shadow: 15px 15px 40px #d9dbe0, -15px -15px 40px #ffffff;
            max-width: 500px;
            margin: 20px auto;
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            cursor: default;
        }

        .hero-payment-card:hover {
            transform: translateY(-12px) scale(1.03);
            box-shadow: 25px 25px 60px #c0c2c7, -15px -15px 40px #ffffff;
            background: linear-gradient(145deg, #ffffff, #e6e9ef);
        }

        .hero-label { 
            color: #6c757d; font-size: 0.9rem; font-weight: 700; 
            text-transform: uppercase; letter-spacing: 1.5px;
            margin-bottom: 10px;
        }
        .hero-value { 
            color: #1a1c1e; font-size: 4rem; font-weight: 900; margin: 0;
            line-height: 1;
            background: -webkit-linear-gradient(#1a1c1e, #4a4d52);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .hero-subtitle { color: #d32f2f; font-size: 1.2rem; font-weight: 600; margin-top: 10px; }

        .styled-table th {
            background-color: #333333 !important;
            color: white !important; font-weight: bold !important; text-align: center !important;
        }
        .styled-table td { text-align: center !important; }
        </style>
    """, unsafe_allow_html=True)

    # --- HEADER ---
    header_path = f"data/{folder}/tarifas_y_formas_header.png"
    if os.path.exists(header_path):
        _, col_img, _ = st.columns([1.2, 3, 1.2])
        with col_img:
            st.image(header_path)

    path_tarifas = f"data/{folder}/tarifas_y_formas_de_pago.csv"
    
    if os.path.exists(path_tarifas):
        df = pd.read_csv(path_tarifas)
        df.columns = df.columns.str.strip()
        
        def clean_val(val):
            if pd.isna(val): return 0.0
            clean = str(val).replace('$', '').replace('.', '').replace(',', '').replace('s', '').strip()
            try: return float(clean)
            except: return 0.0

        # --- SECCIÓN 1: SELECCIONÁ TU ITINERARIO ---
        st.write("### 📅 Seleccioná tu itinerario")
        planes = df['Programa'].tolist()
        cols_p = st.columns(len(planes))
        
        for i, plan in enumerate(planes):
            partes = plan.split(' ', 1)
            numero = partes[0]
            resto = partes[1] if len(partes) >
