# ... (Mantenemos secciones 1, 2, 3 y 4 exactamente igual a como las tenías) ...

# 5. CONSTRUCCIÓN DEL NAVBAR DINÁMICO
logo_url = "https://serranoturismo.com.ar/assets/images/logoserrano-facebook.png"

# --- ESTRUCTURA PARA DESKTOP (Se mantiene la que funcionaba antes) ---
if not dest_actual:
    links_desktop = f"""
        <span style="color: #888; font-size: 12px; font-weight: 600; text-transform: uppercase; margin-right: 5px;">Elegí tu destino:</span>
        <a href="./?nav=Home&destino=San+Pedro" class="btn-destino" target="_self">SAN PEDRO</a>
        <a href="./?nav=Home&destino=Villa+Carlos+Paz" class="btn-destino" target="_self">CARLOS PAZ</a>
    """
else:
    links_desktop = f"""
        <a href="./?nav=Home" class="nav-item" target="_self">HOME</a>
        <div class="dropdown">
            <button class="dropbtn">CONOCÉ TU VIAJE ▼</button>
            <div class="dropdown-content">
                <a href="./?nav=Transporte&destino={dest_actual}" target="_self">Transporte</a>
                <a href="./?nav=Hoteleria&destino={dest_actual}" target="_self">Hotelería</a>
                <a href="./?nav=Comidas&destino={dest_actual}" target="_self">Comidas</a>
                <a href="./?nav=Excursiones&destino={dest_actual}" target="_self">Excursiones</a>
                <a href="./?nav=Actividades&destino={dest_actual}" target="_self">Actividades</a>
                <a href="./?nav=Seguro&destino={dest_actual}" target="_self">Seguro / Coordinación</a>
            </div>
        </div>
        <div class="dropdown">
            <button class="dropbtn">ARMÁ TU VIAJE ▼</button>
            <div class="dropdown-content">
                <a href="./?nav=Tarifas&destino={dest_actual}" target="_self">Tarifas</a>
                <a href="./?nav=Adhesion&destino={dest_actual}" target="_self">Ficha de Adhesión</a>
            </div>
        </div>
    """

# --- ESTRUCTURA PARA MOBILE (Menú 3 líneas / Colapsable) ---
if not dest_actual:
    content_mobile = f"""
        <div class="nav-links-mobile-visible">{links_desktop}</div>
    """
else:
    content_mobile = f"""
        <details class="menu-desplegable">
            <summary class="logo-box-summary">
                <img src="{logo_url}">
                <span class="menu-label">MENÚ ☰</span>
            </summary>
            <div class="nav-links-mobile-collapsed">{links_desktop}</div>
        </details>
    """

# INYECCIÓN FINAL: Desktop y Mobile viven en contenedores separados
st.markdown(f"""
    <div class="navbar desktop-only">
        <div class="logo-box">
            <a href="./?nav=Home" target="_self"><img src="{logo_url}"></a>
        </div>
        <div class="nav-links">{links_desktop}</div>
        <div style="width:110px;"></div>
    </div>

    <div class="navbar-mobile mobile-only">
        {content_mobile if dest_actual else f'<div class="logo-box-mobile-home"><img src="{logo_url}"></div>' + content_mobile}
    </div>
""", unsafe_allow_html=True)

# 6. RENDERIZADO DE CONTENIDO
# ... (Igual que antes) ...
