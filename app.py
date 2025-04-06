import streamlit as st
import os

# Sayfa başlığı
st.set_page_config(page_title="ISO 15197:2013 Standardı", layout="wide")
st.title("📘 ISO 15197:2013 Standardı Web Yayını")

# Dosya klasörü
SECTIONS_DIR = "."


# Menü başlıklarını al (dosya adlarından)
section_files = sorted([f for f in os.listdir(SECTIONS_DIR) if f.endswith(".md")])

# Sidebar menüsü
selected_section = st.sidebar.selectbox("📂 Bölüm Seçin", section_files)

# Seçilen markdown dosyasını göster
with open(os.path.join(SECTIONS_DIR, selected_section), "r", encoding="utf-8") as f:
    content = f.read()
    st.markdown(content, unsafe_allow_html=True)
