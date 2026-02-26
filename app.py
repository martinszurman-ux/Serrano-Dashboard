import streamlit as st
import pandas as pd
import os

# 1. Configuración de página y Estética Profesional (Grises)
st.set_page_config(page_title="Serrano Turismo - Dashboard", layout="wide")

st.markdown("""
    <style>
    /* Fondo general y fuentes */
    .main { background-color: #ffffff; }
    
    /* Contenedores con bordes y fondo gris profesional */
    [data-testid="stVerticalBlockBorderWrapper"] {
        background-color: #f8f9fa !important;
        border: 1px solid #dee2e6 !important;
        border-radius: 12px !important;
        padding: 20px !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.02) !important;
    }
    
    /* Estilo del Header con la imagen de tarifas */
    .header-container {
        position: relative;
        height: 220px;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 15px;
        margin-bottom: 30px;
        background-color: #495057;
    }
    
    .header-img-styled {
        width: 100%;
        height: 220px;
        object-fit: cover;
        border-radius: 15px;
        filter: brightness(0.6);
    }
    
    .header-text-overlay {
        position: absolute;
        text-align: center;
        font-size: 2.5rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.6);
    }

    /* Ajustes de texto en los widgets de monto */
    .widget-title {
        color: #6c757d;
        font-size: 0.85rem;
        font-weight: 700;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .widget-value {
        color: #212529;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0;
    }

    .promo-subtitle {
        font-size: 0.75rem;
        color: #adb5bd;
        margin-top: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Logo y Sidebar
LOGO_URL = "
