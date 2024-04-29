import streamlit as st
from multipage import MultiPage
#from app_pages import home, about, ocr_comparator
from app_pages import ocr_comparator
app = MultiPage()
st.set_page_config(
    page_title='Zero Code OCR Comparator', layout ="wide",
    initial_sidebar_state="expanded",
)

# Add all your application here
#app.add_page("Home", "house", home.app) # Commented by Bhavani
#app.add_page("About", "info-circle", about.app)# Commented by Bhavani
app.add_page("App", "cast", ocr_comparator.app)

# The main app
app.run()