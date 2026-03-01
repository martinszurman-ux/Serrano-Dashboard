import streamlit as st

def render_excursiones(destino):
    st.markdown(f"<h1 style='text-align: center; color: #1E3A8A;'>🏞️ EXCURSIONES EN {destino.upper()}</h1>", unsafe_allow_html=True)
    st.markdown("---")

    # --- INICIO DEL TRUCO DE LA TV ANTIGUA (CSS) ---
    st.markdown("""
        <style>
        /* Contenedor principal para centrar y dar tamaño al mueble de la TV */
        .tv-container {
            display: flex;
            justify-content: center;
            margin: 20px auto;
            max-width: 480px; /* AQUÍ CONTROLAS EL TAMAÑO TOTAL DEL MUEBLE */
        }

        /* El mueble de la TV (con textura de madera simulada) */
        .old-tv-frame {
            background-color: #5d4037; /* Color base madera marrón */
            background-image: linear-gradient(rgba(0,0,0,0.2) 1px, transparent 1px),
                              linear-gradient(90deg, rgba(0,0,0,0.2) 1px, transparent 1px);
            background-size: 10px 10px; /* Pequeña textura de rejilla */
            border: 15px solid #3e2723; /* Borde exterior más oscuro */
            border-radius: 35px; /* Esquinas muy redondeadas del mueble */
            padding: 20px 25px 65px 20px; /* Espacio interno, más abajo para los botones */
            box-shadow: 10px 10px 25px rgba(0,0,0,0.6); /* Sombra profunda para dar volumen */
            position: relative;
            width: 100%;
        }

        /* La pantalla cóncava (el "vidrio" de la TV) */
        .screen-area {
            background-color: #000;
            border: 8px solid #212121; /* Borde interno de la pantalla */
            border-radius: 20px; /* Redondeo de la pantalla */
            overflow: hidden; /* Para que el video no se salga de las esquinas redondeadas */
            position: relative;
            /* Relación de aspecto 4:3 (formato de TV antigua) */
            padding-top: 75%; 
            box-shadow: inset 0 0 20px rgba(0,0,0,0.8); /* Sombra interna para efecto cóncavo */
        }

        /* Forzar que el iframe del video ocupe todo el espacio de la pantalla */
        .screen-area iframe {
            position: absolute;
            top: 0;
            left: 0;
            width: 100% !important;
            height: 100% !important;
            border: none;
        }

        /* Botón giratorio grande (Selector de canales) */
        .tv-knob-large {
            position: absolute;
            bottom: 18px;
            right: 35px;
            width: 35px;
            height: 35px;
            background: linear-gradient(145deg, #757575, #424242);
            border-radius: 50%;
            border: 3px solid #1a1a1a;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.5);
        }
        .tv-knob-large::before { /* Indicador del selector */
            content: '';
            position: absolute;
            top: 5px;
            left: 50%;
            transform: translateX(-50%);
            width: 4px;
            height: 10px;
            background-color: #1a1a1a;
            border-radius: 2px;
        }

        /* Botón giratorio pequeño (Volumen/Sintonía) */
        .tv-knob-small {
            position: absolute;
            bottom: 25px;
            right: 85px;
            width: 22px;
            height: 22px;
            background: linear-gradient(145deg, #616161, #bdbdbd);
            border-radius: 50%;
            border: 2px solid #1a1a1a;
            box-shadow: 1px 1px 3px rgba(0,0,0,0.5);
        }
        
        /* Rejilla decorativa del altavoz */
        .speaker-grill {
            position: absolute;
            bottom: 20px;
            left: 30px;
            width: 70px;
            height: 35px;
            background-image: radial-gradient(#1a1a1a 2px, transparent 2px);
            background-size: 7px 7px;
            opacity: 0.6;
        }

        /* Pequeña luz de encendido (roja) */
        .power-light {
            position: absolute;
            bottom: 10px;
            right: 50%;
            transform: translateX(50%);
            width: 8px;
            height: 8px;
            background-color: #ff1744;
            border-radius: 50%;
            box-shadow: 0 0 5px #ff1744;
        }
        </style>
    """, unsafe_allow_html=True)
    # --- FIN DEL TRUCO DE LA TV ANTIGUA (CSS) ---

    if "Villa Carlos Paz" in destino:
        st.markdown("### ✨ Nuestro Plan de Actividades Exclusivo")
        st.write("Combinamos aventura, relax y mucha diversión para que cada día sea inolvidable.")
        
        col1, col2, col3 = st.columns(3)

        with col1:
            st.info("🥾 **MOUNTAIN TREKK**\n\nExploración por los senderos serranos con las mejores vistas.")
            st.info("🚗 **CITY TOUR**\n\nRecorrido por los puntos emblemáticos y la costanera.")
            st.info("🍩 **FÁBRICA DE ALFAJORES**\n\nVisita técnica y degustación de los clásicos regionales.")

        with col2:
            st.success("🎢 **CRAZY DONKEY**\n\nUn día de pura adrenalina en el parque de aventuras.")
            st.success("💦 **PARQUE ACUÁTICO**\n\nToboganes, piletas y diversión bajo el sol.")
            st.success("🚀 **JUMPING GAMES**\n\nDesafío de altura y saltos en camas elásticas.")

        with col3:
            st.warning("🏖️ **BEACH DAY**\n\nRelax y actividades recreativas a la vera del lago.")
            st.warning("👑 **KING PARK**\n\nEntretenimiento de vanguardia y juegos mecánicos.")
            st.warning("🐒 **COCOGUANA**\n\nParque aéreo y tirolesas en un entorno natural único.")

        # --- VIDEO EN TV PARA CARLOS PAZ ---
        st.markdown("---")
        st.markdown("### 📽️ ¡Viví la Experiencia Serrano en la Villa!")
        
        # ID del video de YouTube (sacado de tu URL: ZG_3Bc8wkx8)
        video_id_cp = "ZG_3Bc8wkx8"
        
        st.markdown(f"""
            <div class="tv-container">
                <div class="old-tv-frame">
                    <div class="screen-area">
                        <iframe 
                            src="https://www.youtube.com/embed/{video_id_cp}?autoplay=0&muted=1&controls=1" 
                            title="Experiencia Serrano Carlos Paz" 
                            frameborder="0" 
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                            allowfullscreen>
                        </iframe>
                    </div>
                    <div class="speaker-grill"></div>
                    <div class="tv-knob-large"></div>
                    <div class="tv-knob-small"></div>
                    <div class="power-light"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    elif "San Pedro" in destino:
        st.markdown("### 🚣 Experiencias en la Naturaleza")
        st.write("Disfrutá de la historia, la aventura y la mejor gastronomía a orillas del Paraná.")

        col1, col2 = st.columns(2)
        with col1:
            st.error("🏰 **EL FUERTE DE OBLIGADO**\n\nTurismo aventura: palestra, péndulo, rappel, tirolesa y toboganes. Incluye almuerzo de asado criollo libre.")
            st.info("🏖️ **BEACH DAY CON CANOTAJE**\n\nBalneario privado con actividades recreativas y bautismo de canotaje en sector seguro.")
            st.success("🌿 **COMPLEJO LAS AMALIAS**\n\nLaberinto de ligustrinas, plaza húmeda, piletas, fútbol y vóley.")

        with col2:
            st.warning("🌅 **SUNSET CATAMARÁN**\n\nPaseo exclusivo por el Río Paraná disfrutando del atardecer y la mejor música.")
            st.info("🏛️ **CITY TOUR**\n\nRecorrido por barrancas, Vía Crucis y compras de artículos regionales típicos.")

        # --- VIDEO EN TV PARA SAN PEDRO ---
        st.markdown("---")
        st.markdown("### 📽️ ¡Serrano en San Pedro!")
        
        # ID del video de YouTube (sacado de tu URL: xBDqSrNB8Ro)
        video_id_sp = "xBDqSrNB8Ro"
        
        st.markdown(f"""
            <div class="tv-container">
                <div class="old-tv-frame">
                    <div class="screen-area">
                        <iframe 
                            src="https://www.youtube.com/embed/{video_id_sp}?autoplay=0&muted=1&controls=1" 
                            title="Serrano en San Pedro" 
                            frameborder="0" 
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                            allowfullscreen>
                        </iframe>
                    </div>
                    <div class="speaker-grill"></div>
                    <div class="tv-knob-large"></div>
                    <div class="tv-knob-small"></div>
                    <div class="power-light"></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.info("Estamos terminando de coordinar las mejores actividades para este destino. ¡Próximamente!")

    st.markdown("---")
    st.caption("⚠️ *El orden de las excursiones está sujeto a condiciones climáticas y logística de la coordinación.*")
