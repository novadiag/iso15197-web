import streamlit as st
import os

st.set_page_config(page_title="ISO 15197:2013 Standardı", layout="wide")

st.title("📘 ISO 15197:2013 Standardı Web Yayını")

# Bulunduğunuz dizindeki tüm .md dosyaları al
section_files = sorted([f for f in os.listdir(".") if f.endswith(".md")])

# Menü - bölüm seçimi
selected_section = st.sidebar.selectbox("📂 Bölüm Seçin", section_files)

# Seçilen dosyayı aç ve göster
with open(selected_section, "r", encoding="utf-8") as file:
    content = file.read()
    st.markdown(content, unsafe_allow_html=True)
