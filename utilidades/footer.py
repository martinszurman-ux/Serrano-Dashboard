import streamlit as st

def render_footer():
    """Footer definitivo con exterminio total de badges de Streamlit Cloud"""
    
    st.markdown("""<style>
#MainMenu, footer, header, [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"], [data-testid="stAppCreatorProfile"], [data-testid="stViewerBadge"], [class^="viewerBadge"], [class*="viewerBadge"], .stDeployButton {visibility: hidden !important; display: none !important;}
.main .block-container {padding-bottom: 0rem !important;}
.footer-container {background-color: white; border-top: 1px solid #eee; padding: 30px 20px; margin-top: 50px; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; width: 100%; font-family: sans-serif;}
.f-col {flex: 1; min-width: 250px; margin: 10px 0;}
.f-brand h4 {color: #333333 !important; font-weight: 800; font-size: 1.1rem; margin: 0; text-transform: uppercase;}
.f-brand p {color: #888; font-size: 0.85rem; margin-top: 5px;}
.f-center {flex: 2; text-align: center; color: #555; font-size: 0.9rem;}
.f-center p {margin: 4px 0; line-height: 1.3;}
.f-right {text-align: right;}
.f-right a {color: #333 !important; font-size: 1.5rem; margin-left: 20px; text-decoration: none !important;}
.wa-float {position: fixed; bottom: 30px; left: 30px; background-color: #25d366; color: white !important; width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 30px; z-index: 999999; box-shadow: 0 4px 12px rgba(0,0,0,0.25); text-decoration: none !important;}
</style>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
<div class="footer-container">
<div class="f-col f-brand">
<h4>SERRANO TURISMO</h4>
<p>29 años de trayectoria. © 2026</p>
</div>
<div class="f-col f-center">
<p>📍 Av. Rivadavia 4532 - Galería Alefa (Local 10) - CABA</p>
<p>📍 Del Cimarrón 1846 - 1er Piso (Of. 4) - Parque Leloir</p>
<p>📞 11-4847-6467</p>
</div>
<div class="f-col f-right">
<a href="https://instagram.com/serrano_turismo" target="_blank"><i class="fab fa-instagram"></i></a>
<a href="https://facebook.com/serranoturismo" target="_blank"><i class="fab fa-facebook-f"></i></a>
</div>
</div>
<a href="https://wa.me/5491156096283" class="wa-float" target="_blank">
<i class="fab fa-whatsapp"></i>
</a>""", unsafe_allow_html=True)
