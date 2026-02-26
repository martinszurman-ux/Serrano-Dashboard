import streamlit as st
import pandas as pd
import os

def render_tarifas(destino):
    folder = "vcp" if destino == "Villa Carlos Paz" else "san_pedro"
    
    # Función de actualización de estado
    def seleccionar_plan(indice):
        st.session_state[f"sel_index_{folder}"] = indice

    # Estilos CSS: Limpieza y centralización de encabezados
    st.markdown("""
        <style>
        .plan-card-click {
            border-radius: 15px; padding: 15px; background: white;
            border: 2px solid #eee; transition: all 0.3s ease;
            min-height: 140px; position: relative;
            display: flex; flex-direction: column; justify-content: center;
        }
        .selected-plan { 
            border: 3px solid #d32f2f !important; 
            background-color: #fff5f5 !important;
        }
        .card-top {
            display: flex; justify-content: center; align-items: center;
            gap: 12px; margin-bottom: 5px;
        }
        .day-number { color: #d32f2f; font-size: 3.2rem; font-weight: 900; line-height: 1; }
        .transport-icon-big { font-size: 2.5rem; }
        .day-text-bottom { 
            color: #495057; font-size: 0.85rem; font-weight: 700; 
            text-transform: uppercase; text-align: center;
        }
        
        .stButton button {
            background-color: transparent !important; border: none !important;
            color: transparent !important; height: 140px !important;
            width: 100% !important; position: absolute; top: 0; left: 0;
            z-index: 10; cursor: pointer;
        }

        .widget-3d-inner {
            background: linear-gradient(145deg, #f0f0f0, #ffffff);
            border-radius: 15px; padding: 20px; text-align: center;
            border: 1px solid #ddd;
            box-shadow: inset 3px 3px 6px #d1d1d1, inset -3px -3px 6px #ffffff;
            min-height: 160px; display: flex; flex-direction: column; 
            justify-content: center; align-items: center;
        }

        /* Formato de Tabla: Centralizado y Negrita en Encabezados */
        th {
            text-align: center !important;
            font-weight: bold !important;
            text-transform: uppercase;
            color: #333 !important;
            background-color: #f2f2f2 !important;
        }
        td {
            text-align: center !important;
        }
        </style>
    """, unsafe_allow_html=True)

    path_tarifas = f"data
