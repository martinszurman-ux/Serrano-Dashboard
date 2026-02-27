import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# =================================================================
# 📋 MÓDULO: SOLICITUD DE ADHESIÓN (Serrano Turismo)
# VERSIÓN: Ultra-Fix Mobile (Corregido: Nombres de Planes)
# =================================================================

def render_adhesion(logo_url):
    # CSS Total para corregir visibilidad en Mobile y modo oscuro
    st.markdown("""
        <style>
        /* 1. Reset de visibilidad y colores (Anti Modo Oscuro) */
        .main {
            background-color: white !important;
        }
        .main .block-container { 
            padding-top: 3.5rem !important; 
            padding-bottom: 1rem !important; 
            color: black !important;
        }

        /* Forzar etiquetas visibles */
        label p {
            color: black !important;
            font-weight: 600 !important;
            font-size: 0.85rem !important;
        }

        /* Forzar inputs legibles */
        input {
            color: black !important;
            background-color: #f0f2f6 !important;
            border: 1px solid #dcdcdc !important;
        }

        /* 2. FIX MENÚ: Mostrar cabecera nativa */
        [data-testid="stHeader"] { 
            display: flex !important; 
            visibility: visible !important;
            background-color: rgba(255,255,255,0.9) !important;
        }

        /* 3. TRUCO COLUMNAS MOBILE: Forzar 2 o más por fila */
        @media (max-width: 768px) {
            [data-testid="stHorizontalBlock"] {
                flex-direction: row !important;
                display: flex !important;
                flex-wrap: nowrap !important;
                gap: 5px !important;
            }
            [data-testid="column"] {
                width: auto !important;
                min-width: 0px !important;
                flex: 1 1 auto !important;
            }
            h2 { font-size: 1.1rem !important; }
            .stMarkdown p { font-size: 0.8rem !important; }
        }

        /* 4. MODO IMPRESIÓN */
        @media print {
            @page { size: A4; margin: 0.4cm; }
            html, body { zoom: 85%; }
            header, [data-testid="stSidebar"], .no-print, .stButton, footer, [data-testid="stHeader"] {
                display: none !important;
            }
            .main .block-container { padding: 0 !important; margin: 0 !important; }
            input
